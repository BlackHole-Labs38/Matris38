import streamlit as st
import random

# Sayfa Genişliği ve Başlık
st.set_page_config(page_title="9. Sınıf Mat Web", page_icon="📝")

st.title("📐 9. Sınıf Matematik Portalı")
st.subheader("MEB Müfredatı ile Tam Uyumlu")

# Sol Menü (Navigasyon)
menu = st.sidebar.radio("Gitmek İstediğin Yer:", ["Konu Anlatımı", "Soru Çöz", "Başarı Tablom"])

if menu == "Konu Anlatımı":
    konu = st.selectbox("Bir Konu Seç:", ["Mantık", "Kümeler", "Denklemler", "Üçgenler"])
    
    if konu == "Mantık":
        st.write("### 🧠 Mantık (Önermeler)")
        st.write("Doğruluk değeri 1 (Doğru) veya 0 (Yanlış) olan ifadelere denir.")
        st.latex(r"p \land q \text{ (Ve), } p \lor q \text{ (Veya)}")
        st.info("İpucu: 'Ve' bağlacında sonucun 1 olması için ikisinin de 1 olması gerekir.")
        
    elif konu == "Kümeler":
        st.write("### 🎯 Kümeler")
        st.write("Nesneler topluluğudur. Eleman sayısı $s(A)$ ile gösterilir.")
        st.latex(r"A \cup B \text{ (Birleşim), } A \cap B \text{ (Kesişim)}")
        
    # Diğer konuları buraya ekleyebiliriz...

elif menu == "Soru Çöz":
    st.write("### ✍️ Test Vakti")
    zorluk = st.select_slider("Zorluk:", options=["Kolay", "Orta", "Sınav Tadında"])
    
    # Basit bir soru mantığı
    s1 = random.randint(10, 50)
    s2 = random.randint(5, 15)
    
    st.write(f"**Soru:** $x + {s2} = {s1}$ ise $x$ kaçtır?")
    cevap = st.number_input("Cevabın:", step=1)
    
    if st.button("Cevabı Kontrol Et"):
        if cevap == (s1 - s2):
            st.success("Doğru! MEB sınavında olsa kesin yapardın. 🔥")
            st.balloons()
        else:
            st.error(f"Hadi be kanka! Doğru cevap {s1-s2} olmalıydı.")

elif menu == "Başarı Tablom":
    st.write("### 🏆 Gelişimin")
    st.progress(40) # Örnek ilerleme
    st.write("Şu ana kadar Mantık konusunu %100 tamamladın!")

st.sidebar.markdown("---")
st.sidebar.write("Yapımcı: **Kerem**")
