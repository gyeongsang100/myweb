import streamlit as st

과목 = st.selectbox("과목을 선택하세요", ["확률과 통계", "미분과 적분", "기하와 벡터"])
st.subheader(f"당신이 선택한 과목은 {과목}입니다.")

total = 0
# 체크박스
check1 = st.checkbox("짜장면(5000원)")
check2 = st.checkbox("짬뽕(7000원)")
check3 = st.checkbox("탕수육(15000원)")
if check1:
    total += 5000
if check2:
    total += 7000
if check3:
    total += 15000

st.subheader(f"선택한 음식의 가격은 {total}원 입니다")


