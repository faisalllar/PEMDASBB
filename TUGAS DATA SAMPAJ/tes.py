#NO1
import pandas as pd  
pd.set_option('display.max_rows',None)
data = pd.read_csv('ds.csv')
print(data)

#no2
tahun_tertentu = 2020
data_tahun_tertentu = data[data['tahun'] == tahun_tertentu]
total_sampah = data_tahun_tertentu['jumlah_produksi_sampah'].sum()
print(f"Total produksi sampah di Jawa Barat pada tahun {tahun_tertentu} adalah {total_sampah} ton.")

#NO3
print(data.columns)

#NO 4
for column in data.columns:
    print(f"Kolom: {column}")
    print(data[column])
    print("-" * 30)

