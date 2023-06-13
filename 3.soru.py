import pandas as pd
import math

data = {'x': ['1', '2', '2', '3', '4', '5', '6', '8', '10', '11'],
        'y': ['3', '5', '3', '9', '7', '2', '8', '6', '6', '1'],
        'z': ['Negatif', 'Pozitif', 'Pozitif', 'Negatif', 'Negatif',
              'Pozitif', 'Pozitif', 'Negatif', 'Negatif', 'Negatif']}

df = pd.DataFrame(data)
print(df.to_string(index=False))
print('')
print(df[['x','y']].to_string(index=False))

x_new = 7
y_new = 3

distances = []
for i, row in df.iterrows():
    x = int(row['x'])
    y = int(row['y'])
    distance = math.sqrt((x - x_new) ** 2 + (y - y_new) ** 2)
    distances.append(distance)

df['uzaklik'] = distances
df['Sıralama'] = df['uzaklik'].rank()


print('')
print(df.to_string(index=False))

# En yakın 3 komşuyu seçme
en_yakin_komsular = df.nsmallest(3, 'uzaklik')

# Sınıfları kontrol ederek yeni örneğin sınıfını belirleme
siniflar = en_yakin_komsular['z'].tolist()
sinif = max(set(siniflar), key=siniflar.count)

print('\n'f"Yeni örneğin sınıfı: {sinif}")

