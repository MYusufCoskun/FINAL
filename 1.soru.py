import pandas as pd

veriler = [
    ['PERSONEL', 'MAAS', 'DENEYİM', 'GÖREV', 'MEMNUN'],
    ['1', 'NORMAL', 'ORTA', 'UZMAN', 'EVET'],
    ['2', 'YÜKSEK', 'YOK', 'UZMAN', 'EVET'],
    ['3', 'DÜŞÜK', 'YOK', 'YÖNETİCİ', 'EVET'],
    ['4', 'YÜKSEK', 'ORTA', 'YÖNETİCİ', 'EVET'],
    ['5', 'DÜŞÜK', 'ORTA', 'YÖNETİCİ', 'EVET'],
    ['6', 'YÜKSEK', 'İYİ', 'YÖNETİCİ', 'EVET'],
    ['7', 'DÜŞÜK', 'İYİ', 'YÖNETİCİ', 'EVET'],
    ['8', 'YÜKSEK', 'ORTA', 'UZMAN', 'HAYIR'],
    ['9', 'DÜŞÜK', 'ORTA', 'UZMAN', 'HAYIR'],
    ['10', 'YÜKSEK', 'İYİ', 'UZMAN', 'HAYIR'],
    ['11', 'DÜŞÜK', 'İYİ', 'UZMAN', 'HAYIR']
]

df = pd.DataFrame(veriler[1:], columns=veriler[0])
# DataFrame'i ekrana yazdırma 1.soru A)
print(df.to_string(index=False))

sol_sayilar = []
sag_sayilar = []

bolum = 1  # İlk bölünme numarası

# Sol taraftaki koşullara göre örnek sayılarını hesapla
sol_sayilar.append(len(df[df['MAAS'] == 'NORMAL']))
sol_sayilar.append(len(df[df['MAAS'] == 'YÜKSEK']))
sol_sayilar.append(len(df[df['MAAS'] == 'DÜŞÜK']))
sol_sayilar.append(len(df[df['DENEYİM'] == 'YOK']))
sol_sayilar.append(len(df[df['DENEYİM'] == 'ORTA']))
sol_sayilar.append(len(df[df['DENEYİM'] == 'İYİ']))
sol_sayilar.append(len(df[df['GÖREV'] == 'UZMAN']))
sol_sayilar.append(len(df[df['GÖREV'] == 'YÖNETİCİ']))

# Sağ taraftaki koşullara göre örnek sayılarını hesapla
sag_sayilar.append(len(df[df['MAAS'].isin(['DÜŞÜK', 'YÜKSEK'])]))
sag_sayilar.append(len(df[df['MAAS'].isin(['DÜŞÜK', 'NORMAL'])]))
sag_sayilar.append(len(df[df['MAAS'].isin(['NORMAL', 'YÜKSEK'])]))
sag_sayilar.append(len(df[df['DENEYİM'].isin(['ORTA', 'İYİ'])]))
sag_sayilar.append(len(df[df['DENEYİM'].isin(['YOK', 'İYİ'])]))
sag_sayilar.append(len(df[df['DENEYİM'].isin(['YOK', 'ORTA'])]))
sag_sayilar.append(len(df[df['GÖREV'].isin(['UZMAN', 'YÖNETİCİ'])]))
sag_sayilar.append(len(df[df['GÖREV'].isin(['UZMAN', 'UZMAN'])]))



