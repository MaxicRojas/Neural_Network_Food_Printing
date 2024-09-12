import numpy as np
import tensorflow as tf 
import matplotlib.pyplot as plt
import os
import random
import tensorboard
from datetime import datetime
from packaging import version


# Load the coordinates and stress values from the files
def main():
    x,y,z,x_test,y_test,z_test,t_strain,t_stress=load_data()
    x = tf.convert_to_tensor(x)
    y = tf.convert_to_tensor(y)
    x_test = tf.convert_to_tensor(x_test)
    #y_test = tf.convert_to_tensor(y_test)
    # Compile the model
    initial_learning_rate = 0.0001
    min_learning_rate = 1e-10
    opt = (tf.keras.optimizers.Adam(learning_rate = initial_learning_rate))
    model.compile(optimizer = opt, loss='mean_absolute_error')
    def lr_schedule(epoch):
        new_learning_rate = initial_learning_rate * tf.math.exp(-0.01*epoch)
        return tf.maximum(new_learning_rate, min_learning_rate)
    lr_scheduler = tf.keras.callbacks.LearningRateScheduler(lr_schedule)
    #Early_stopping
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=100)
    #TensorBoard
    logdir="logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)
    # Train the model   
    history = model.fit(x, y, epochs=2000, batch_size=32, validation_split=0, callbacks =[lr_scheduler,early_stopping,tensorboard_callback]) 
    stopped_epoch = early_stopping.stopped_epoch 
    plot_loss(history,stopped_epoch)
    # Save the trained model
    model.save('stress_prediction_model.h5')
    
    # Make predictions
    predictions = model.predict(x_test)
    value = np.sum(np.abs(predictions-y_test))/len(predictions)
    

    

    #Cubic_predictions
    cube_pre, z_cube, y_cube = cubic_predict('old_predictions.txt')
    c_stress, c_strain = cubic_total('diamond_actual.txt')

    plot_predicted_data_full(z_test, predictions, y_test,t_strain,t_stress,cube_pre,z_cube,y_cube,c_stress,c_strain)
    # Print or use predictions as needed
    print("Prueba --------------------------")
    print("Mean absolute error:", value)

def cubic_predict(filename):
    predictions = []
    z_cube =[]
    y_cube = []
    with open(filename, 'r') as file:
        for line in file: 
            values = line.strip().split('\t')
            predictions.append(float(values[0]))
            z_cube.append(float(values[1]))
            y_cube.append(float(values[2]))
    return predictions, z_cube, y_cube
def cubic_total(filename):
    c_stress = []
    c_strain = []
    with open(filename, 'r') as file:
        for line in file: 
            values = line.strip().split('\t')
            c_stress.append(float(values[0]))
            c_strain.append(float(values[1]))
    return c_stress,c_strain
def plot_predicted_data_full(z_test, predictions, y_test, t_strain, t_stress, cube_pre, z_cube,y_cube,c_stress,c_strain):
    predictions = np.array(predictions)
    flatten_pre = predictions.ravel()
    y_test = np.array(y_test)
    z_test = np.array(z_test)

    # Plot Actual data & predicted data
    fig, ax1 = plt.subplots()  # create a figure and an axes
    ax1.scatter(z_test, predictions, color='r', label='Predicción de tensión hidrogel de diamante')  # plot the predicted data on the first axes
    ax1.set_xlabel('Deformación')  # set the x-axis label
    ax1.set_ylabel('Tensión', color='r')  # set the y-axis label for the predicted data
    ax1.tick_params(axis='y', labelcolor='r')  # set the y-axis tick color for the predicted data

    # Curve of the stress vs. strain data
    ax1.plot(t_strain, t_stress, color='g', label='Curva de la tensión')

    ax2 = ax1.twinx()  # create a second axes that shares the same x-axis
    ax2.scatter(z_test, y_test, color='b', label='Tensión real', s=10)  # plot the actual data on the second axes

    

    # Third scatter plot on the same set of axes as ax2
    ax2.scatter(z_cube, cube_pre, color='#800000', label='Predicción de tensión de hidrogel cubico', marker  = "s")
    ax2.plot(c_strain,c_stress, color = 'black', linestyle = '--',label = 'Curva tensión hydrogel cubico')


    ax3 =ax2.twinx()
    ax3.scatter(z_cube,y_cube,color='#FF00FF', marker = "s", s= 10)

    plt.title('Tensión vs. Deformación')  # set the title

    # Note: No need to create a new ax3 as it's not required when sharing the axes with ax2
    plt.show()
    


    # Test the model on new coordinates
#load the files in ther 

def plot_loss(history, stopped_epoch):
    plt.plot(history.history['loss'][:stopped_epoch+1])  # Solo muestra hasta el punto de detención
    plt.title('Loss vs. epochs')
    plt.ylabel('Loss')
    plt.yscale('log')
    plt.xlabel('Epoch')
    plt.legend(['Training'], loc='upper right')
    plt.show()


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





# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1024, input_dim=900, activation='relu'),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(254, activation='relu'),
    tf.keras.layers.Dense(254, activation='relu'),
    tf.keras.layers.Dense(254, activation='relu'),
    tf.keras.layers.Dense(254, activation='relu'),
    tf.keras.layers.Dense(125, activation='relu'),
    tf.keras.layers.Dense(125, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(254, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1)
])



if __name__ == "__main__":
    main()