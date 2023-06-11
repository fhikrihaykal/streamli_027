import streamlit as st
import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    st.title("Kalkulator Statistika")

    with st.form('data'):
        data2 = st.number_input('banyak data (n)', min_value=1)
        submit_button = st.form_submit_button('kirim')

        st.write('Mencari Karakteristik Data')
        df = pd.DataFrame(columns=["Data"], index=range(1, int(data2) + 1), dtype=float)
        df_input = st.experimental_data_editor(df, use_container_width=True)
        df_output = st.form_submit_button('ok')

        if df_output:
            x_data = df_input["Data"].tolist()

            st.write("Jumlah Data:", len(x_data))
            st.write("Total:", sum(x_data))
            st.write("Rata-rata:", statistics.mean(x_data))
            st.write("Median:", statistics.median(x_data))
            st.write("Standar Deviasi:", statistics.stdev(x_data))
            st.write("Variansi:", statistics.variance(x_data))

            # Menampilkan Boxplot
            plt.boxplot(x_data)
            plt.title("Boxplot")
            plt.xlabel("Data")
            plt.ylabel("Nilai")
            st.pyplot()
        else:
            st.write("Kolom 'Data' tidak ditemukan. Harap masukkan data terlebih dahulu.")
            st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == '__main__':
    main()