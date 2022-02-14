import streamlit as st



def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def pagenate(df):
    """ https://github.com/streamlit/release-demos/blob/0.84/0.84/demos/pagination.py """

    def _next_page():
        st.session_state.page += 1

    def _prev_page():
        st.session_state.page -= 1


    if "page" not in st.session_state:
        st.session_state.page = 0

    _, col1, col2, col3 = st.columns([0.63, 0.1, 0.17, 0.1])

    if st.session_state.page < 4:
        col3.button(">", on_click=_next_page)
    else:
        col3.write("")  # this makes the empty column show up on mobile

    if st.session_state.page > 0:
        col1.button("<", on_click=_prev_page)
    else:
        col1.write("")  # this makes the empty column show up on mobile

    col2.write(f"Page {1+st.session_state.page} of {5}")
    start = 10 * st.session_state.page
    end = start + 10
    st.write(df.iloc[start:end])


if __name__ == '__main__':
    print(is_port_in_use(8501))