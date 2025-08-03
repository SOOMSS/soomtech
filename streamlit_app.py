import streamlit as st
from openai import OpenAI

# 페이지 설정
st.set_page_config(
    page_title="SOOMTECH Minecraft EDU",
    page_icon="🖥️",
    layout="wide"
)

# 🔑 API 키 입력
st.sidebar.markdown("## 🔐 OpenAI API Key")
api_key = st.sidebar.text_input("API 키를 입력하세요", type="password")
if api_key:
    st.sidebar.success("✅ 올바른 API 키가 입력되었습니다.")
else:
    st.sidebar.info("👆 위 칸에 OpenAI API 키를 입력하세요.")

# OpenAI 클라이언트
client = OpenAI(api_key=api_key) if api_key else None

# 스타일
st.markdown("""
<style>
    .menu-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border: 3px solid #fbbf24;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .menu-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .menu-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .main-header {
        position: relative;
        color: white;
        text-align: center;
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 2rem;
        height: 250px;
    }
    .main-header::before {
        content: "";
        background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
                    url("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20130329_299%2Fkgk3377_13645414165827r1hD_PNG%2F2013-03-28_20.00.52.png&type=l340_165");
        background-size: cover;
        background-position: center;
        position: absolute;
        top:0; left:0; right:0; bottom:0;
        z-index: 0;
    }
    .main-header-content {
        position: relative;
        z-index: 1;
        background-color: rgba(0, 0, 0, 0.6);
        display: inline-block;
        padding: 1rem 2rem;
        border-radius: 10px;
        margin-top: 50px;
    }
    
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown("""
<div class="main-header">
    <div class="main-header-content">
        <h1>📘 마인크래프트 건축 수업</h1>
        <p>도면을 보고 상상하고, 설계하고, 구현하기</p>
    </div>
</div>
""", unsafe_allow_html=True)

# 메뉴 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "홈"

# 사이드바 메뉴
menu_map = {
    "홈": "🏠 홈",
    "정투상법": "🧱 정투상법",
    "일반모드": "🏙️ 일반모드",
    "설계사무실": "🏛️ 설계사무실",
    "블록코딩": "💻 블록코딩"
}
menu_choice = st.sidebar.selectbox("🎮 학습 모드 선택", list(menu_map.keys()))
st.session_state.page = menu_choice


# 📌 홈 페이지
if st.session_state.page == "홈":
    st.markdown("### 📖 수업 소개")
    st.markdown("중학교 2학년 기술 수업을 위한 창의적 웹앱입니다. 도면 읽기부터 3D 건축 설계까지 활동을 통해 **공간지각능력**과 **창의성**을 기릅니다.")

    st.markdown("## 🎯 수업 목표 및 활동")
    st.markdown("""
    <div style="background:#fff3cd; padding:1rem; border-radius:10px;">
        <p>1. 도면(정면도, 평면도, 우측면도 등)을 기반으로 입체 구조를 시각적으로 유추할 수 있다.</p>
        <p>2. 선택한 국가와 도시의 건축양식, 기후, 랜드마크의 정보를 분석하여 설계에 반영할 수 있다.</p>
        <p>3. 자신만의 설계를 Minecraft EDU를 활용하여 건축할 수 있다.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("## 🎮 학습 모드 선택")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">📐</div>
        <h3>정투상법</h3>
        <p>도면 기반 입체도형 추론</p>
    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">🗺️</div>
        <h3>일반모드</h3>
        <p>국가/도시별 건축 정보</p>
    </div>
    """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">🏛️</div>
        <h3>설계사무실</h3>
        <p>가상 건축 설계</p>
    </div>
    """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">💻</div>
        <h3>블록코딩</h3>
        <p>Minecraft 연동 코딩</p>
    </div>
    """, unsafe_allow_html=True)


# 각 페이지
elif st.session_state.page == "정투상법":
    st.subheader("🧱 정투상법 퀴즈")
    st.image("https://github.com/SOOMSS/minecraft_picture/blob/main/IMG_8942.jpg?raw=true", caption="정면도 예시", width=300)

elif st.session_state.page == "일반모드":
    st.subheader("🏙️ 일반모드: 도시 정보 탐색")
    country = st.selectbox("국가 선택", ["일본", "프랑스", "이탈리아", "미국"])
    city = st.text_input("도시를 입력하세요 (예: 교토, 파리, 로마)")
    if st.button("도시 정보 생성"):
        if not client:
            st.error("⚠️ API 키가 입력되지 않았습니다.")
        else:
            with st.spinner("도시 정보를 불러오는 중..."):
                prompt = f"""
                너는 건축 전문가야. 학생들에게 설명해주듯이 친절하고 간결하게 설명해줘.
                국가: {country}
                도시: {city}
                다음 항목을 한국어로 알려줘:
                1. 건축양식 특징
                2. 기후 특징
                3. 유명한 건축 랜드마크
                """
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                st.markdown("#### 📋 결과:")
                st.markdown(response.choices[0].message.content)

elif st.session_state.page == "설계사무실":
    st.subheader("🏛️ 설계사무실")
    st.markdown("건축 블록을 조합하여 나만의 가상 건축을 설계해보세요. WebSim 연동은 향후 구현 예정입니다.")
    st.image("https://github.com/SOOMSS/minecraft_picture/blob/main/IMG_8950.jpg?raw=true", width=400)

elif st.session_state.page == "블록코딩":
    st.subheader("💻 블록코딩")
    st.markdown("MakeCode를 활용하여 Minecraft에서 작동하는 건축 코드 생성기를 개발 중입니다.")
    st.code("""
player.onChat("tower", function () {
    blocks.fill(
        BLOCKS.STONE,
        pos(3, 0, 3),
        pos(3, 10, 3)
    )
})
    """, language="typescript")
