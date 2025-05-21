import streamlit as st

st.title("🎈LooOve♥️")
st.write("ayo olahraga bersama !"
        )
st.image("1747010510672.jpg", width=200)
st.title("apklikasi sederhana")
st.header("apklikasi mengecek nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", volue=0, step=1)

if (angka % 2) == 0:
        st.write(f"{angka} adalah Bilangan Genap")
else:
        st.write(f"{angka} adalah Bilangan Ganjil")
        
