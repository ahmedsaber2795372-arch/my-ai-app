import streamlit as st
import google.generativeai as genai

# هذا هو المحرك
genai.configure(api_key="AIzaSyCUJg61xCUaB2A4Nsfqf7HhilH0GSApgu8")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("تطبيقي الخاص 🤖")

# مكان الكتابة
user_input = st.text_input("اكتب سؤالك هنا:", placeholder="كيف حالك اليوم؟")

if st.button("إرسال"):
    if user_input:
        response = model.generate_content(user_input)
        st.info(response.text)
    else:
        st.warning("من فضلك اكتب سؤالاً أولاً!")