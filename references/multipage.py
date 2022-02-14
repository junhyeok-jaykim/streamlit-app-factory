"""
This file is the framework for generating multiple Streamlit applications 
through an object oriented framework. 
"""

# Import necessary libraries 
import streamlit as st

# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self):
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.single_apps = []
    
    def add_page(self, title, execute_func):
        """Class Method to Add single apps to the project

        Args:
            title ([str]): The title of page which we are adding to the list of apps 
            
            func: Python function to render this page in Streamlit
        """

        self.single_apps.append(
            {
                "title": title, 
                "executer": execute_func
            }
        )

    def run(self, sidebar_text="Write Sidebar Text", sidebar_type="selectbox"):
        """ when user click sidebar element, then streamlit will rerun the script """
        # Drodown to select the page to run  
        sidebar = None
        if sidebar_type == 'selectbox':
            sidebar = st.sidebar.selectbox
        elif sidebar_type == 'radio':
            sidebar = st.sidebar.radio
        else:
            raise ValueError(
                f"Only Support 'selectbox', 'radio' sidebar type: {sidebar_type}")
    
        single_app = sidebar(
            sidebar_text,
            self.single_apps, 
            format_func=lambda single_app: single_app['title']
        )

        # run the app function 
        single_app['executer']()