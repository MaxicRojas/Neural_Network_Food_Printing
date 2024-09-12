import os
import matplotlib.pyplot as plt
import sys
import numpy as np
from sklearn.cluster import KMeans


def main():
    txtpath = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice"
    open_archives(txtpath)

def open_archives(txtpath):
    #Get the centroids
    file_count = 1
    base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_4\\b_16\\phi_0.40\\perc_bi_1.5\\conf"
    files = os.listdir(base_path)
    for file in files:
        cor_x, cor_y, cor_z = [], [], []
        file_path = os.path.join(base_path,file)
        with open(file_path, 'r') as f:
            data = np.loadtxt(file_path, skiprows=9, usecols=(2,3,4))
            cor_x.extend(data[:, 0])  # Append values from column 2 to cor_x
            cor_y.extend(data[:, 1])  # Append values from column 3 to cor_y
            cor_z.extend(data[:, 2])  # Append values from column 4 to cor_z

        #Make x, y, z coordinates into a single array
        coordinates = np.column_stack((cor_x,cor_y,cor_z))

        #Use K-Means to find centroids
        num_clusters = 300
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(coordinates)
        centroids = kmeans.cluster_centers_
        
        
        #Write centroids in another txt file
        output_file_path = os.path.join(base_path,f"File_{file_count}_centroids.txt")
        with open(output_file_path, 'w') as output_file:
            centroids_str = '\n'.join([','.join(map(str, centroid)) for centroid in centroids])
            output_file.write(centroids_str)
        file_count += 1



                                    
if __name__ == "__main__":
    main()