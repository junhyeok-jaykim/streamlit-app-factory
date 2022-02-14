""" 
Table Type Demo App

"""
import os
import requests

# Installed Libraries
import streamlit as st
import pandas as pd

def _json_to_table(json_input, fields=None):
    try:
        res = json_input['result']
    except:
        # TODO: logging
        return ['Request Error']
    if fields is not None:
        new_res = []
        for item in res:
            new_item = {}
            for field in fields:
                if field in item:
                    new_item[field] = item[field]
            new_res.append(new_item)
        res = new_res
    return pd.DataFrame(res).style.format(precision=2)

def app():
    # FIXME: 테스크에 맞는 타이틀로 변경
    st.title("Table Demo")
    query = st.text_input(
        label="Search",
        value="Your Default Text"
        # placeholder="텍스트를 입력해주세요"
    )
    st.subheader("Result")

    if query:
        samples = [
            {'rank': 1, 'name': 'a'},
            {'rank': 2, 'name': 'b'},
            {'rank': 3, 'name': 'c'},
            {'rank': 4, 'name': 'd'},
        ]
        st.table(samples)
        # r = requests.get(api.format(query=query))
        # output = r.json()
        # fields = ['rank', 'score', 'segmentation', 'label']
        # st.table(_json_to_table(output, fields=fields))


if __name__ == '__main__':
    app()
