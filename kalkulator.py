import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inisialisasi simbol
x = sp.Symbol('x')

# Judul aplikasi
st.title("🧮 Kalkulator Integral & Turunan")
st.write("Aplikasi ini menghitung **turunan atau integral** dari fungsi aljabar yang dimasukkan.")

# Input fungsi dari user
fungsi_input = st.text_input("Masukkan fungsi aljabar (gunakan variabel x):", value="x**2 + 3*x")

# Pilihan operasi
operasi = st.radio("Pilih operasi:", ("Turunan", "Integral"))

# Tombol eksekusi
if st.button("Hitung"):

    try:
        # Parsing fungsi input
        fungsi = sp.sympify(fungsi_input)

        # Hitung turunan atau integral
        if operasi == "Turunan":
            hasil = sp.diff(fungsi, x)
            st.latex(f"f'(x) = {sp.latex(hasil)}")

        elif operasi == "Integral":
            hasil = sp.integrate(fungsi, x)
            st.latex(f"\\int f(x) dx = {sp.latex(hasil)} + C")

        # Evaluasi numerik (pada x=1)
        hasil_numerik = hasil.evalf(subs={x: 1})
        st.write(f"Hasil numerik (pada x=1): **{hasil_numerik}**")

        # Plot grafik
        st.subheader("📈 Grafik Fungsi dan Turunannya")

        # Konversi fungsi ke bentuk numerik
        fungsi_np = sp.lambdify(x, fungsi, modules=["numpy"])
        hasil_np = sp.lambdify(x, hasil, modules=["numpy"])

        # Sumbu x
        x_vals = np.linspace(-10, 10, 400)
        y_fungsi = fungsi_np(x_vals)
        y_hasil = hasil_np(x_vals)

        # Plot
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_fungsi, label="Fungsi Asli", color='blue')
        ax.plot(x_vals, y_hasil, label=operasi, color='red')
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
