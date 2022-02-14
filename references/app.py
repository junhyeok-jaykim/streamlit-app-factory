"""[summary]

[Streamlit Configuration]
    vi ~/.streamlit/config.toml
    https://docs.streamlit.io/library/advanced-features/configuration
"""
import os

# Installed Libraries
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
#from pages import data_upload, machine_learning, metadata, data_visualize, redundant # import your pages here
from single_apps import (
    empty,
    ref_data_upload,
    ref_annotated_text,
    ref_cheat_sheet,
)
def configure_page():
    st.set_page_config(
         #page_title='Streamlit cheat sheet',
         layout="wide",
         initial_sidebar_state="expanded",
    )

def main():
    # TODO: selectbox에 항목이 선택되면, 나머지는 --select--의 빈페이지로 바꿔서 엉키지 않게 하기
    # 또한 widget에 필요한 항목들이 더 생길 수 있음.

    configure_page()

    # TODO: 사이드바로 넣기
    # Title of the main page
    display = Image.open('Logo.png')
    display = np.array(display)
    # st.image(display, width = 400)
    # st.title("Data Storyteller Application")
    col1, col2 = st.columns(2)
    col1.image(display, width = 400)
    col2.title("Data Storyteller Application")

    # ////////////////////////////////
    # Apps for Projects
    # ////////////////////////////////
    project_apps = MultiPage()
    #project_apps.add_page("Upload Data", ref_data_upload.app)
    project_apps.add_page("Our Projects", ref_annotated_text.app)
    project_apps.add_page("Annotated Text", ref_annotated_text.app)

    # run apps
    #project_apps.run(sidebar_text="Projects", sidebar_type="radio")
    project_apps.run(sidebar_text="Projects", sidebar_type="selectbox")

    # ////////////////////////////////
    # Apps for Demo
    # ////////////////////////////////
    demo_apps = MultiPage()
    demo_apps.add_page("--- Select ---", empty.app)
    demo_apps.add_page("Annotated Text", ref_annotated_text.app)

    # run apps
    demo_apps.run(sidebar_text="Demo", sidebar_type="selectbox")

    # ////////////////////////////////
    # Apps for References
    # ////////////////////////////////
    reference_apps = MultiPage()

    # Add all your application here
    reference_apps.add_page("--- Select ---", empty.app)
    reference_apps.add_page("Upload Data", ref_data_upload.app)
    reference_apps.add_page("Annotated Text", ref_annotated_text.app)
    reference_apps.add_page("Streamlit Cheatsheet", ref_cheat_sheet.app)
    #reference_apps.add_page("Change Metadata", metadata.app)
    #reference_apps.add_page("Machine Learning", machine_learning.app)
    #reference_apps.add_page("Data Analysis",data_visualize.app)
    #reference_apps.add_page("Y-Parameter Optimization",redundant.app)

    # run apps
    reference_apps.run(sidebar_text="Reference Apps", sidebar_type="selectbox")


if __name__ == "__main__":
    main()
