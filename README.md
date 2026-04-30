📊 Sales Data Analysis Project

This repository contains my first end-to-end Data Analyst project using:

Microsoft Excel
MySQL
Python (Pandas & Matplotlib)

Project ini mensimulasikan analisis data penjualan sederhana dari proses data → SQL → Python → Visualisasi.

📁 Project Structure
File	Description
analisis_penjualan.xlsx	Raw dataset & Excel analysis
sql_analysis.sql	SQL queries for data analysis
analysis_python.py	Python script for analysis & visualization
🧾 Dataset Information

Dataset berisi data penjualan sederhana:

Tanggal
Produk
Kota
Jumlah
Harga
Total Penjualan
📌 Excel Analysis

Analisis yang dilakukan di Excel:

Total Penjualan → =Jumlah * Harga
Total Revenue → =SUM(Total)
Average Sales → =AVERAGE(Total)
Pivot Table Dashboard
Sales Chart Visualization
🗄️ SQL Analysis

Analisis menggunakan MySQL:

SELECT & WHERE filtering
GROUP BY & HAVING
JOIN antar tabel
Window Functions (RANK, ROW_NUMBER)
Pivot Table SQL
Subquery & CTE

Contoh query:

SELECT produk, SUM(total) AS total_penjualan
FROM penjualan
GROUP BY produk;
🐍 Python Analysis

Python digunakan untuk:

Mengambil data dari MySQL
Analisis menggunakan Pandas
Visualisasi grafik dengan Matplotlib

Contoh:

df.groupby("produk")["total"].sum()
🎯 Project Goal

Tujuan project ini:

Melatih skill Data Analyst end-to-end
Menggabungkan Excel + SQL + Python
Membuat portfolio pertama
👨‍💻 Author

First Data Analyst Portfolio Project 🚀
