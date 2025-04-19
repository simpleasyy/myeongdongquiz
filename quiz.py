import streamlit as st
import pandas as pd

# 엑셀 파일 읽기
file_path = '/mnt/data/2025 문제.xlsx'
sheet_name = '일반상식'

df = pd.read_excel(file_path, sheet_name=sheet_name)

# 문제와 답 추출 (예를 들면, 문제는 1열, 답은 2열이라고 가정)
questions = df.iloc[:, 0]
answers = df.iloc[:, 1]

# 문제 인덱스 저장
if 'q_idx' not in st.session_state:
    st.session_state.q_idx = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

# 문제 보여주기
st.title("일반상식 퀴즈")
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
