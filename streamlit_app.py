import streamlit as st

st.title("🧁 Welcome 🧁")
st.write(
    "test website"
)
st.image("239e46c7a088b819d1b9ff9ecd7e5eff.jpg")

st.title("aplikasi sederhana")
st.header("aplikasi mengecek nilai genap/ganjil")
angka - st.number_input("tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
    st.write(f"{angka} adalah bilangan ganjil") 
