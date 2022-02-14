import streamlit as st
from annotated_text import annotated_text

# @st.cache
def app():
    import streamlit as st

    """
    # Annotated text example
    
    Below is an example of how to use the annotated_text function:
    """
    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)

    annotated_text(
        "This ",
        ("is", "verb", "#8ef"),
        " some ",
        ("annotated", "adj", "#faa"),
        ("text", "noun", "#afa"),
        " for those of ",
        ("you", "pronoun", "#fea"),
        " who ",
        ("like", "verb", "#8ef"),
        " this sort of ",
        ("thing", "noun", "#afa"),
    )
