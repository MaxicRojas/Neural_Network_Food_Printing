import os
import matplotlib.pyplot as plt
import sys
from sklearn.cluster import KMeans

def main(): 
    print("\nSelect a number to choose which graph to make")
    print("1: Stress ")
    print("2: Energy ")
    print("3: Temperature")
    x  = int(input("Write the number: "))
    data_4_13_30= []
    data_4_13_40= []
    data_4_13_50= []
    data_4_13_60= []
    data_4_15_30= []
    data_4_15_40= []
    data_4_15_50= []
    data_4_15_60= []
    data_5_13_30= []
    data_5_13_40= []
    data_5_13_50= []
    data_5_13_60= []
    data_5_15_30= []
    data_5_15_40= []
    data_5_15_50= []
    data_5_15_60= []
    if (x == 1):
        file_name = "gstress_trace_g0.01_rate0.0001.data"
    elif(x == 2 or x == 3):
        file_name = "energy_shear_g0.01_rate0.0001.data"
    else:
        print("Ending program no correct number selected")
        sys.exit()



    
    open_archives(file_name,data_4_13_30,data_4_13_40,data_4_13_50,data_4_13_60,data_4_15_30,data_4_15_40,data_4_15_50,data_4_15_60,data_5_13_30,data_5_13_40,data_5_13_50,data_5_13_60,data_5_15_30,data_5_15_40,data_5_15_50,data_5_15_60,x)
    



def open_archives(file_name,data_4_13_30,data_4_13_40,data_4_13_50,data_4_13_60,data_4_15_30,data_4_15_40,data_4_15_50,data_4_15_60,data_5_13_30,data_5_13_40,data_5_13_50,data_5_13_60,data_5_15_30,data_5_15_40,data_5_15_50,data_5_15_60,option):

    
    for c in range (4, 6):
        for phi in range (30, 70, 10):
            for perc in range (13, 16, 2):
                perc /= 10
                #Get the stress graph
                if (option == 1):
                    if (c == 4 and perc == 1.3): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_4_13_30.append((float(values[1]), float(values[5])))
                                elif phi == 40:
                                    data_4_13_40.append((float(values[1]), float(values[5])))
                                elif phi == 50:
                                    data_4_13_50.append((float(values[1]), float(values[5])))
                                elif phi == 60:
                                    data_4_13_60.append((float(values[1]), float(values[5])))
                    if (c == 4 and perc == 1.5): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_4_15_30.append((float(values[1]), float(values[5])))
                                elif phi == 40:
                                    data_4_15_40.append((float(values[1]), float(values[5])))
                                elif phi == 50:
                                    data_4_15_50.append((float(values[1]), float(values[5])))
                                elif phi == 60:
                                    data_4_15_60.append((float(values[1]), float(values[5])))
                    if (c == 5 and perc == 1.3): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_5_13_30.append((float(values[1]), float(values[5])))
                                elif phi == 40:
                                    data_5_13_40.append((float(values[1]), float(values[5])))
                                elif phi == 50:
                                    data_5_13_50.append((float(values[1]), float(values[5])))
                                elif phi == 60:
                                    data_5_13_60.append((float(values[1]), float(values[5])))
                    if (c == 5 and perc == 1.5): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_5_15_30.append((float(values[1]), float(values[5])))
                                elif phi == 40:
                                    data_5_15_40.append((float(values[1]), float(values[5])))
                                elif phi == 50:
                                    data_5_15_50.append((float(values[1]), float(values[5])))
                                elif phi == 60:
                                    data_5_15_60.append((float(values[1]), float(values[5])))

                #Get the energy graph 
                if (option == 2):
                    if (c == 4 and perc == 1.3): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_4_13_30.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 40:
                                    data_4_13_40.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 50:
                                    data_4_13_50.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 60:
                                    data_4_13_60.append((float(values[0]), float(values[2]) + float(values[3])))
                    if (c == 4 and perc == 1.5): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_4_15_30.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 40:
                                    data_4_15_40.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 50:
                                    data_4_15_50.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 60:
                                    data_4_15_60.append((float(values[0]), float(values[2]) + float(values[3])))
                    if (c == 5 and perc == 1.3): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_5_13_30.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 40:
                                    data_5_13_40.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 50:
                                    data_5_13_50.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 60:
                                    data_5_13_60.append((float(values[0]), float(values[2]) + float(values[3])))
                    if (c == 5 and perc == 1.5): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_5_15_30.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 40:
                                    data_5_15_40.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 50:
                                    data_5_15_50.append((float(values[0]), float(values[2]) + float(values[3])))
                                elif phi == 60:
                                    data_5_15_60.append((float(values[0]), float(values[2]) + float(values[3])))
                #Get the Temperature graph
                if (option == 3):
                    if (c == 4 and perc == 1.3): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_4_13_30.append((float(values[0]), float(values[1])))
                                elif phi == 40:
                                    data_4_13_40.append((float(values[0]), float(values[1])))
                                elif phi == 50:
                                    data_4_13_50.append((float(values[0]), float(values[1])))
                                elif phi == 60:
                                    data_4_13_60.append((float(values[0]), float(values[1])))
                    if (c == 4 and perc == 1.5): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_4_15_30.append((float(values[0]), float(values[1])))
                                elif phi == 40:
                                    data_4_15_40.append((float(values[0]), float(values[1])))
                                elif phi == 50:
                                    data_4_15_50.append((float(values[0]), float(values[1])))
                                elif phi == 60:
                                    data_4_15_60.append((float(values[0]), float(values[1])))
                    if (c == 5 and perc == 1.3): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_5_13_30.append((float(values[0]), float(values[1])))
                                elif phi == 40:
                                    data_5_13_40.append((float(values[0]), float(values[1])))
                                elif phi == 50:
                                    data_5_13_50.append((float(values[0]), float(values[1])))
                                elif phi == 60:
                                    data_5_13_60.append((float(values[0]), float(values[1])))
                    if (c == 5 and perc == 1.5): 
                        base_path = "C:\\Users\\maxim\\Documents\\Reologia\\cubic_lattice\\Insert_colloids\\ncells_"+str(c)+"\\b_16\\phi_0."+str(phi)+"\\perc_bi_"+str(perc)
                        file_path = os.path.join(base_path,file_name)
                        with open(file_path, 'r') as file:
                            next(file)
                            for line in file:
                                values = line.split()
                                if phi == 30:
                                    data_5_15_30.append((float(values[0]), float(values[1])))
                                elif phi == 40:
                                    data_5_15_40.append((float(values[0]), float(values[1])))
                                elif phi == 50:
                                    data_5_15_50.append((float(values[0]), float(values[1])))
                                elif phi == 60:
                                    data_5_15_60.append((float(values[0]), float(values[1])))
                
    plot_cell_1(option,[data_4_13_30,data_4_13_40,data_4_13_50,data_4_13_60], labels=["Phi 0.30", "Phi 0.40", "Phi 0.50", "Phi 0.60"])
    plot_cell_2(option,[data_4_15_30,data_4_15_40,data_4_15_50,data_4_15_60], labels=["Phi 0.30", "Phi 0.40", "Phi 0.50", "Phi 0.60"])
    plot_cell_3(option,[data_5_13_30,data_5_13_40,data_5_13_50,data_5_13_60], labels=["Phi 0.30", "Phi 0.40", "Phi 0.50", "Phi 0.60"])
    plot_cell_4(option,[data_5_15_30,data_5_15_40,data_5_15_50,data_5_15_60], labels=["Phi 0.30", "Phi 0.40", "Phi 0.50", "Phi 0.60"])
    

