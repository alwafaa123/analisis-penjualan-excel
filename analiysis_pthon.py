# ===============================
# ANALISIS PENJUALAN DENGAN PYTHON
# ===============================

import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# koneksi ke MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="penjualan_db"
)

# ambil data dari MySQL
query = "SELECT * FROM penjualan"
df = pd.read_sql(query, conn)

print("Data berhasil diambil:")
print(df.head())

# ===============================
# ANALISIS
# ===============================

# total penjualan per produk
produk = df.groupby("produk")["total"].sum().reset_index()
print("\nTotal penjualan per produk:")
print(produk)

# ===============================
# VISUALISASI
# ===============================

plt.figure()
plt.bar(produk["produk"], produk["total"])
plt.title("Total Penjualan per Produk")
plt.xlabel("Produk")
plt.ylabel("Total Penjualan")
plt.show()