import streamlit as st

# 왼쪽 사이드바
menu = st.sidebar.selectbox("MENU", ["로그인", "회원가입"])

# 로그인
db_id = "test"
db_pw = "123"

if menu == "로그인":
    st.title("😜로그인")
    id = st.text_input("아이디", placeholder="아이디를 입력하세요.")
    pw = st.text_input("비밀번호", type="password")
    login = st.button("로그인")

    if login:
        if db_id == id and db_pw == pw:
            st.success("로그인 성공")
            st.balloons()
        else:
            st.error("로그인 실패")
            st.snow()
elif menu == "회원가입":
    st.title("회원가입💖😍")
    st.video("https://youtu.be/VcWqTV7bswY")


# 이미지 가져오기 - Media elements
# import streamlit as st
# st.image("sunrise.jpg", caption="Sunrise by the mountains")

# 과목 = st.selectbox("과목을 선택하세요", ["확률과 통계", "미분과 적분", "기하와 벡터"])
# st.subheader(f"당신이 선택한 과목은 {과목}입니다.")

# total = 0
# # 체크박스
# check1 = st.checkbox("짜장면(5000원)")
# check2 = st.checkbox("짬뽕(7000원)")
# check3 = st.checkbox("탕수육(15000원)")
# if check1:
#     total += 5000
# if check2:
#     total += 7000
# if check3:
#     total += 15000

# st.subheader(f"선택한 음식의 가격은 {total}원 입니다")