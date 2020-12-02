import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
# reqAngle = 30
# isAngle = True

class Stress_MohrCircle():
    def __init__(self, σxx,σyy,σxy,σzz = 0,σyz = 0,σzx = 0):
        self.σxx = σxx
        self.σyy = σyy
        self.σzz = σzz
        self.σxy = σxy
        self.σyz = σyz
        self.σzx = σzx
        self.ndims = 3
        self.isGraph = False
        self.isAngle_stress = False
        self.reqAngle_stress_2d = None
        self.reqAngle_normal_3d = [0,0,0]
    def Find_Mohr_Circle(self):
        # global isAngle, reqAngle
        Stress = list(self.principal_stress)
        Stress_tensor = self.σ_tensor
        # print(Stress)
        Stress.sort(reverse=True)
        sigma1=Stress[0]
        sigma2=Stress[1]
        center1_2=round((sigma1+sigma2)/2, 4)
        radius1_2=abs(sigma2-center1_2)
        if self.ndims==3:
            sigma3=Stress[2]        
            center1_3=round((sigma1+sigma3)/2, 4)
            center2_3=round((sigma2+sigma3)/2, 4)    
            radius1_3=abs(sigma3-center1_3)    
            radius2_3=abs(sigma2-center2_3)
            print("The Principal Stresses are: \nε1: {0} \nε2: {1} \nε3: {2} \n".format(sigma1,sigma2,sigma3))
            print("Maximum Shear Stress τ_max: " +str(round((sigma1-sigma3)/2, 3)))
            print("\nThe centers of the circle are: \nC1: {0} \nC2: {1} \nC3: {2} \n".format(center1_3,center1_2,center2_3))
        else:
            print("The Principal Stresses are: \nε1: {0} \nε2: {1} \n".format(sigma1,sigma2))
            print("Maximum Shear Stress τ_max: " +str(round((sigma1-sigma2)/2, 3))) 
            print("\nThe center of the circle are: \nC1: {0}".format(center1_2))           

        
        new_x_1, new_x_2,new_y_1,new_y_2 = None, None, None, None
        sigma_NN,sigma_NS = None, None
        radius = []
        _, ax = plt.subplots()
        if self.ndims == 3:
            ax.set(xlim=(center1_3-(radius1_3+0.5), sigma1+0.5), ylim = (-(radius1_3+1), radius1_3+1))
            radius = [radius1_2,radius2_3,radius1_3]
            mohr_center=[[center1_3,0],[center2_3,0],[center1_2,0]]
            mohr_sigma=[[sigma1,0],[sigma2,0],[sigma3,0]]
            if(self.isAngle_stress):
                l = self.reqAngle_normal_3d[0]
                m = self.reqAngle_normal_3d[1]
                n2 = 1 - l**2 - m**2
                print(l,m,n2)
                if(n2<0):
                    print("Invalid Angle input!!!!!")
                    raise ValueError('Bad input!')
                # else:
                n = np.sqrt(n2)
                sigma_NN = (l**2)*sigma1 + (m**2)*sigma2 + (n**2)*sigma3
                sigma_NS = np.sqrt((l**2)*sigma1**2 + (m**2)*sigma2**2 + (n**2)*sigma3**2 - sigma_NN**2)
            if(self.isGraph):
                ax.plot(*zip(*mohr_center), marker='o', color='r', ls='')
                ax.plot(*zip(*mohr_sigma), marker='o', color='b', ls='')
                for i in range(len(mohr_sigma)):
                    ax.annotate("σ"+str(i+1),tuple(mohr_sigma[i]),fontsize=12)
                for i in range(len(mohr_center)):
                    ax.annotate("C"+str(i+1),tuple(mohr_center[i]),fontsize=12)

                Circle1_3 = plt.Circle((center1_3, 0),abs(radius1_3),fill=False, color="red")
                Circle2_3 = plt.Circle((center2_3, 0),abs(radius2_3),fill=False, color="blue")
                Circle1_2 = plt.Circle((center1_2, 0),abs(radius1_2),fill=False, color="green")
                if(self.isAngle_stress):
                    new_points = [[sigma_NN,sigma_NS]]
                    print(new_points)
                    ax.plot(*zip(*new_points),marker='o', color='purple', ls='')
                    # n = self.reqAngle_normal_3d[2]
                ax.add_artist(Circle1_3)
                ax.add_artist(Circle1_2)
                ax.add_artist(Circle2_3)
                ax.minorticks_on()
        elif self.ndims ==2:
            ax.set(xlim=(center1_2-(radius1_2+0.5), sigma1+0.5), ylim = (-(radius1_2+0.5), radius1_2+0.5))
            radius = [radius1_2]
            mohr_center=[[center1_2,0]]
            mohr_sigma=[[sigma1,0],[sigma2,0]]
            if(self.isAngle_stress):
                try:
                    curr_angle = np.arctan((-Stress_tensor[0][1])/(Stress_tensor[0][0]-center1_2))
                except:
                    if(Stress_tensor[0][1]>=0):
                        curr_angle = np.deg2rad(90)
                    else:
                        curr_angle = np.deg2rad(-90)
                total_angle = curr_angle + np.deg2rad(2*self.reqAngle_stress_2d)
                # print(np.rad2deg(total_angle))
                new_x_1 = radius1_2*np.cos(total_angle) + center1_2
                new_y_1 = radius1_2*np.sin(total_angle)    
                new_x_2 = radius1_2*np.cos(total_angle + np.deg2rad(180))+center1_2
                new_y_2 = radius1_2*np.sin(total_angle + np.deg2rad(180))
            if(self.isGraph):
                ax.plot(*zip(*mohr_center), marker='o', color='r', ls='')
                ax.plot(*zip(*mohr_sigma), marker='o', color='b', ls='')
                points = [[Stress_tensor[0][0],-Stress_tensor[0][1]],[Stress_tensor[1][1],Stress_tensor[0][1]]]
                ax.plot(*zip(*points),marker='o', color='black', ls='')
                ax.plot([Stress_tensor[0][0],Stress_tensor[1][1]],[-Stress_tensor[0][1],Stress_tensor[0][1]])
                if(self.isAngle_stress):
                    new_points = [[new_x_1,new_y_1],[new_x_2,new_y_2]]
                    ax.plot(*zip(*new_points),marker='o', color='black', ls='')
                    ax.plot([new_x_1,new_x_2],[new_y_1,new_y_2])
                # ax.plot()
                for i in range(len(mohr_sigma)):
                    ax.annotate("ε"+str(i+1),tuple(mohr_sigma[i]),fontsize=12)
                for i in range(len(mohr_center)):
                    ax.annotate("C"+str(i+1),tuple(mohr_center[i]),fontsize=12)
                Circle1_2 = plt.Circle((center1_2, 0),abs(radius1_2),fill=False, color="green")
                ax.add_artist(Circle1_2)
        if(self.isGraph):
            ax.minorticks_on()
            ax.set_aspect('equal', adjustable='box')

            ax.spines['bottom'].set_position('center')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            ax.grid(which='major', axis='both', linestyle ='--')
            plt.show()
            plt.close('all')
        if(self.ndims == 2):
            return mohr_center, mohr_sigma, radius ,(new_x_1, new_y_1), (new_x_2, new_y_2)
        else:
            return mohr_center, mohr_sigma, radius ,(sigma_NN, sigma_NS)
    def find_Principal_Stress(self):
        if self.σ_tensor.shape == (3,3):
            a=self.σ_tensor.copy()
            self.I1= a[0][0] + a[1][1] + a[2][2]
            self.I2= a[0][0]*a[1][1] + a[1][1]*a[2][2] + a[0][0]*a[2][2] - a[0][1]**2 - a[0][2]**2 -a[1][2]**2
            self.I3 = np.linalg.det(self.σ_tensor)
            a=np.linalg.eig(a)[0]                
            self.principal_stress=np.round(a, 4)
            return Stress_MohrCircle.Find_Mohr_Circle(self)
        elif self.σ_tensor.shape == (2,2):
            a=self.σ_tensor.copy()
            self.I1= a[0][0] + a[1][1]
            # print(a[0][1])
            self.I2= a[0][0]*a[1][1] - a[0][1]**2 
            a=np.linalg.eig(a)[0]    
            self.principal_stress=np.round(a, 4)
            return Stress_MohrCircle.Find_Mohr_Circle(self)        

    def stress_execute(self):
        # print()
        if self.ndims==2:
            self.σ_tensor = [[self.σxx , self.σxy ],
                        [self.σxy , self.σyy ]]
        else:                    
            self.σ_tensor = [[self.σxx , self.σxy , self.σzx],
                        [self.σxy , self.σyy , self.σyz],
                        [self.σzx , self.σyz , self.σzz]]
        self.σ_tensor= np.array(self.σ_tensor)
        # print(σ_tensor.shape)
        return Stress_MohrCircle.find_Principal_Stress(self)

# m = Stress_MohrCircle(σxx= 34.3, σyy= 74,σzz= 3, σxy= -83.9, σyz= 5, σzx= 6)
# m.ndims = 2
# m.isGraph = True
# # m.isAngle_stress = True
# # m.reqAngle_normal_3d = [np.cos(0), round(np.cos(0),3), np.cos(90)]
# # print(m.reqAngle_normal_3d)
# m.isAngle_stress = True
# m.reqAngle_stress_2d = 54.6
# m.stress_execute()

