

""" 
Highlighting Row

st.dataframe(
    pd.DataFrame(sample_data)
    .style.apply(highlight, axis=1)
    .set_properties(**{"color": "#FFF"})
)
"""
def highlight(series: pd.Series) -> list:
    """return list same width as row to apply styling
    Args:
        series (pd.Series): one row of data from chosen datafram
    Returns:
        list: list same size as series with styling to apply
    """
    return ["background-color: #3e9456"] * (len(series))
    #if series.is_success >= 1:
    #    return ["background-color: #3e9456"] * (len(series))
    #else:
    #    return ["background-color: #a62100"] * (len(series))


    if st.button("the notice you want to show"):
        st.write("content you want to show")

    st.text_input("Your name", key="name")

    # This exists now:
    st.session_state.name