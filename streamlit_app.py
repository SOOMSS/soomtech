import streamlit as st
from openai import OpenAI
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt

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
    "Minecraft Education": "🧱 Minecraft Education",
    "검색모드": "🏙️ 검색모드",
    "설계사무실": "🏛️ 설계사무실",
    "블록코딩": "💻 블록코딩"
}
menu_choice = st.sidebar.selectbox("🎮 학습 모드 선택", list(menu_map.keys()))
st.session_state.page = menu_choice

# 사이드바 만든이 소개
with st.sidebar:
    st.markdown("---")
    st.markdown("""
    💡 “미래 교육은 연결과 협업에서 시작됩니다.”

    👤 **성사중학교 김수민**

    📌 AI 융합교육 / 메이커 수업 / 피지컬 컴퓨팅 연구  
    📌 Arduino, 센서, 코딩 기반 프로젝트형 수업 다수 운영  
    📌 교무업무 자동화와 온라인 협업 시스템(디지털 교무실) 구축 실천 중  

    🎯 *“학생과 교사가 모두 성장하는, 똑똑한 학교 만들기”*를 지향합니다.
    """)


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
        <h3>Minecraft Education</h3>
        <p>작동법 익히기</p>
    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">🗺️</div>
        <h3>검색모드</h3>
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
        <p>Minecraft 좌표 코딩</p>
    </div>
    """, unsafe_allow_html=True)


elif st.session_state.page == "Minecraft Education":
    st.subheader("🧱 Minecraft Education: 정면/평면 설계 실습")
    st.markdown("아래 WebSim 시뮬레이터에서 도면을 기반으로 블록을 조합하여 건축 설계를 해보세요.")

    # WebSim URL 삽입
    websim_url = "https://websim.com/@JiQuad/eaglercraft-minecraft"  # 실제 프로젝트 주소로 대체
    import streamlit.components.v1 as components
    components.iframe(websim_url, height=650, width=1050, scrolling=True)

    # 사용자 설계 요약 입력
    st.markdown("### 📝 설계 설명 작성")
    summary = st.text_area("설계의 의도, 사용 블록, 층수 등을 자유롭게 설명해보세요.")

    if st.button("설계 요약 저장"):
        if "edu_design_notes" not in st.session_state:
            st.session_state.edu_design_notes = []
        st.session_state.edu_design_notes.append(summary)
        st.success("📝 설계 설명이 저장되었습니다!")

    if st.session_state.get("edu_design_notes"):
        st.markdown("### 📂 저장된 설계 설명 목록")
        for i, note in enumerate(st.session_state.edu_design_notes[::-1], 1):
            st.markdown(f"**{i}.** {note}")


elif st.session_state.page == "검색모드":
    st.markdown("### 🌏 주요 국가별 건축양식 요약")
    with st.expander("🔍 클릭하여 대표 건축양식과 랜드마크 정보를 확인하세요"):
        col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🇯🇵 일본")
        st.markdown("""
        - **양식**: 전통 목조건축, 기와지붕, 미니멀리즘
        - **랜드마크**: 기요미즈데라, 금각사
        - **특징**: 자연과의 조화를 중시하며, 단순하고 조용한 느낌을 강조
        """)

        st.markdown("#### 🇫🇷 프랑스")
        st.markdown("""
        - **양식**: 고딕, 르네상스, 바로크, 현대 유리건축
        - **랜드마크**: 에펠탑, 루브르박물관
        - **특징**: 장식적인 디테일과 예술성이 돋보임
        """)

    with col2:
        st.markdown("#### 🇮🇹 이탈리아")
        st.markdown("""
        - **양식**: 로마네스크, 르네상스, 바로크
        - **랜드마크**: 콜로세움, 두오모 성당
        - **특징**: 고대 로마 유산과 화려한 돔 구조가 강점
        """)

        st.markdown("#### 🇺🇸 미국")
        st.markdown("""
        - **양식**: 현대 건축, 마천루, 산업적 기능주의
        - **랜드마크**: 엠파이어 스테이트 빌딩, 백악관
        - **특징**: 대규모 구조와 첨단 기술 중심
        """)

    st.subheader("🏙️ 일반모드: 도시 정보 탐색")
    name = st.text_input("이름을 적어주세요.(별명도 좋아요)")
    country = st.selectbox("국가 선택", ["일본", "프랑스", "이탈리아", "미국"])
    city = st.text_input("도시를 입력하세요 (예: 교토, 파리, 로마)")
    if st.button("도시 정보 생성"):
        if not client:
            st.error("⚠️ API 키가 입력되지 않았습니다.")
        else:
            with st.spinner("작성한 내용을 토대로 도시의 정보를 불러오는 중..."):
                prompt = f"""
                너는 건축 전문가야. 학생들에게 설명해주듯이 친절하고 간결하게 설명해줘.
                국가: {country}
                도시: {city}
                다음 항목을 한국어로 알려줘:
                1. 건축양식 특징
                2. 기후 특징
                3. 유명한 건축 랜드마크
                알려줄때는 이름 : {name}님 작성한 내용을 토대로 알려드리겠습니다. 라고 한 뒤에 알려줘.
                이 내용을 바탕으로 minecraft education에서 어떤 건축물을 지으면 좋을지 자세하게 추천해줘.
                또한, 해당 건축물과 관련있는 유튜브 영상을 링크로 추천해줘
                """
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                st.markdown("#### 📋 결과:")
                st.markdown(response.choices[0].message.content)


    import streamlit.components.v1 as components

elif st.session_state.page == "설계사무실":
    st.subheader("🏛️ 설계사무실")
    st.markdown("WebSim을 활용하여 가상 건축 설계를 하고, 설계 결과를 저장하고 시각화해보세요.")

    websim_url = "https://websim.com/p/pmyqwk48eamjoydzrr0t/5"
    components.iframe(src=websim_url, height=1000, width=1500, scrolling=True)

    st.markdown("---")
    st.markdown("### 📝 설계 결과 기록하기")

    if "design_data" not in st.session_state:
        st.session_state.design_data = []

    name = st.text_input("설계자 이름 또는 닉네임")
    structure_name = st.text_input("건축물 이름")
    material = st.selectbox("주요 재료", ["석재", "목재", "유리", "철근", "복합재료"])
    floors = st.slider("건물 층수", 1, 10, 3)
    notes = st.text_area("설계 특징 간단 메모")

    if st.button("설계 저장"):
        st.session_state.design_data.append({
            "설계자": name,
            "건축물": structure_name,
            "재료": material,
            "층수": floors,
            "설명": notes
        })
        st.success("✅ 설계 정보가 저장되었습니다.")

    if st.session_state.design_data:
        st.markdown("### 📋 설계 결과 목록")
        df = pd.DataFrame(st.session_state.design_data)
        st.dataframe(df, use_container_width=True)

        # 🔧 Minecraft 코드 자동 생성
        st.markdown("### 💻 Minecraft용 코드 자동 생성")
        latest_design = st.session_state.design_data[-1]

        # 재료 매핑
        block_map = {
            "석재": "STONE",
            "목재": "OAK_WOOD",
            "유리": "GLASS",
            "철근": "IRON_BLOCK",
            "복합재료": "BRICKS"
        }

        # 기본 코드 템플릿
        code = f"""
