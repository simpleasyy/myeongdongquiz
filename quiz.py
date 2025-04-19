import streamlit as st
import pandas as pd

st.title("일반상식 퀴즈 웹앱")

# 파일 업로드 받기
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=['xlsx'])

if uploaded_file is not None:
    # 엑셀파일 읽기
    sheet_name = '일반상식'
    df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

    # 문제와 답 추출
    questions = df.iloc[:, 0]
    answers = df.iloc[:, 1]

    # 세션 상태 초기화
    if 'q_idx' not in st.session_state:
        st.session_state.q_idx = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0

    # 문제 보여주기
    st.write(f"문제 {st.session_state.q_idx + 1}: {questions[st.session_state.q_idx]}")

    # 사용자 입력
    user_answer = st.text_input("당신의 답은?")

    if st.button("제출"):
        correct_answer = str(answers[st.session_state.q_idx]).strip()
        if user_answer.strip() == correct_answer:
            st.success("정답입니다!")
            st.session_state.score += 1
        else:
            st.error(f"오답입니다! 정답은: {correct_answer}")

        st.session_state.q_idx += 1
        if st.session_state.q_idx >= len(questions):
            st.write(f"퀴즈가 끝났습니다! 총 점수: {st.session_state.score} / {len(questions)}")
            st.session_state.q_idx = 0
            st.session_state.score = 0