# Hesaplanan örnek sayılarına göre tabloları oluştur
sol_df = pd.DataFrame({
    'Bölünme': range(1, len(sol_sayilar) + 1),
    'B(sol)': sol_sayilar,
    'p(sol)': [sayi / len(df) for sayi in sol_sayilar],
    'Tsinif(EVET)': [len(df[(df['MAAS'] == 'NORMAL') & (df['MEMNUN'] == 'EVET')]),
                      len(df[(df['MAAS'] == 'YÜKSEK') & (df['MEMNUN'] == 'EVET')]),
                      len(df[(df['MAAS'] == 'DÜŞÜK') & (df['MEMNUN'] == 'EVET')]),
                      len(df[(df['DENEYİM'] == 'YOK') & (df['MEMNUN'] == 'EVET')]),
                      len(df[(df['DENEYİM'] == 'ORTA') & (df['MEMNUN'] == 'EVET')]),
                      len(df[(df['DENEYİM'] == 'İYİ') & (df['MEMNUN'] == 'EVET')]),
                      len(df[(df['GÖREV'] == 'UZMAN') & (df['MEMNUN'] == 'EVET')]),
                      len(df[(df['GÖREV'] == 'YÖNETİCİ') & (df['MEMNUN'] == 'EVET')])],
    'Tsinif(HAYIR)': [len(df[(df['MAAS'] == 'NORMAL') & (df['MEMNUN'] == 'HAYIR')]),
                       len(df[(df['MAAS'] == 'YÜKSEK') & (df['MEMNUN'] == 'HAYIR')]),
                       len(df[(df['MAAS'] == 'DÜŞÜK') & (df['MEMNUN'] == 'HAYIR')]),
                       len(df[(df['DENEYİM'] == 'YOK') & (df['MEMNUN'] == 'HAYIR')]),
                       len(df[(df['DENEYİM'] == 'ORTA') & (df['MEMNUN'] == 'HAYIR')]),
                       len(df[(df['DENEYİM'] == 'İYİ') & (df['MEMNUN'] == 'HAYIR')]),
                       len(df[(df['GÖREV'] == 'UZMAN') & (df['MEMNUN'] == 'HAYIR')]),
                       len(df[(df['GÖREV'] == 'YÖNETİCİ') & (df['MEMNUN'] == 'HAYIR')])],
    'P(EVET|t(sol))': [len(df[(df['MAAS'] == 'NORMAL') & (df['MEMNUN'] == 'EVET')]) / sol_sayilar[0],
                       len(df[(df['MAAS'] == 'YÜKSEK') & (df['MEMNUN'] == 'EVET')]) / sol_sayilar[1],
                       len(df[(df['MAAS'] == 'DÜŞÜK') & (df['MEMNUN'] == 'EVET')]) / sol_sayilar[2],
                       len(df[(df['DENEYİM'] == 'YOK') & (df['MEMNUN'] == 'EVET')]) / sol_sayilar[3],
                       len(df[(df['DENEYİM'] == 'ORTA') & (df['MEMNUN'] == 'EVET')]) / sol_sayilar[4],
                       len(df[(df['DENEYİM'] == 'İYİ') & (df['MEMNUN'] == 'EVET')]) / sol_sayilar[5],
                       len(df[(df['GÖREV'] == 'UZMAN') & (df['MEMNUN'] == 'EVET')]) / sol_sayilar[6],
                       len(df[(df['GÖREV'] == 'YÖNETİCİ') & (df['MEMNUN'] == 'EVET')]) / sol_sayilar[7]],
    'P(HAYIR|t(sol))': [len(df[(df['MAAS'] == 'NORMAL') & (df['MEMNUN'] == 'HAYIR')]) / sol_sayilar[0],
                        len(df[(df['MAAS'] == 'YÜKSEK') & (df['MEMNUN'] == 'HAYIR')]) / sol_sayilar[1],
                        len(df[(df['MAAS'] == 'DÜŞÜK') & (df['MEMNUN'] == 'HAYIR')]) / sol_sayilar[2],
                        len(df[(df['DENEYİM'] == 'YOK') & (df['MEMNUN'] == 'HAYIR')]) / sol_sayilar[3],
                        len(df[(df['DENEYİM'] == 'ORTA') & (df['MEMNUN'] == 'HAYIR')]) / sol_sayilar[4],
                        len(df[(df['DENEYİM'] == 'İYİ') & (df['MEMNUN'] == 'HAYIR')]) / sol_sayilar[5],
                        len(df[(df['GÖREV'] == 'UZMAN') & (df['MEMNUN'] == 'HAYIR')]) / sol_sayilar[6],
                        len(df[(df['GÖREV'] == 'YÖNETİCİ') & (df['MEMNUN'] == 'HAYIR')]) / sol_sayilar[7]]
})

