#NO1
import pandas as pd  
pd.set_option('display.max_rows',None)
data = pd.read_csv('ds.csv')
print(data)

#NO2
tahun_tertentu = 2020  # Ganti dengan tahun yang diinginkan
total_sampah = 0

# Iterasi untuk menjumlahkan produksi sampah di tahun tertentu
for index, row in data.iterrows():
    if row['tahun'] == tahun_tertentu:
        total_sampah += row['jumlah_produksi_sampah']

print(f"Total produksi sampah pada tahun {tahun_tertentu}: {total_sampah} ton")

#no3
total_per_tahun = {}

for index, row in data.iterrows():
    tahun = row['tahun']
    total_per_tahun[tahun] = total_per_tahun.get(tahun, 0) + row['jumlah_produksi_sampah']

print("Total produksi sampah per tahun:", total_per_tahun)

#no4
total_per_kota_tahun = {}

for index, row in data.iterrows():
    key = (row['nama_kabupaten_kota'], row['tahun'])
    total_per_kota_tahun[key] = total_per_kota_tahun.get(key, 0) + row['jumlah_produksi_sampah']

for key, value in total_per_kota_tahun.items():
    print(f"Kota: {key[0]}, Tahun: {key[1]}, Total Sampah: {value} ton")
