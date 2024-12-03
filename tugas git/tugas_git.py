#152023100_MuhammadFaisalA
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# 1. Menampilkan seluruh data
print("Seluruh data panen:")
for lokasi, info in data_panen.items():
    print(f"{info['nama_lokasi']}: {info['hasil_panen']}")

# 2. Jumlah hasil panen jagung dari lokasi2
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"\nJumlah hasil panen jagung dari lokasi2 (Kebun B): {jagung_lokasi2}")

# 3. Nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"\nNama lokasi dari lokasi3: {nama_lokasi3}")

# 4. Jumlah hasil panen padi dan kedelai ke dalam variabel
hasil_padi = {lokasi: info['hasil_panen']['padi'] for lokasi, info in data_panen.items()}
hasil_kedelai = {lokasi: info['hasil_panen']['kedelai'] for lokasi, info in data_panen.items()}

print("\nJumlah hasil panen padi per lokasi:")
print(hasil_padi)
print("\nJumlah hasil panen kedelai per lokasi:")
print(hasil_kedelai)

# 5. Percabangan untuk perhatian khusus
print("\nStatus setiap lokasi:")
for lokasi, info in data_panen.items():
    padi = info['hasil_panen']['padi']
    jagung = info['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{info['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{info['nama_lokasi']} dalam kondisi baik.")
