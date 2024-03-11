# Proyek-Analisis-Data
Repositori ini adalah hasil dari proyek analis data yang dibuat dengan Streamlit. Tujuannya adalah untuk melakukan analisis data terhadap E-Commerce Public Dataset yang divisualisasikan di cloud melalui sebuah website.Tujuan utamanya adalah untuk memberikan pemahaman dan pemahaman tentang data.
# Sumber Data dan Instalasi Environment
E-Commerce Public Dataset ([Sumber](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce))
```
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit
```
# Struktur Direktori
- `/E-Commerce Public Dataset`: Beriki kumpulan dataset yang di download melalui [sumber](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) untuk di analisis.
- `all_data.csv`: Merupakan seluruh kumpulan data yang sudah digabungkan menjadi 1 file utuh yang siap untuk di visualisasikan dengan `streamlit`.
- `Proyek Analisis Data.ipynb`: File yang digunakan untuk melakukan analisis data.
- `dashboard.py`: File python untuk melakukan visualisasi dengan `streamlit`.
- `requirements.txt`: Kumpulan library/module yang dipakai dalam melakukan analisis dan visualisasi data.
- `README.md`: Markdown file.
# Run Streamlit App
Mengakses dan kompilasi secara local:
```
streamlit run dashboard.py
```
