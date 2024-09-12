import os
import matplotlib.pyplot as plt
import sys
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def main():
    open_archives()

def open_archives():
     #Get the centroids
    for c in range (4,6):
        for phi in range (30, 70, 10):
            for perc in range (13, 16, 2):
                perc /= 10
                for file_count in range (1, 103, 1):
                    file_name = f"File_{file_count}_centroids.txt"
                    
                    if (c == 4):
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)+"\\conf"
                        file_path = os.path.join(base_path,file_name)
                        try:
                            os.remove(file_path)
                            print(f"Se han borrado los archivo : {file_path}")
                        except Exception as e: 
                            print(f"No se pudo borrar el archivo {file_path}: {e}")
                        

                    if (c == 5): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)+"\\conf"
                        file_path = os.path.join(base_path,file_name)
                        try:
                            os.remove(file_path)
                            print(f"Se han borrado los archivo : {file_path}")
                        except Exception as e: 
                            print(f"No se pudo borrar el archivo {file_path}: {e}")




                        



                    



                                    
if __name__ == "__main__":
    main()