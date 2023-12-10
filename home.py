import streamlit as st



st.set_page_config(
    page_title="Portfolio | nihayah",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("me.jpg", width= 390)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : NIHAYATUL KHUSNA")
   st.caption("NIM : 0402201095")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 13 Januari 2002 
            - Alamat               : Brebes
            - Hobi                 : Membaca
            - Cita-cita            : Arsitek
            - Hal yang disukai     : Membaca Novel
            - Status               : Lajang
            """
        )
st.header("*Call Me If You Want*")
