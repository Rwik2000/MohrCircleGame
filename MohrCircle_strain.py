import numpy as np
np.seterr(all='raise')
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
# reqAngle_strain = None
# isAngle_strain = False

def Plot_Mohr_Circle(Strain, dim, Stress_tensor, isAngle_strain, reqAngle_strain):
    # global isAngle_strain, reqAngle_strain
    Strain.sort(reverse=True)
    sigma1=Strain[0]
    sigma2=Strain[1]
    centre1_2=round((sigma1+sigma2)/2, 4)
    radius1_2=abs(sigma2-centre1_2)
    new_point = []
    if dim==3:
        sigma3=Strain[2]        
        centre1_3=round((sigma1+sigma3)/2, 4)
        centre2_3=round((sigma2+sigma3)/2, 4)    
        radius1_3=abs(sigma3-centre1_3)    
        radius2_3=abs(sigma2-centre2_3)
        print("The Principal Stresses are: \nε1: {0} \nε2: {1} \nε3: {2} \n".format(sigma1,sigma2,sigma3))
        print("Maximum Shear Strain τ_max: " +str(round((sigma1-sigma3)/2, 3)))
        print("\nThe Centres of the circle are: \nC1: {0} \nC2: {1} \nC3: {2} \n".format(centre1_3,centre1_2,centre2_3))
    else:
        print("The Principal Stresses are: \nε1: {0} \nε2: {1} \n".format(sigma1,sigma2))
        print("Maximum Shear Strain τ_max: " +str(round((sigma1-sigma2)/2, 3))) 
        print("\nThe Centre of the circle are: \nC1: {0}".format(centre1_2))           

    

    _, ax = plt.subplots()
    if dim == 3:
        ax.set(xlim=(centre1_3-(radius1_3+0.5), sigma1+0.5), ylim = (-(radius1_3+1), radius1_3+1))
        mohr_centre=[[centre1_3,0],[centre2_3,0],[centre1_2,0]]
        mohr_sigma=[[sigma1,0],[sigma2,0],[sigma3,0]]
        ax.plot(*zip(*mohr_centre), marker='o', color='r', ls='')
        ax.plot(*zip(*mohr_sigma), marker='o', color='b', ls='')
        for i in range(len(mohr_sigma)):
            ax.annotate("ε"+str(i+1),tuple(mohr_sigma[i]),fontsize=12)
        for i in range(len(mohr_centre)):
            ax.annotate("C"+str(i+1),tuple(mohr_centre[i]),fontsize=12)

        Circle1_3 = plt.Circle((centre1_3, 0),abs(radius1_3),fill=False, color="red")
        Circle2_3 = plt.Circle((centre2_3, 0),abs(radius2_3),fill=False, color="blue")
        Circle1_2 = plt.Circle((centre1_2, 0),abs(radius1_2),fill=False, color="green")
        ax.add_artist(Circle1_3)
        ax.add_artist(Circle1_2)
        ax.add_artist(Circle2_3)
        ax.minorticks_on()
    elif dim ==2:
        ax.set(xlim=(centre1_2-(radius1_2+0.5), sigma1+0.5), ylim = (-(radius1_2+0.5), radius1_2+0.5))
        mohr_centre=[[centre1_2,0]]
        mohr_sigma=[[sigma1,0],[sigma2,0]]
        ax.plot(*zip(*mohr_centre), marker='o', color='r', ls='')
        ax.plot(*zip(*mohr_sigma), marker='o', color='b', ls='')
        points = [[Stress_tensor[0][0],Stress_tensor[0][1]],[Stress_tensor[1][1],-Stress_tensor[0][1]]]
        ax.plot(*zip(*points),marker='o', color='black', ls='')
        ax.plot([Stress_tensor[0][0],Stress_tensor[1][1]],[Stress_tensor[0][1],-Stress_tensor[0][1]])
        if(isAngle_strain):
            try:
                curr_angle = np.arctan((Stress_tensor[0][1])/(Stress_tensor[0][0]-centre1_2))
            except:
                if(Stress_tensor[0][1]>=0):
                    curr_angle = np.deg2rad(90)
                else:
                    curr_angle = np.deg2rad(-90)
            total_angle = curr_angle + np.deg2rad(reqAngle_strain)
            # print(np.rad2deg(total_angle))
            new_x_1 = radius1_2*np.cos(total_angle) + centre1_2
            new_y_1 = radius1_2*np.sin(total_angle)    
            new_x_2 = radius1_2*np.cos(total_angle + np.deg2rad(180))+centre1_2
            new_y_2 = radius1_2*np.sin(total_angle + np.deg2rad(180))
            new_points = [[new_x_1,new_y_1],[new_x_2,new_y_2]]
            ax.plot(*zip(*new_points),marker='o', color='black', ls='')
            ax.plot([new_x_1,new_x_2],[new_y_1,new_y_2])
        ax.plot()
        for i in range(len(mohr_sigma)):
            ax.annotate("ε"+str(i+1),tuple(mohr_sigma[i]),fontsize=12)
        for i in range(len(mohr_centre)):
            ax.annotate("C"+str(i+1),tuple(mohr_centre[i]),fontsize=12)
        Circle1_2 = plt.Circle((centre1_2, 0),abs(radius1_2),fill=False, color="green")
        ax.add_artist(Circle1_2)

    ax.minorticks_on()
    ax.set_aspect('equal', adjustable='box')
    # ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.grid(which='major', axis='both', linestyle ='--')
    plt.show()

    return mohr_centre