#Graph the data for 4 cells perc 1.3 
def plot_cell_1(option,datasets, labels):
    plt.figure()
    colors = ['b', 'g','r', 'c']

    for i, data in enumerate(datasets):
        x, y = zip(*data)
        plt.plot(x,y,marker='o',linestyle='-', label = labels[i],color = colors[i])

    
    if (option == 1):
        plt.title('Stress graph with 4 cells, 16 beads, 1.3 size')
        plt.xlabel('Gama')
        plt.ylabel('Deformation')
        plt.xscale('log')
        plt.yscale('log')
    elif (option == 2):
        plt.title('Total Energy with 4 cells, 16 beads, 1.3 size')
        plt.xlabel('Time')
        plt.ylabel('Sum of 3 and 4 column')
    elif (option == 3): 
        plt.title('Temperature with 4 cells, 16 beads, 1.3 size')
        plt.xlabel('Time')
        plt.ylabel('Temperature')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_cell_2(option,datasets, labels):
    plt.figure()
    colors = ['b', 'g','r', 'c']

    for i, data in enumerate(datasets):
        x, y = zip(*data)
        plt.plot(x,y,marker='o',linestyle='-', label = labels[i],color = colors[i])

    
    if (option == 1):
        plt.title('Stress graph with 4 cells, 16 beads, 1.5 size')
        plt.xlabel('Gama')
        plt.ylabel('Deformation')
        plt.xscale('log')
        plt.yscale('log')
    elif (option == 2):
        plt.title('Total Energy with 4 cells, 16 beads, 1.5 size')
        plt.xlabel('Time')
        plt.ylabel('Sum of 3 and 4 column')
    elif (option == 3): 
        plt.title('Temperature with 4 cells, 16 beads, 1.5 size')
        plt.xlabel('Time')
        plt.ylabel('Temperature')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_cell_3(option,datasets, labels):
    plt.figure()
    colors = ['b', 'g','r', 'c']

    for i, data in enumerate(datasets):
        x, y = zip(*data)
        plt.plot(x,y,marker='o',linestyle='-', label = labels[i],color = colors[i])

    
    if (option == 1):
        plt.xlabel('Gama')
        plt.ylabel('Deformation')
        plt.title('Stress graph with 5 cells, 16 beads, 1.3 size')
        plt.xscale('log')
        plt.yscale('log')
    elif (option == 2):
        plt.title('Total Energy with 5 cells, 16 beads, 1.3 size')
        plt.xlabel('Time')
        plt.ylabel('Sum of 3 and 4 column')
    elif (option == 3): 
        plt.title('Temperature with 5 cells, 16 beads, 1.3 size')
        plt.xlabel('Time')
        plt.ylabel('Temperature')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_cell_4(option,datasets, labels):
    plt.figure()
    colors = ['b', 'g','r', 'c']

    for i, data in enumerate(datasets):
        x, y = zip(*data)
        plt.plot(x,y,marker='o',linestyle='-', label = labels[i],color = colors[i])

    
    if (option == 1):
        plt.title('Stress graph with 5 cells, 16 beads, 1.5 size')
        plt.xlabel('Gama')
        plt.ylabel('Deformation')
        plt.xscale('log')
        plt.yscale('log')
    elif (option == 2):
        plt.title('Total Energy with 5 cells, 16 beads, 1.5 size')
        plt.xlabel('Time')
        plt.ylabel('Sum of 3 and 4 column')
    elif (option == 3): 
        plt.title('Temperature with 5 cells, 16 beads, 1.5 size')
        plt.xlabel('Time')
        plt.ylabel('Temperature')
    
    plt.grid(True)
    plt.legend()
    plt.show()
                    

        
               

if __name__ == "__main__":
    main()



