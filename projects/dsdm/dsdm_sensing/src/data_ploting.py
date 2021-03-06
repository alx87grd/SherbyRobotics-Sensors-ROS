#!/usr/bin/env python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


#data = np.array([[ self.q , self.dq , self.q_d , self.f , self.k , t, self.w1 , self.w2 , self.i1 , self.i2 , self.brake ]])


## LOADING


#name      = '1dof_loaded_D15'

name      = '/home/alex/ROS_WS/src/dsdm_robotics/dsdm_sensing/data/' + name + '.npy'

DATA = np.load( name )

i = 1 + 500 * 1.470
j = i + 500 * 4

## DEOCODING
q  = DATA[i:j,0]
dq = DATA[i:j,1]
qd = DATA[i:j,2]
f  = DATA[i:j,3]
k  = DATA[i:j,4]
t  = DATA[i:j,5] - DATA[i,5] 
w1 = DATA[i:j,6] 
w2 = DATA[i:j,7]  
i1 = DATA[i:j,8] 
i2 = DATA[i:j,9]
b  = DATA[i:j,10] / 255.
id1= DATA[i:j,11] 
id2= DATA[i:j,12]
wr1= DATA[i:j,13] 
wr2= DATA[i:j,14]


## Figures

def plot_main():

    fontsize = 5
    
    matplotlib.rc('xtick', labelsize=fontsize )
    matplotlib.rc('ytick', labelsize=fontsize )
    
    
    simfig , plot = plt.subplots(4, sharex=True,figsize=(5, 3),dpi=400, frameon=True)
    
    simfig.canvas.set_window_title('Closed loop trajectory')
    
    plot[0].plot( t ,  qd , 'r--', label = 'Ref. trajectory')
    plot[0].plot( t ,  q , 'b' ,  label = 'Actual position')
    plot[0].set_yticks([-3.14,0])
    plot[0].set_ylim(-5,1)
    plot[0].grid(True)
    plot[0].set_ylim(-6,1)
    legend = plot[0].legend(loc='lower right', fancybox=True, shadow=False, prop={'size':fontsize})
    legend.get_frame().set_alpha(0.4)
    
    plot[1].plot( t ,  dq , 'b')
    plot[1].set_yticks([-6,0,6])
    plot[1].set_ylim(-8,8)
    plot[1].grid(True)
    
    plot[2].plot( t ,  f , 'b')
    plot[2].set_yticks([-0.2,0,0.2])
    plot[2].set_ylim(-0.3,0.3)
    plot[2].grid(True)
    
    plot[3].plot( t ,  k * 451 + 23 , 'r')
    plot[3].set_yticks([23,474])
    plot[3].set_ylim(-100,600)
    plot[3].grid(True)
    
    plot[0].set_ylabel('Angle [rad]' , fontsize=fontsize )
    plot[1].set_ylabel('Speed [rad/sec]' , fontsize=fontsize )
    plot[2].set_ylabel('Torque [Nm]' , fontsize=fontsize )
    plot[3].set_ylabel('Gear Ratio' , fontsize=fontsize )
    
    plot[-1].set_xlabel('Time [sec]', fontsize=fontsize )
    plot[-1].set_xlim(0,4)
    plot[-1].set_xticks([0,1,2,3,4])

    simfig.tight_layout()
    
    simfig.show()
    

def plot_motors():

    fontsize = 5
    
    matplotlib.rc('xtick', labelsize=fontsize )
    matplotlib.rc('ytick', labelsize=fontsize )
    
    
    simfig , plot = plt.subplots(1, sharex=True,figsize=(4, 3),dpi=400, frameon=True)
    
    simfig.canvas.set_window_title('Motors velocity')
    
    plot.plot( t ,  w1 , 'b')
    plot.plot( t ,  w2 , 'r')
    plot.grid(True)
    
    plot.set_ylabel('Velocity [rad]/sec' , fontsize=fontsize )
    
    plot.set_xlabel('Time [sec]', fontsize=fontsize )
    
    simfig.tight_layout()
    
    simfig.show()
    
    
    
def plot_motors_raw():

    fontsize = 5
    
    matplotlib.rc('xtick', labelsize=fontsize )
    matplotlib.rc('ytick', labelsize=fontsize )
    
    
    simfig , plot = plt.subplots(1, sharex=True,figsize=(4, 3),dpi=400, frameon=True)
    
    simfig.canvas.set_window_title('Motors velocity')
    
    plot.plot( t ,  wr1 , 'b')
    plot.plot( t ,  wr2 , 'r')
    plot.grid(True)
    
    plot.set_ylabel('Velocity [rad]/sec' , fontsize=fontsize )
    
    plot.set_xlabel('Time [sec]', fontsize=fontsize )
    
    simfig.tight_layout()
    
    simfig.show()
    
    
    
def plot_shift_delay():

    fontsize = 5
    
    matplotlib.rc('xtick', labelsize=fontsize )
    matplotlib.rc('ytick', labelsize=fontsize )
    
    
    simfig , plot = plt.subplots(1, sharex=True,figsize=(4, 3),dpi=400, frameon=True)
    
    simfig.canvas.set_window_title('Motors velocity')
    
    plot.plot( t ,  wr1 * 1.57 , 'b')
    plot.plot( t ,  k   * 50  , 'r')
    plot.grid(True)
    
    plot.set_ylabel('Velocity [ticks/interval]' , fontsize=fontsize )
    plot.set_ylim(-200,150)
    
    plot.set_xlabel('Time [sec]', fontsize=fontsize )
    
    simfig.tight_layout()
    
    simfig.show()
    
    
    
def plot_currents():

    fontsize = 5
    
    matplotlib.rc('xtick', labelsize=fontsize )
    matplotlib.rc('ytick', labelsize=fontsize )
    
    
    simfig , plot = plt.subplots(1, sharex=True,figsize=(4, 3),dpi=400, frameon=True)
    
    simfig.canvas.set_window_title('Motors Currents')
    
    plot.plot( t ,  i1 , 'b')
    plot.plot( t ,  i2 , 'r')
    plot.plot( t ,  id1 , 'g.')
    plot.plot( t ,  id2 , 'c.')
    plot.grid(True)
    
    plot.set_ylabel('Currents [mA]' , fontsize=fontsize )
    
    plot.set_xlabel('Time [sec]', fontsize=fontsize )
    
    simfig.tight_layout()
    
    simfig.show()
    
    
    
plot_main()
#plot_motors()
#plot_currents()
#plot_shift_delay()
