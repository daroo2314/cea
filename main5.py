# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
#st.balloons()
st.title('CEA Translation assistan')

content = st.text_input('Please enter a word or sentence.-in Korean or English-')
st.text('**If the desired answer is not provided or different, please press the "Translate for me" button again.^^')
# result = chat_model.predict(content + "국악가사를 써줘")
# print(result)

if st.button("Translate for me."):
   with st.spinner('Translating...'):
      result = chat_model.predict(content+'를 영어 또는 한글로 자동 번역해줘')
      st.write(result) 
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx5SPWmg_F0A4K4TgQbBzVp2-dkZsQvz5IQA&usqp=CAU')
st.text('컬럼비아 잉글리쉬 아카데이')
st.text('상담: 010.2300.1430')