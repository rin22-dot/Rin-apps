import streamlit as st

st.title("sigma 😝")


st.write("sIigmAaA")
st.image("9769a4cd94b663946f97ec66857f9d6f.jpg", width=200)

st.title("aplikasi sederhana")
st.header("aplikasi mengecek nilai genap/ganjil")
angka = st.number_input("tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
    st.write(f"{angka} adalah bilangan ganjil") 

age = st.slider("How old are you?", 0, 1000, 1)
st.write("I'm ", age, "years old")
