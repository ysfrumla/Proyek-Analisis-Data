import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import datetime as dt

df_all_data = pd.read_csv('all_data.csv')

# Mengubah tipe data kolom datetime
datetime_col = ["order_approved_at"]
for column in datetime_col:
    df_all_data[column] = pd.to_datetime(df_all_data[column])

# Fungsi untuk menghitung jumlah pesanan per bulan
def monthly_orders_df(df):
    monthly_orders = df.resample(rule='M', on='order_approved_at').agg({
        "order_id": "size",
    })
    monthly_orders.index = monthly_orders.index.strftime('%B')
    monthly_orders = monthly_orders.reset_index()
    monthly_orders.rename(columns={"order_id": "order_count"}, inplace=True)
    monthly_orders = monthly_orders.sort_values('order_count').drop_duplicates('order_approved_at', keep='last')
    return monthly_orders

# Fungsi untuk menghitung total pengeluaran pelanggan per bulan
def monthly_spend_df(df):
    monthly_spend = df.resample(rule='M', on='order_approved_at').agg({
        "price": "sum"
    })
    monthly_spend = monthly_spend.reset_index()
    monthly_spend.rename(columns={"price": "Total Spending"}, inplace=True)
    monthly_spend['order_approved_at'] = monthly_spend['order_approved_at'].dt.strftime('%B')
    monthly_spend = monthly_spend.sort_values('Total Spending').drop_duplicates('order_approved_at', keep='last')
    return monthly_spend

# Fungsi untuk menampilkan produk dengan penjualan tertinggi dan terendah
def top_and_least_products_df(df):
    product_id_counts = df.groupby('product_category_name_english')['product_id'].count().reset_index()
    sorted_df = product_id_counts.sort_values(by='product_id', ascending=False)
    return sorted_df

# Fungsi untuk menampilkan rating pelanggan terhadap layanan
def customers_rating_df(df):
    rating_service = df['review_score'].value_counts().sort_values(ascending=False)
    max_score = rating_service.idxmax()
    return rating_service, max_score, df['review_score']

with st.sidebar:
    # Menampilkan informasi mengenai dataset
    st.write('E-Commerce Public Dataset')

st.header('E-Commerce Public Dataset')

st.subheader('Monthly Orders')
daily_orders_df = monthly_orders_df(df_all_data)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_orders_df["order_approved_at"],
    daily_orders_df["order_count"],
    marker='o',
    linewidth=2,
    color="#90CAF9",
)
plt.xticks(rotation=45)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.subheader('Total Customer Expenditure')
monthly_spend_df = monthly_spend_df(df_all_data)
plt.figure(figsize=(16, 8))
sns.barplot(
    x='order_approved_at',
    y='Total Spending',
    data=monthly_spend_df,
    linestyle='-',
    color="#90CAF9",
)
plt.xlabel('')
plt.ylabel('Total Spending')
plt.xticks(fontsize=10, rotation=25)
plt.yticks(fontsize=10)
plt.legend()
st.pyplot(plt)

st.subheader("Top And Least Product")
top_and_least_products_df = top_and_least_products_df(df_all_data)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
sns.barplot(
    x="product_id", 
    y="product_category_name_english", 
    data=top_and_least_products_df.head(5), 
    palette=["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"], 
    ax=ax[0],
)
ax[0].set_ylabel('')
ax[0].set_xlabel('')
ax[0].set_title("Top Selling Products", loc="center", fontsize=18)
ax[0].tick_params(axis ='y', labelsize=15)

sns.barplot(
    x="product_id", 
    y="product_category_name_english", 
    data=top_and_least_products_df.sort_values(by="product_id", ascending=True).head(5), 
    palette=["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"], 
    ax=ax[1],
)
ax[1].set_ylabel('')
ax[1].set_xlabel('')
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Least Selling Products", loc="center", fontsize=18)
ax[1].tick_params(axis='y', labelsize=15)

plt.suptitle("Top and least sold products", fontsize=20)
st.pyplot(fig)