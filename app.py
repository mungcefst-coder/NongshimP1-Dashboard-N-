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
    
    # 🎨 1. 화면 전체에 스타일을 부여하는 Custom CSS (유리 질감 & 폰트)
    st.markdown("""
        <style>
            /* 전체 배경을 조금 더 모던한 딥 네이비/그레이 톤으로 변경 */
            .stApp {
                background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
            }
            
            /* 유리 질감(Glassmorphism) 로그인 카드 스타일 */
            .glass-login-card {
                background: rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 24px;
                padding: 40px;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
                text-align: center;
                margin-top: 10vh; /* 화면 상단에서 약간 떨어뜨리기 */
            }
            
            /* 카드 내부 텍스트 스타일 */
            .card-title {
                color: #FFFFFF !important;
                font-size: 28px !important;
                font-weight: 800 !important;
                margin-bottom: 6px !important;
                letter-spacing: -0.5px;
            }
            .card-subtitle {
                color: #94A3B8 !important;
                font-size: 12px !important;
                font-weight: 600 !important;
                letter-spacing: 1.5px;
                margin-bottom: 35px !important;
                text-transform: uppercase;
            }
            
            /* Streamlit 내부 입력창 테두리선 정돈 */
            div[data-testid="stForm"] {
                border: none !important;
                padding: 0 !important;
                background: transparent !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # 🏢 2. 레이아웃 배치 (좌우 빈 공간을 두어 중앙으로 모으기)
    _, login_container, _ = st.columns([1, 1.2, 1])
    
    with login_container:
        # HTML로 예쁜 카드 상단 디자인 그리기
        st.markdown("""
            <div class="glass-login-card">
                <div class="card-title">🔐 SYSTEM ACCESS</div>
                <div class="card-subtitle">Busan Plant Production Team 1</div>
            </div>
        """, unsafe_allow_html=True)
        
        # 입력창과 버튼은 카드 바로 아래 자연스럽게 이어지도록 st.form 활용
        with st.form("login_form", clear_on_submit=False):
            st.text_input("Username", key="username", placeholder="사번 또는 ID를 입력하세요")
            st.text_input("Password", type="password", key="password", placeholder="비밀번호를 입력하세요")
            
            # 버튼도 일반 버튼 대신 양옆으로 꽉 찬 모던한 버튼으로 변경
            submit_button = st.form_submit_button("보안 시스템 접속", use_container_width=True)
            
            if submit_button:
                login() # 폼이 제출되면 위에서 만든 login 함수 실행
                
else:
    # 로그인 성공 시 나오는 메인 화면 틀 (기존과 동일)
    st.success("🎉 로그인 성공! 메인 대시보드 구역입니다.")
    if st.button("🔓 로그아웃"):
        st.session_state['logged_in'] = False
        st.rerun()
    if st.button("🔓 로그아웃"):
        st.session_state['logged_in'] = False
        st.rerun()
