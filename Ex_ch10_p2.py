import streamlit as st
import pandas as pd
import numpy as np

data = {"요일": ["월", "화", "수", "목", "금"], "1교시": ["산림치유복지학", None , None, "명상과수행", "컴퓨팅탐색"], "2교시": ["탁구초급", None, None, '산림평가학', None], "3교시": ['체력단련', None, None, None, None]}
list_data = [["컴퓨팅기초", 19], ["컴퓨팅탐색", 1], ["컴퓨팅핵심", 4]]
df = pd.DataFrame(data)

st.title("나의 수업 시간표")
st.header("정적 시간표(st.table)")
st.table(df)

json_data = {
    "산림치유복지학":{
        "교수": "한희",
        "강의실": "200동"
    },
    "명상과수행":{
        "교수": "성해영",
        "강의실": "43-1동"
    },
    "컴퓨팅탐색":{
        "교수": "변해선",
        "강의실": "26동"
    },
    "탁구초급":{
        "교수": "권준우",
        "강의실": "71동"
    },
    "산림평가학":{
        "교수": "한희",
        "강의실": "200동"
    },
    "체력단련":{
        "교수": "김정준",
        "강의실": "71동"
    } }
st.write("### 수업 정보")
st.json(json_data)

#지표(숫자+증감률) 표시 
st.write("## 이번 학기 요약")
col1, col2 = st.columns(2)
col1.metric(label = "수강과목수", value = "6")
col2.metric(label = "총 학점", value = "14", delta = "-4")
