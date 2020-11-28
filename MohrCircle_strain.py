import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
# reqAngle = 30
# isAngle = True

class Strain_MohrCircle():
    def __init__(self, 𝜏xx,𝜏yy,𝜏xy,𝜏zz = 0,𝜏yz = 0,𝜏zx = 0):
        self.𝜏xx = 𝜏xx
        self.𝜏yy = 𝜏yy
        self.𝜏zz = 𝜏zz
        self.𝜏xy = 𝜏xy
        self.𝜏yz = 𝜏yz
        self.𝜏zx = 𝜏zx
        self.ndims = 3
        self.isGraph = False
        self.isAngle_strain = False
        self.reqAngle_strain_2d = None
        self.reqAngle_normal_3d = [0,0,0]
    def Find_Mohr_Circle(self):
        # global isAngle, reqAngle
        Strain = list(self.principal_strain)
        Strain_tensor = self.𝜏_tensor
        # print(Strain)
        Strain.sort(reverse=True)
        tau1=Strain[0]
        tau2=Strain[1]
        centre1_2=round((tau1+tau2)/2, 4)
        radius1_2=abs(tau2-centre1_2)
        if self.ndims==3:
            tau3=Strain[2]        
            centre1_3=round((tau1+tau3)/2, 4)
            centre2_3=round((tau2+tau3)/2, 4)    
            radius1_3=abs(tau3-centre1_3)    
            radius2_3=abs(tau2-centre2_3)
            print("The Principal Straines are: \n𝜏1: {0} \n𝜏2: {1} \n𝜏3: {2} \n".format(tau1,tau2,tau3))
            print("Maximum Shear Strain τ_max: " +str(round((tau1-tau3)/2, 3)))
            print("\nThe Centres of the circle are: \nC1: {0} \nC2: {1} \nC3: {2} \n".format(centre1_3,centre1_2,centre2_3))
        else:
            print("The Principal Straines are: \n𝜏1: {0} \n𝜏2: {1} \n".format(tau1,tau2))
            print("Maximum Shear Strain τ_max: " +str(round((tau1-tau2)/2, 3))) 
            print("\nThe Centre of the circle are: \nC1: {0}".format(centre1_2))           

        

        _, ax = plt.subplots()
        if self.ndims == 3:
            ax.set(xlim=(centre1_3-(radius1_3+0.5), tau1+0.5), ylim = (-(radius1_3+1), radius1_3+1))
            mohr_centre=[[centre1_3,0],[centre2_3,0],[centre1_2,0]]
            mohr_tau=[[tau1,0],[tau2,0],[tau3,0]]
            if(self.isGraph):
                ax.plot(*zip(*mohr_centre), marker='o', color='r', ls='')
                ax.plot(*zip(*mohr_tau), marker='o', color='b', ls='')
                for i in range(len(mohr_tau)):
                    ax.annotate("𝜏"+str(i+1),tuple(mohr_tau[i]),fontsize=12)
                for i in range(len(mohr_centre)):
                    ax.annotate("C"+str(i+1),tuple(mohr_centre[i]),fontsize=12)

                Circle1_3 = plt.Circle((centre1_3, 0),abs(radius1_3),fill=False, color="red")
                Circle2_3 = plt.Circle((centre2_3, 0),abs(radius2_3),fill=False, color="blue")
                Circle1_2 = plt.Circle((centre1_2, 0),abs(radius1_2),fill=False, color="green")
                print(self.isAngle_strain)
                if(self.isAngle_strain):
                    l = self.reqAngle_normal_3d[0]
                    m = self.reqAngle_normal_3d[1]
                    n2 = 1 - l**2 - m**2
                    print(l,m,n2)
                    if(n2<0):
                        print("Invalid Angle input!!!!!")
                        raise ValueError('Bad input!')
                    # else:
                    n = np.sqrt(n2)
                    tau_NN = (l**2)*tau1 + (m**2)*tau2 + (n**2)*tau3
                    tau_NS = np.sqrt((l**2)*tau1**2 + (m**2)*tau2**2 + (n**2)*tau3**2 - tau_NN**2)
                    new_points = [[tau_NN,tau_NS]]
                    print(new_points)
                    ax.plot(*zip(*new_points),marker='o', color='purple', ls='')
                    # n = self.reqAngle_normal_3d[2]
                ax.add_artist(Circle1_3)
                ax.add_artist(Circle1_2)
                ax.add_artist(Circle2_3)
                ax.minorticks_on()
        elif self.ndims ==2:
            ax.set(xlim=(centre1_2-(radius1_2+0.5), tau1+0.5), ylim = (-(radius1_2+0.5), radius1_2+0.5))
            mohr_centre=[[centre1_2,0]]
            mohr_tau=[[tau1,0],[tau2,0]]
            if(self.isGraph):
                ax.plot(*zip(*mohr_centre), marker='o', color='r', ls='')
                ax.plot(*zip(*mohr_tau), marker='o', color='b', ls='')
                points = [[Strain_tensor[0][0],Strain_tensor[0][1]],[Strain_tensor[1][1],-Strain_tensor[0][1]]]
                ax.plot(*zip(*points),marker='o', color='black', ls='')
                ax.plot([Strain_tensor[0][0],Strain_tensor[1][1]],[Strain_tensor[0][1],-Strain_tensor[0][1]])
                if(self.isAngle_strain):
                    try:
                        curr_angle = np.arctan((Strain_tensor[0][1])/(Strain_tensor[0][0]-centre1_2))
                    except:
                        if(Strain_tensor[0][1]>=0):
                            curr_angle = np.deg2rad(90)
                        else:
                            curr_angle = np.deg2rad(-90)
                    total_angle = curr_angle + np.deg2rad(self.reqAngle_strain_2d)
                    # print(np.rad2deg(total_angle))
                    new_x_1 = radius1_2*np.cos(total_angle) + centre1_2
                    new_y_1 = radius1_2*np.sin(total_angle)    
                    new_x_2 = radius1_2*np.cos(total_angle + np.deg2rad(180))+centre1_2
                    new_y_2 = radius1_2*np.sin(total_angle + np.deg2rad(180))
                    new_points = [[new_x_1,new_y_1],[new_x_2,new_y_2]]
                    ax.plot(*zip(*new_points),marker='o', color='black', ls='')
                    ax.plot([new_x_1,new_x_2],[new_y_1,new_y_2])
                ax.plot()
                for i in range(len(mohr_tau)):
                    ax.annotate("𝜏"+str(i+1),tuple(mohr_tau[i]),fontsize=12)
                for i in range(len(mohr_centre)):
                    ax.annotate("C"+str(i+1),tuple(mohr_centre[i]),fontsize=12)
                Circle1_2 = plt.Circle((centre1_2, 0),abs(radius1_2),fill=False, color="green")
                ax.add_artist(Circle1_2)
        if(self.isGraph):
            ax.minorticks_on()
            ax.set_aspect('equal', adjustable='box')
            ax.spines['bottom'].set_position('center')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            ax.grid(which='major', axis='both', linestyle ='--')
            plt.show()

        return mohr_centre
    def find_Principal_Strain(self):
        if self.𝜏_tensor.shape == (3,3):
            a=self.𝜏_tensor.copy()
            self.I1= a[0][0] + a[1][1] + a[2][2]
            self.I2= a[0][0]*a[1][1] + a[1][1]*a[2][2] + a[0][0]*a[2][2] - a[0][1]**2 - a[0][2]**2 -a[1][2]**2
            self.I3 = np.linalg.det(self.𝜏_tensor)
            a=np.linalg.eig(a)[0]                
            self.principal_strain=np.round(a, 4)
            return Strain_MohrCircle.Find_Mohr_Circle(self)
        elif self.𝜏_tensor.shape == (2,2):
            a=self.𝜏_tensor.copy()
            self.I1= a[0][0] + a[1][1]
            # print(a[0][1])
            self.I2= a[0][0]*a[1][1] - a[0][1]**2 
            a=np.linalg.eig(a)[0]    
            self.principal_strain=np.round(a, 4)
            return Strain_MohrCircle.Find_Mohr_Circle(self)        

    def strain_execute(self):
        # print()
        if self.ndims==2:
            self.𝜏_tensor = [[self.𝜏xx , self.𝜏xy ],
                        [self.𝜏xy , self.𝜏yy ]]
        else:                    
            self.𝜏_tensor = [[self.𝜏xx , self.𝜏xy , self.𝜏zx],
                        [self.𝜏xy , self.𝜏yy , self.𝜏yz],
                        [self.𝜏zx , self.𝜏yz , self.𝜏zz]]
        self.𝜏_tensor= np.array(self.𝜏_tensor)
        # print(𝜏_tensor.shape)
        return Strain_MohrCircle.find_Principal_Strain(self)

# m = Strain_MohrCircle(𝜏xx= 1, 𝜏yy= 2,𝜏zz= 3, 𝜏xy= 4, 𝜏yz= 5, 𝜏zx= 6)
# m.ndims = 3
# m.isGraph = True
# m.isAngle_strain = True
# m.reqAngle_normal_3d = [np.cos(0), round(np.cos(0),3), np.cos(90)]
# print(m.reqAngle_normal_3d)
# # m.isAngle_strain = True
# # m.reqAngle_strain_2d = 45
# m.strain_execute()

