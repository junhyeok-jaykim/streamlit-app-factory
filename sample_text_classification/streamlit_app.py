""" Text Classification Demo


"""

from os import name
import streamlit as st
from annotated_text import annotated_text

def load_sample_text(sample_file_path):
    """[샘플 데이터가 있는 경우 불러오는 함수]

    Args:
        sample_file_path ([str]): 샘플 데이터 경로

    Returns:
        [list]: list of sample text
    """
    samples = []
    return samples

# TODO: 샘플 데이터 박스, 버튼 추가, 버튼 이미지 등 커스터마이징
# 페이지 커스터마이징
def app():
    import streamlit as st

    # FIXME: 테스크에 맞는 타이틀로 변경
    st.title("Text Classification Demo")
    query = st.text_input(
        label="Search",
        placeholder="텍스트를 입력해주세요"
    )
    st.subheader("Result")

    if query:
        # FIXME: 모델 또는 Web API로 요청 받은 쿼리에 대한 결과를 가져온다.
        # load model
        # predict, e.g. output = ner_model.predict(query)
        # transform output like below
        st.subheader(f'Your query is "{query}"')

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



if __name__ == '__main__':
    app()
