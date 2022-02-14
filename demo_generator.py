""" 
Table Type Demo App


"""
import os
import time
import requests
import webbrowser

# Installed Libraries
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from streamlit.elements.pyplot import PyplotGlobalUseWarning

# Custom Modules
import crud
from utils import pagenate
from model import RunningApp
from subprocess_jobs import deploy_app

# Configures the default settings of the page
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

link = '[GitHub](http://github.com)'
st.markdown(link, unsafe_allow_html=True)


if st.button('Github으로 이동하기'):
    url = 'https://www.streamlit.io/'
    webbrowser.open_new_tab(url)


def show_deploy_form():
    """App Deploy Form
    """
    st.header("⚙️ Generator️")

    with st.form("my_form"):
        app_path = st.selectbox(
            label='App Path',
            options=[f'{x.path} ({x.desc})' for x in crud.read_app_meta()]
        )
        col1, col2 = st.columns(2)
        # slider_val = st.slider("Form slider")
        # checkbox_val = st.checkbox("Form checkbox")
        with col1:
            runner = st.text_input(
                label='Runner',
                placeholder='작업을 제출하는 분의 이름 또는 아이디를 적어주세요'
            )

        # Every form must have a submit button.
        deploy_btn = st.form_submit_button("Deploy")
        if deploy_btn:
            # simple validation
            if not runner:
                st.error('! 작업 제출자의 이름 또는 아이디가 필요합니다 😅')
            else:
                status = deploy_app(app_path)
                if status is None:
                    crud.create_history()
                    # TODO: Running App에 추가


def show_running_app():
    """현재 구동 중인 App의 정보를 보여준다.
    서버에서 사용 중인 Port를 ps aux | grep 'meta.ini' 과 같이 조회하여
    os 모듈에서 지원할듯

    AppMeta Table에서 해당 정보를 가져와서 보여준다. 
    또한 Go, Kill 버튼을 제공한다.

    Go를 누르면 해당 링크로 이동
    Kill을 누르면 포트를 찾아서 죽인다.
    """
    st.header("🏃‍♀️ Running Apps")
    # description, port
    # path, running script, port, create time, runner, 담당자, kill time, load time, (deploy button), (kill button), (link button)
    # → meta 데이터를 추가해줄 것(그러면 running script등 명시할 필요가 없어진다)
    sample_data = [
        {'desc': '검색용 NER', 'port': '10000',
            'create': '20220107201310', 'kill': '', 'duration': '20s'},
        {'desc': 'Query Segmentation', 'port': '10010',
            'create': '20220107201320', 'kill': '', 'duration': '100s'},
        {'desc': 'Semantic Role Labeling', 'port': '10020',
            'create': '20220108101310', 'kill': '', 'duration': '5s'},
    ]

    col_names = ['Index', 'Desc', 'Port', 'Create', 'Button', 'Redeploy']
    n_cols = 6
    cols = st.columns(n_cols)
    for i, field in enumerate(col_names):
        cols[i].write(field)

    for i, dat in enumerate(sample_data):
        cols = st.columns(n_cols)
        # for j in range(n_cols):
        #    cols[j].write(dat[''])
        cols[0].write(i)
        cols[1].write(dat['desc'])
        cols[2].write(dat['port'])
        cols[3].write(dat['create'])
        demo_button = cols[4].empty().button('Go to Demo', key=f'demo_btn_{i}')
        redeploy_button = cols[5].empty().button(
            'Redeploy', key=f'redeploy_btn_{i}')
        # st.button(label='Go to Demo', key=f'button_{i}'))
        if demo_button:
            placeholder = st.empty()
            placeholder.info('You clicked [Demo] button')
            # st.info('You clicked [Demo] button')
            # do something here
            time.sleep(1)
            placeholder.success('Success')
            # # 여러 개를 보여주고 싶은 경우
            # with placeholder.container():
            #     st.write('asfdsf')
            #     st.write('adfsafafsfdsf')

        if redeploy_button:
            # do something here
            with st.spinner('잠시만 기다려주세요'):
                st.info('You clicked [Redeploy] button')
                time.sleep(2)
                st.balloons()
            # 문제가 생겼을 경우에는
            # name = st.text_input('Name')
            # if not name:
            #   st.warning('Please input a name.')
            #   st.stop()
            # st.success('Thank you for inputting a name.')
    pass


def show_historical_run():
    """ Deploy 버튼으로 제출한 작업 히스토리들 """
    st.header("🔎 Historical Run")
    # history_list = crud.read_history()
    # col_names = crud.read_history_columns()
    history_list = crud.read_app_meta()
    col_names = crud.read_app_meta_columns()

    history_data = []
    for history in history_list:
        history_data.append(
            {col_name:getattr(history, col_name) 
             for col_name in col_names}
        )
    history_data = pd.DataFrame(history_data)
    pagenate(history_data)
    # st.write(history_data)


def refresh():
    """페이지를 새로고침 하거나 이벤트가 발생하는 경우 앱에서 활용하는 데이터를
    업데이트 한다.
    예: Deploy Form 에서 활용하는 AppMeta 데이터를 업데이트
        - Repo에 Push를 하여 새로운 앱이 추가/삭제/업데이트 된 경우
    예: Running App 업데이트
        - 서버 문제로 Running App이 죽은 경우 업데이트 필요
    """
    pass


def app():

    st.title('Hello World!')

    refresh()
    show_deploy_form()
    show_running_app()
    show_historical_run()


if __name__ == '__main__':
    app()
