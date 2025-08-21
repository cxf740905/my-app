import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="学生成绩分析系统", layout="wide")

st.title("📊 学生成绩自动分析可视化系统")

uploaded_file = st.file_uploader("📁 上传学生成绩 CSV 文件", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ 文件上传成功！")
    
    st.subheader("🔍 数据预览")
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if numeric_cols:
        st.subheader("📈 成绩分布图")
        selected_col = st.selectbox("选择科目", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col], kde=True, bins=10, ax=ax)
        ax.set_title(f"{selected_col} 分布图")
        st.pyplot(fig)

        st.subheader("📉 成绩趋势图")
        if "姓名" in df.columns or "学号" in df.columns:
            id_col = "姓名" if "姓名" in df.columns else "学号"
            fig, ax = plt.subplots()
            sns.lineplot(x=df[id_col], y=df[selected_col], marker="o", ax=ax)
            ax.set_title(f"{selected_col} 成绩趋势")
            plt.xticks(rotation=45)
            st.pyplot(fig)
    else:
        st.warning("⚠️ 没有可视化的数值型成绩列。")
else:
    st.info("请上传一个包含学生成绩的 CSV 文件。")
