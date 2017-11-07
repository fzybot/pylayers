from pylayers.antprop.slab import *
import numpy as np
import matplotlib.pylab as plt
sl = SlabDB(filemat='matDB.ini',fileslab='slabDB.ini')
sl.mat.add(name='ConcreteJc',cval=3.5,alpha_cmm1=1.9,fGHz=120,typ='THz')
sl.mat.add(name='GlassJc',cval=2.55,alpha_cmm1=2.4,fGHz=120,typ='THz')
sl.add('ConcreteJc',['ConcreteJc'],[0.049])
sl.add('DoubleGlass',['GlassJc','AIR','GlassJc'],[0.0029,0.0102,0.0029])
theta = np.linspace(20,60,100)*np.pi/180
sl['ConcreteJc'].eval(120,theta)
f,a=sl['ConcreteJc'].plotwrt(var='a',typ=['l20'])
fig = plt.figure()
sl['DoubleGlass'].eval(120,theta)
f,a = sl['DoubleGlass'].plotwrt(var='a',typ=['l20'])
freq = np.linspace(110,135,50)
fig = plt.figure()
sl['DoubleGlass'].eval(freq,theta)
sl['DoubleGlass'].pcolor(dB=True)
