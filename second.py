import streamlit as st
import numpy as np
from scipy.stats import norm

# Membuat judul aplikasi
st.title('Tabel Distribusi Normal')

# Mengambil input dari pengguna
mean = st.number_input('Mean (μ)', value=0.0)
std_dev = st.number_input('Standard Deviation (σ)', value=1.0)
x_value = st.number_input('X Value', value=0.0)

# Menghitung z-score
z_score = (x_value - mean) / std_dev

# Menghitung nilai probabilitas menggunakan distribusi normal
probability = norm.cdf(z_score)

# Menampilkan hasil
st.subheader('Hasil')
st.write(f'Z-Score: {z_score:.4f}')
st.write(f'Probabilitas: {probability:.4f}')