def find_Principal_Stress(Stress_tensor, isAngle_strain, reqAngle_strain):
    if Stress_tensor.shape == (3,3):
        a=Stress_tensor.copy()
        I1= a[0][0] + a[1][1] + a[2][2]
        I2= a[0][0]*a[1][1] + a[1][1]*a[2][2] + a[0][0]*a[2][2] - a[0][1]**2 - a[0][2]**2 -a[1][2]**2
        I3 = np.linalg.det(Stress_tensor)
        a=np.linalg.eig(a)[0]    
        a=np.round(a, 4)
        return Plot_Mohr_Circle(list(a), dim=3, Stress_tensor= Stress_tensor, isAngle_strain=isAngle_strain, reqAngle_strain=reqAngle_strain)
    elif Stress_tensor.shape == (2,2):
        a=Stress_tensor.copy()
        I1= a[0][0] + a[1][1]
        # print(a[0][1])
        I2= a[0][0]*a[1][1] - a[0][1]**2 
        a=np.linalg.eig(a)[0]    
        a=np.round(a, 4)
        return Plot_Mohr_Circle(list(a), dim=2, Stress_tensor = Stress_tensor, isAngle_strain=isAngle_strain, reqAngle_strain=reqAngle_strain)        

def input_to_tensor(εxx,εyy,εzz,εxy,εyz,εzx, n_dim, isAngle_strain, reqAngle_strain):
    # print()
    if n_dim==2:
        ε_tensor = [[εxx , εxy ],
                    [εxy , εyy ]]
    else:                    
        ε_tensor = [[εxx , εxy , εzx],
                    [εxy , εyy , εyz],
                    [εzx , εyz , εzz]]
    ε_tensor= np.array(ε_tensor)
    # print(ε_tensor.shape)
    return find_Principal_Stress(ε_tensor, isAngle_strain, reqAngle_strain)

def strain_execute(n_dim, input, isAngle_strain=False, reqAngle_strain=None):
    # print(input)
    if n_dim == 3:
        for i in range(3):
            if input[i+3]==None:
                input[i+3]=0
    
    return input_to_tensor(εxx = input[0],εyy = input[1],εzz = input[3], εxy = input[2],
                           εyz = input[4],εzx = input[5], n_dim=n_dim, isAngle_strain=isAngle_strain,reqAngle_strain= reqAngle_strain)

# ########### User input ##########
# '''For two dimensional mohr circle, input only εxx,εyy,εxy, leave εzz,εyz,εzx as None'''
# εxx=-4
# εyy=-4
# εxy=1

# '''For three dimensional mohr circle, input the following '''
# εzz=3
# εyz=0
# εzx=0
# input = [εxx, εyy, εxy, εzz, εyz, εzx]
# ##################################

# strain_execute(n_dim=2,  input=input, isAngle_strain=True, reqAngle_strain=22.5)

