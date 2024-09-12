import numpy as np
from sklearn.metrics import silhouette_score

# Leer los centroides desde el archivo de texto
centroid_file_path = r"C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_4\\b_16\\phi_0.40\\perc_bi_1.5\\conf\\File_1_centroids.txt"
centroids = np.loadtxt(centroid_file_path, delimiter=',')

# Leer tus datos originales, por ejemplo, desde el archivo 'data.txt'
data = np.loadtxt(r"C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_4\\b_16\\phi_0.40\\perc_bi_1.5\\conf\\mhel.dump.0", skiprows=9, usecols=(2, 3, 4))

# Asignar cada punto de datos al centroide más cercano
labels = np.argmin(np.linalg.norm(data[:, np.newaxis, :] - centroids, axis=2), axis=1)

# Calcular el Silhouette Score
silhouette_avg = silhouette_score(data, labels)
print("Silhouette Score:", silhouette_avg)
