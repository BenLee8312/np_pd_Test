import numpy as np
import pandas as pd
import streamlit as st

st.title("測試套件")
a= np.array([89,71,69,77,63,85,92])
b=st.number_input("請輸入成績: ",0,100,key="num_b")  #key像是在幫變數取名稱

if st.button("輸入完成"):
    a= np.append(a,b) #右邊會先執行，執行完輸入回a
    st.write(a)
