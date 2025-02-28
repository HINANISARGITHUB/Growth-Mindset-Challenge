#streamlit
import streamlit as st

st.set_page_config(page_title = "Growth Mindset Project", page_icon="✨")
st.title("Growth Mindset AI Project")

st.header("🏆Welcome to your growth journey!")
st.write("""
Welcome to the Growth Mindset Challenge!  
This challenge is designed to help you develop a positive mindset, embrace challenges, and learn from feedback.  
Let's embark on this journey of growth and self-improvement together!""")

#quote section
st.header("Welcome to today,s Growth Mindset Quote")
st.write(" “Nations are born in the hearts of poets, they prosper and die in the hands of politicians.”― Allama Iqbal")

st.header("🧠 Today Challange?")
user_input = st.text_input("Which challenge you are facing:")

#condition

if user_input:
    st.success(f"😢 You are facing: {user_input}. Keep pushing forward towards your goal!")

else:
   st.warning("Tell us about your challenge to get atarted!")

#reflexing
st.header(" Reflect on your learning")
reflection = st.text_area("write your reflection here")

if reflection:
    st.success(f"✨Great insight! your reflection: {reflection}")

else:
    st.info("Reflection on past experience help you grow! Share your experience")


#acheivement
st.header("🏆Celebrate your Sucess!") 
acheivement = st.text_input("Share something you have recently accomplished:")  

if acheivement:
    st.success(f"🎉Amazing! you acheived: {acheivement}")

else:
    st.info("Biger or small, every acheivement counts! Share one now! 🙂") 

#footer
st.write("- - -")  
st.write("Keep believing in yourself. Growth is a journey, not a destination! ⭐")   

st.write("**©️ Created by Hina Nisar**")

   

