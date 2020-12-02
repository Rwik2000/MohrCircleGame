import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
from MohrCircle_stress import Stress_MohrCircle
# reqAngle = 30
# isAngle = True

class tut_Stress_MohrCircle():
    def __init__(self, σxx,σyy,σxy,σzz = 0,σyz = 0,σzx = 0, angle1= None,angle2 = None,angle3 = None):
        self.σxx = σxx
        self.σyy = σyy
        self.σzz = σzz
        self.σxy = σxy
        self.σyz = σyz
        self.σzx = σzx
        self.angle2d = angle1
        self.angle1, self.angle2,  self.angle3 = angle1, angle2, angle3 
        # self.angle1, self.angle2, self.angle2 = np.cos(np.deg2rad(angle1)), np.cos(np.deg2rad(angle2)), np.cos(np.deg2rad(angle3))
        # self.angle3d = [np.cos(np.deg2rad(angle1)),np.cos(np.deg2rad(angle2)),np.cos(np.deg2rad(angle3))]
        self.ndims = 3
    def _plot(self, ax):
            ax.minorticks_on()
            ax.set_aspect('equal', adjustable='box')
            ax.spines['bottom'].set_position('center')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            ax.grid(which='major', axis='both', linestyle ='--')
            plt.show()
    def _calc_mohr(self):
            mohr_circle = Stress_MohrCircle(self.σxx, self.σyy,self.σxy, self.σzz,self.σyz,self.σzx)
            if(self.angle2d!=None and self.ndims==2):
                print("yes")
                mohr_circle.isAngle_stress = True
                mohr_circle.reqAngle_stress_2d = self.angle2d
            elif(self.ndims==3 and self.angle1!=None and self.angle2!=None):
                l,m,n= np.cos(np.deg2rad(self.angle1)), np.cos(np.deg2rad(self.angle2)), np.cos(np.deg2rad(self.angle3))
                mohr_circle.isAngle_stress = True
                l,m,n = round(l,3),round(m,3),round(n,3)
                mohr_circle.reqAngle_normal_3d = list([l,m,n])
            mohr_circle.ndims = self.ndims
            return mohr_circle.stress_execute()
    def plot_cent(self):
        if(self.ndims == 2):
            mohr_cent,_,_,_,_ = self._calc_mohr()
            _,ax = plt.subplots()
            ax.plot(*zip(*mohr_cent), marker='o', color='r', ls='')
            init_pts = [[self.σxx, self.σyy],[-self.σxy,self.σxy]]
            ax.plot(*zip(init_pts), marker = 'o', color='b', ls='')
            ax.plot([self.σxx,self.σyy],[-self.σxy,self.σxy])
            self._plot(ax)
        else:
            mohr_cent,mohr_sigma,_,_ = self._calc_mohr()
            _,ax = plt.subplots()
            ax.plot(*zip(*mohr_cent), marker='o', color='r', ls='')
            ax.plot(*zip(*mohr_sigma), marker = 'o', color='b', ls='')
            self._plot(ax)

    def plot_init_pts(self):
        if(self.ndims)==2:
            _,ax = plt.subplots()
            init_pts = [[self.σxx, self.σyy],[-self.σxy,self.σxy]]
            ax.plot(*zip(init_pts), marker = 'o', color='b', ls='')
            self._plot(ax)

    def plot_circle(self):
        if(self.ndims==2):
            mohr_cent,mohr_sigma,radius,_,_ = self._calc_mohr()
            _,ax = plt.subplots()
            ax.plot(*zip(*mohr_cent), marker='o', color='r', ls='')
            ax.plot(*zip(*mohr_sigma),marker='o', color='black', ls='')
            init_pts = [[self.σxx, self.σyy],[-self.σxy,self.σxy]]
            ax.plot(*zip(init_pts), marker = 'o', color='b', ls='')
            ax.plot([self.σxx,self.σyy],[-self.σxy,self.σxy])
            Circle1_2 = plt.Circle(tuple(mohr_cent[0]), abs(radius[0]), fill= False, color='green')
            ax.add_artist(Circle1_2)
            ax.set(xlim=((mohr_cent[0][0]-radius[0]-0.5), mohr_sigma[0][0]+0.5), ylim = (-(radius[0]+0.5), radius[0]+0.5))
            self._plot(ax)
    def plot_angle2d(self):
        if(self.ndims==2):
            mohr_cent,mohr_sigma,radius,new1,new2 = self._calc_mohr()
            _,ax = plt.subplots()
            fin_pts = [[new1[0],new1[1]],[new2[0],new2[1]]]
            ax.plot(*zip(*fin_pts), marker='o', color='orange', ls='')
            ax.plot([new1[0],new2[0]],[new1[1],new2[1]])
            print(fin_pts)


            ax.plot(*zip(*mohr_cent), marker='o', color='r', ls='')
            ax.plot(*zip(*mohr_sigma),marker='o', color='black', ls='')
            init_pts = [[self.σxx, self.σyy],[-self.σxy,self.σxy]]
            ax.plot(*zip(init_pts), marker = 'o', color='b', ls='')
            ax.plot([self.σxx,self.σyy],[-self.σxy,self.σxy])
            Circle1_2 = plt.Circle(tuple(mohr_cent[0]), abs(radius[0]), fill= False, color='green')
            ax.add_artist(Circle1_2)
            ax.set(xlim=((mohr_cent[0][0]-radius[0]-0.5), mohr_sigma[0][0]+0.5), ylim = (-(radius[0]+0.5), radius[0]+0.5))
            self._plot(ax)
    def get_I_values(self):
        a  = [[self.σxx , self.σxy , self.σzx],
              [self.σxy , self.σyy , self.σyz],
              [self.σzx , self.σyz , self.σzz]]
        I1 = a[0][0] + a[1][1] + a[2][2]
        i2 = a[0][0]*a[1][1] + a[1][1]*a[2][2] + a[0][0]*a[2][2] - a[0][1]**2 - a[0][2]**2 -a[1][2]**2
        I3 = np.linalg.det(a)
        return I1,i2,I3
    def get_princip_values(self):
        a  = [[self.σxx , self.σxy , self.σzx],
              [self.σxy , self.σyy , self.σyz],
              [self.σzx , self.σyz , self.σzz]]
        a = np.linalg.eig(a)[0]
        a = np.round(a, 4)
        return a
    def plot_circle_3d(self):
        mohr_circle = Stress_MohrCircle(self.σxx, self.σyy,self.σxy, self.σzz,self.σyz,self.σzx)
        mohr_circle.isGraph = True
        mohr_circle.stress_execute()
# m = tut_Stress_MohrCircle(1,1,1,1,1,1)
# m.ndims = 3
# m.plot_circle_3d()