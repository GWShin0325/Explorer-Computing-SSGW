import streamlit as st
import requests
from bs4 import BeautifulSoup
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import time
from matplotlib import rc, font_manager


font_path = "C:/Windows/Fonts/malgun.ttf"  
try:
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)
except Exception as e:
    rc('font', family='sans-serif')

st.title("멜론 차트 TOP 100 가수 트렌드 분석")
search = st.button("차트 분석 시작")

if search:
    st.write(f"멜론 차트 데이터를 수집 중...")

    url = "https://www.melon.com/chart/index.htm"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # HTTP 오류가 발생하면 예외 발생
        time.sleep(1) 

        soup = BeautifulSoup(response.text, "html.parser")

        artist_links = soup.find_all('a', href=re.compile("javascript:melon.link.goArtistDetail"))

        artists = [link.text.strip() for link in artist_links] 

        titles = artists

        st.write(f"총 {len(titles)}개의 가수 정보를 찾았습니다. (중복 포함)")

        if titles:
            st.subheader("추출된 가수 목록 (일부)")
            st.write(titles[:10])

            counter = Counter(titles) 
            most_common = dict(counter.most_common(20)) 

            words_list = list(most_common.keys())  
            counts_list = list(most_common.values()) 

            fig_bar, ax = plt.subplots(figsize=(10, 6))

            top_10_words = words_list[:10][::-1]
            top_10_counts = counts_list[:10][::-1]

            ax.barh(top_10_words, top_10_counts, color='skyblue')
            ax.set_title("차트 Top 100 내 최다 곡 보유 가수", fontsize=16)
            ax.set_xlabel("보유 곡 수 (빈도)", fontsize=12)
            st.pyplot(fig_bar)

            wc = WordCloud(
                width=800, 
                height=400, 
                font_path=font_path, 
                background_color="white")

            wc.generate_from_frequencies(most_common)

            fig_wc, ax = plt.subplots(figsize=(10,5))
            ax.imshow(wc, interpolation='bilinear')
            ax.set_title("가수별 영향력 워드 클라우드", fontsize=16)
            ax.axis("off")
            st.pyplot(fig_wc)

        else:
            st.write("가수 정보를 찾지 못했습니다. 멜론 차트 구조가 변경되었을 수 있습니다.")

    except requests.exceptions.RequestException as e:
        st.error(f"크롤링 중 오류 발생: {e}")
        st.info("인터넷 연결 상태나 멜론 서버 상태를 확인해주세요.")
