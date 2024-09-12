import numpy as np
import tensorflow as tf 
import matplotlib.pyplot as plt
from sklearn import  model_selection
import os
import random

def main():
    x,y,z,x_test,y_test,z_test,t_strain,t_stress=load_data()

    print("\n", z_test)
    print("\n", y_test)

def load_data():
    mylist = np.arange(102)
    random.seed(100)   
    random.shuffle(mylist)
    data=[]
    stress = [] # input stress_value    
    strain = []
    complete_strain = []
    for file_count in range (1, 103, 1):
        file_name_1 = f"File_{file_count}_centroids.txt"
        x = [] #input x coordinate
        y = [] #input y coordinate
        z = [] #input z  coordinate
        base_path_1 = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_4\\b_16\\phi_0.40\\perc_bi_1.5\\conf"
        file_stress = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Shear_mixture\\ncells_4\\b_16\\phi_0.40\\perc_bi_1.5\\gstress_trace_g0.01_rate0.0001.data"
        file_path = os.path.join(base_path_1,file_name_1)
        with open(file_path, 'r') as f:
            centroids = np.loadtxt(file_path, delimiter=',')
        with open (file_stress, 'r') as f:
            #Hacer otro array con strain e igual se haga el shuffle 
            all_strain_value = np.loadtxt(file_stress,skiprows=1, usecols=1)
            strain_value = all_strain_value[file_count-1]
            all_stress_value = np.loadtxt(file_stress, skiprows=1,usecols=5)
            stress_value = all_stress_value[file_count-1]
        x.append(centroids[:,0])
        y.append(centroids[:,1])
        z.append(centroids[:,2])
        vect=np.concatenate([np.transpose(np.array(x)),np.transpose(np.array(y)),np.transpose(np.array(z))], axis = 0)
        data.append(vect) #Revisar shape 
        stress.append(stress_value)
        strain.append(strain_value)
     
    shuffled_data = [data[number] for number in mylist]
    shuffled_stress = [stress[number] for number in mylist]
    shuffled_strain = [strain[number] for number in mylist]
    shuffle_data_train = shuffled_data[:90]
    shuffle_stress_train = shuffled_stress[:90]
    shuffle_strain_train = shuffled_strain[:90]
    shuffle_data_test = shuffled_data[90:]
    shuffle_stress_test = shuffled_stress[90:] 
    shuffle_strain_test = shuffled_strain[90:]


    return shuffle_data_train,shuffle_stress_train, shuffle_strain_train, shuffle_data_test, shuffle_stress_test, shuffle_strain_test,strain,stress



if __name__ == "__main__":
    main()