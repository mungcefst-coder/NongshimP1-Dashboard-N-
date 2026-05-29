import streamlit as st
from datetime import datetime

# 전역 설정
MAIN_BLUE = "#3B82F6"       
BRAND_NAVY = "#1E40AF"       

st.set_page_config(layout="wide", page_title="[실험실] Smart 수율 모니터링 System")

# 세션 제어 변수 초기화
if 'logged_in' not in st.session_state: 
    st.session_state['logged_in'] = False

# 로그인 처리 함수
def login():
    uid = st.session_state.username
    upw = st.session_state.password
    if uid == "admin" and upw == "admin5678":
        st.session_state['logged_in'] = True
    else: 
        st.error("⚠️ 아이디 또는 비밀번호가 올바르지 않습니다.")

# --- 라우터 (로그인 여부에 따라 화면 전환) ---
if not st.session_state['logged_in']:
    # 📌 3단계에서 여기에 들어갈 '예쁜 로그인 UI'를 집중적으로 깎을 겁니다!
    _, login_grid, _ = st.columns([1, 1.5, 1])
    with login_grid:
        st.title("🔐 실험실 로그인")
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        st.button("로그인", on_click=login, use_container_width=True)
else:
    # 로그인 성공 시 나오는 메인 화면 틀
    st.success("🎉 로그인 성공! 메인 대시보드 구역입니다.")
    if st.button("🔓 로그아웃"):
        st.session_state['logged_in'] = False
        st.rerun()