player.onChat("{latest_design['건축물'].lower()}", function () {{
    blocks.fill(
        BLOCKS.{block_map[latest_design['재료']]},
        pos(0, 0, 0),
        pos(4, {latest_design['층수'] * 3}, 4)
    )
}})
        """
        st.code(code, language="typescript")
        st.info(f"🧱 위 코드를 Minecraft Education의 MakeCode에 붙여넣으면 '{latest_design['건축물'].lower()}' 명령어로 {latest_design['건축물']}이 생성됩니다!")

# 블록코딩 페이지


elif st.session_state.page == "블록코딩":
    st.subheader("💻 블록코딩")
    st.markdown("Minecraft에서 자주 혼동되는 **절대좌표와 상대좌표**를 이해하고, 자동으로 계산해보세요!")

    # 📘 설명 영역
    with st.expander("📘 절대좌표와 상대좌표 개념 설명"):
        st.markdown("""
        - **절대좌표**는 마인크래프트 월드의 고정된 위치입니다. 예: `pos(10, 5, -3)`
        - **상대좌표**는 플레이어나 특정 블록을 기준으로 얼마나 떨어져 있는지를 나타냅니다. 예: `~3 ~1 ~-2`
        - `~`는 현재 위치 기준으로 좌표를 지정할 수 있게 해주며, 예를 들어 `~1`은 현재 위치에서 +1을 의미합니다.

        예: 플레이어 위치가 (5, 4, 7)이고 목표 위치가 (8, 6, 10)이라면 상대좌표는 `~3 ~2 ~3`입니다.
        """)

    # 🧮 입력
    st.header("🧮 좌표 입력 및 계산")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📍 현재 위치 (절대좌표)")
        cx = st.number_input("현재 X", value=0, key="cx")
        cy = st.number_input("현재 Y", value=0, key="cy")
        cz = st.number_input("현재 Z", value=0, key="cz")

    with col2:
        st.subheader("🎯 목표 위치 (절대좌표)")
        tx = st.number_input("목표 X", value=5, key="tx")
        ty = st.number_input("목표 Y", value=5, key="ty")
        tz = st.number_input("목표 Z", value=5, key="tz")

    # 상대좌표 계산
    dx, dy, dz = tx - cx, ty - cy, tz - cz

    st.markdown("### ✅ 계산된 상대좌표")
    st.code(f"~{dx} ~{dy} ~{dz}", language="text")

    # 명령어 예시 생성
    st.markdown("### 🧱 명령어 예시")
    chat_command = st.text_input("명령어 이름 입력 (예: move)", value="move")
    st.code(f"""
player.onChat("{chat_command}", function () {{
    player.move(~{dx}, ~{dy}, ~{dz})
}})
    """, language="typescript")

    # 📊 시각화
    st.header("📊 좌표 시각화 (3D)")
    import plotly.graph_objects as go
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(
        x=[cx], y=[cy], z=[cz],
        mode='markers+text',
        marker=dict(size=5, color='blue'),
        name='현재 위치',
        text=["현재 위치"], textposition="top center"
    ))
    fig.add_trace(go.Scatter3d(
        x=[tx], y=[ty], z=[tz],
        mode='markers+text',
        marker=dict(size=5, color='red'),
        name='목표 위치',
        text=["목표 위치"], textposition="top center"
    ))
    fig.add_trace(go.Scatter3d(
        x=[cx, tx], y=[cy, ty], z=[cz, tz],
        mode='lines', line=dict(color='green', width=4), name='이동 벡터'
    ))
    fig.update_layout(
        margin=dict(l=0, r=0, b=0, t=0),
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

    st.success("⬆️ 위 그래프에서 현재 위치와 목표 위치, 이동 방향을 3D로 확인할 수 있습니다!")

    # 🎁 추가 예시
    st.markdown("### 🔧 blocks.fill 예시")
    st.code("""
player.onChat("tower", function () {
    blocks.fill(
        BLOCKS.STONE,
        pos(3, 0, 3),
        pos(3, 10, 3)
    )
})
    """, language="typescript")
