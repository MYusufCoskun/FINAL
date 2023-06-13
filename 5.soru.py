import numpy as np

# Veri setini oluşturma
X = np.array([[5.1, 3.5, 1.4, 0.2],
              [4.9, 3.0, 1.4, 0.2],
              [7.0, 3.2, 4.7, 1.4],
              [6.4, 3.2, 4.5, 1.5],
              [6.3, 3.3, 6.0, 2.5],
              [5.8, 2.7, 5.1, 1.9]])

# Hedef sınıf etiketlerini oluşturma
Y = np.array([[1, 0, 0],
              [1, 0, 0],
              [0, 1, 0],
              [0, 1, 0],
              [0, 0, 1],
              [0, 0, 1]])

# Matrisleri oluşturma
X_transpose = np.transpose(X)
X_transpose_X = np.dot(X_transpose, X)
X_transpose_Y = np.dot(X_transpose, Y)

# Katsayıları hesaplama
theta = np.dot(np.linalg.inv(X_transpose_X), X_transpose_Y)
print("Doğrusal regresyon katsayıları:")
print(theta)
# Yeni örnek
Yeni = np.array([[5.0, 3.4, 1.5, 0.2]], dtype=float)


# Yeni örneğin hangi sınıfa ait olduğunu belirleme
Yeni_Y = np.dot(Yeni, theta)
sinif_index = np.argmax(Yeni_Y)
sinif = chr(ord('A') + sinif_index)

# Sonuçları yazdırma
print('')
print("Yeni örneğin sınıfı:", sinif)
