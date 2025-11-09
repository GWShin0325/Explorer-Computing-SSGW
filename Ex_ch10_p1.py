import streamlit as st
import pandas as pd

# Markdown 문법을 지원하여 헤더, 볼드, 이탤릭, 하이퍼링크 등 다양한 텍스트 스타일 가능
st.markdown("# 나의 소개 페이지")
st.markdown("## 자기소개")
st.markdown("**안녕하세요, 제 이름은 신건우입니다.**")
st.markdown("**저는 자연환경과 야생동물에 관심이 있습니다.**")
st.markdown("## 좋아하는 것")
st.write("저는 여행을 매우 좋아합니다. 특히 멋있는 풍경과 잔잔한 분위기가 있는 곳을 좋아합니다.")

# write()함수는 다목적 함수로 텍스트, 마크다운, 데이터, 객체 등 다양한 요소를 자동으로 감지하여 인식함
st.markdown("## 앞으로의 목표")
st.write("앞으로 컴퓨터에 대한 이해와 함께 컴퓨터 활용 능력을 키우고 싶습니다.") 

st.caption("제가 좋아하는 파이썬 코드 예시")
st.code("for i in range(3): print('Thank you!')")
st.latex(r"ax^2 + bx + c = 0")