sag_df = pd.DataFrame({
    'Bölünme': range(1, len(sag_sayilar) + 1),
    'B(sağ)': sag_sayilar,
    'p(sağ)': [sayi / len(df) for sayi in sag_sayilar],
    'Tsinif(EVET)': [len(df[(df['MAAS'].isin(['DÜŞÜK', 'YÜKSEK']) & (df['MEMNUN'] == 'EVET'))]),
                      len(df[(df['MAAS'].isin(['DÜŞÜK', 'NORMAL']) & (df['MEMNUN'] == 'EVET'))]),
                      len(df[(df['MAAS'].isin(['NORMAL', 'YÜKSEK']) & (df['MEMNUN'] == 'EVET'))]),
                      len(df[(df['DENEYİM'].isin(['ORTA', 'İYİ']) & (df['MEMNUN'] == 'EVET'))]),
                      len(df[(df['DENEYİM'].isin(['YOK', 'İYİ']) & (df['MEMNUN'] == 'EVET'))]),
                      len(df[(df['DENEYİM'].isin(['YOK', 'ORTA']) & (df['MEMNUN'] == 'EVET'))]),
                      len(df[(df['GÖREV'].isin(['UZMAN', 'YÖNETİCİ']) & (df['MEMNUN'] == 'EVET'))]),
                      len(df[(df['GÖREV'].isin(['UZMAN', 'UZMAN']) & (df['MEMNUN'] == 'EVET'))])],
    'Tsinif(HAYIR)': [len(df[(df['MAAS'].isin(['DÜŞÜK', 'YÜKSEK']) & (df['MEMNUN'] == 'HAYIR'))]),
                       len(df[(df['MAAS'].isin(['DÜŞÜK', 'NORMAL']) & (df['MEMNUN'] == 'HAYIR'))]),
                       len(df[(df['MAAS'].isin(['NORMAL', 'YÜKSEK']) & (df['MEMNUN'] == 'HAYIR'))]),
                       len(df[(df['DENEYİM'].isin(['ORTA', 'İYİ']) & (df['MEMNUN'] == 'HAYIR'))]),
                       len(df[(df['DENEYİM'].isin(['YOK', 'İYİ']) & (df['MEMNUN'] == 'HAYIR'))]),
                       len(df[(df['DENEYİM'].isin(['YOK', 'ORTA']) & (df['MEMNUN'] == 'HAYIR'))]),
                       len(df[(df['GÖREV'].isin(['UZMAN', 'YÖNETİCİ']) & (df['MEMNUN'] == 'HAYIR'))]),
                       len(df[(df['GÖREV'].isin(['UZMAN', 'UZMAN']) & (df['MEMNUN'] == 'HAYIR'))])],
    'P(EVET|t(sağ))': [len(df[(df['MAAS'].isin(['DÜŞÜK', 'YÜKSEK']) & (df['MEMNUN'] == 'EVET'))]) / sag_sayilar[0],
                       len(df[(df['MAAS'].isin(['DÜŞÜK', 'NORMAL']) & (df['MEMNUN'] == 'EVET'))]) / sag_sayilar[1],
                       len(df[(df['MAAS'].isin(['NORMAL', 'YÜKSEK']) & (df['MEMNUN'] == 'EVET'))]) / sag_sayilar[2],
                       len(df[(df['DENEYİM'].isin(['ORTA', 'İYİ']) & (df['MEMNUN'] == 'EVET'))]) / sag_sayilar[3],
                       len(df[(df['DENEYİM'].isin(['YOK', 'İYİ']) & (df['MEMNUN'] == 'EVET'))]) / sag_sayilar[4],
                       len(df[(df['DENEYİM'].isin(['YOK', 'ORTA']) & (df['MEMNUN'] == 'EVET'))]) / sag_sayilar[5],
                       len(df[(df['GÖREV'].isin(['UZMAN', 'YÖNETİCİ']) & (df['MEMNUN'] == 'EVET'))]) / sag_sayilar[6],
                       len(df[(df['GÖREV'].isin(['UZMAN', 'UZMAN']) & (df['MEMNUN'] == 'EVET'))]) / sag_sayilar[7]],
    'P(HAYIR|t(sağ))': [len(df[(df['MAAS'].isin(['DÜŞÜK', 'YÜKSEK']) & (df['MEMNUN'] == 'HAYIR'))]) / sag_sayilar[0],
                        len(df[(df['MAAS'].isin(['DÜŞÜK', 'NORMAL']) & (df['MEMNUN'] == 'HAYIR'))]) / sag_sayilar[1],
                        len(df[(df['MAAS'].isin(['NORMAL', 'YÜKSEK']) & (df['MEMNUN'] == 'HAYIR'))]) / sag_sayilar[2],
                        len(df[(df['DENEYİM'].isin(['ORTA', 'İYİ']) & (df['MEMNUN'] == 'HAYIR'))]) / sag_sayilar[3],
                        len(df[(df['DENEYİM'].isin(['YOK', 'İYİ']) & (df['MEMNUN'] == 'HAYIR'))]) / sag_sayilar[4],
                        len(df[(df['DENEYİM'].isin(['YOK', 'ORTA']) & (df['MEMNUN'] == 'HAYIR'))]) / sag_sayilar[5],
                        len(df[(df['GÖREV'].isin(['UZMAN', 'YÖNETİCİ']) & (df['MEMNUN'] == 'HAYIR'))]) / sag_sayilar[6],
                        len(df[(df['GÖREV'].isin(['UZMAN', 'UZMAN']) & (df['MEMNUN'] == 'HAYIR'))]) / sag_sayilar[7]]
})

print("Sol Tablo:")
print(sol_df)

print("\nSağ Tablo:")
print(sag_df)
