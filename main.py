import pandas
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    一氧化碳能够吸收地球表面释放的长波红外辐射，因此符合温室气体的定义。然而，其浓度在大气
    中极低（通常不超过0.01%），直接吸收的热量有限，因此对全球变暖的直接影响微弱。\n
    一氧化碳在严格定义上属于温室气体，但其对全球变暖的直接贡献有限，更多是通过影响其他
    温室气体的循环间接发挥作用。当前气候变化应对措施仍以减排二氧化碳、甲烷等气体为核心，
    但CO的间接效应仍需在大气化学模型中纳入考量。
    """
    st.info(content)

content2 = """
CO的温室气体属性。一氧化碳能够吸收地球表面释放的长波红外辐射，因此符合温室气体的定义。
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])