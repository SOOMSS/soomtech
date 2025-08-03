import streamlit as st
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

from openai import OpenAI
client = OpenAI(api_key=api_key) if api_key else None

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

# ----------------------------- 홈 -----------------------------
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

# ----------------------------- 정투상법 -----------------------------
elif st.session_state.page == "정투상법":
    st.subheader("🧱 정투상법 퀴즈")
    st.image("https://github.com/SOOMSS/minecraft_picture/blob/main/IMG_8942.jpg?raw=true", caption="정면도 예시", width=300)

# ----------------------------- 일반모드 -----------------------------
elif st.session_state.page == "일반모드":
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
                이 내용을 바탕으로 minecraft education에서 어떤 건축물을 지으면 좋을지 자세하게 추천해줘
                """
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                st.markdown("#### 📋 결과:")
                st.markdown(response.choices[0].message.content)

# ----------------------------- 설계사무실 -----------------------------
elif st.session_state.page == "설계사무실":
    st.subheader("🏛️ 설계사무실")
    st.markdown("WebSim을 활용하여 가상 건축 설계를 하고, 설계 결과를 저장하고 시각화해보세요.")

    # WebSim 삽입
    websim_url = "https://websim.com/p/pmyqwk48eamjoydzrr0t"
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

        # 시각화
        st.markdown("### 📊 재료 사용 분포")
        material_counts = df['재료'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(material_counts, labels=material_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

# ----------------------------- 블록코딩 -----------------------------
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
