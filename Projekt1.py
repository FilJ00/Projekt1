import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

A = 1
L = 20
m = 1
w = 2*np.pi
n = 1
Ft = 5
mi = m/L
V = np.sqrt(Ft/mi)
x = np.linspace(0,L,num=101)
l = (2*L)/n
t = np.linspace(0,10,num=101)
print(t)
print(type(t))
def y(Amp, Lgh, wl, pul, tm):
    return 2*Amp*np.sin((2*np.pi*Lgh)/wl)*np.cos(pul*tm)

fig,ax = plt.subplots()
line, = ax.plot(x,y(A,x,l,w,t))
ax.grid(True)
fig.subplots_adjust(bottom=0.25)
axdeg = fig.add_axes([0.25, 0.1, 0.65, 0.03])
time_slider = Slider(
    ax=axdeg,
    label='Czas [s]',
    valmin=0,
    valmax=L,
    valinit=0)


def update(val):
    line.set_ydata(y(A, x, l, w, time_slider.val))


fig.canvas.draw_idle()
time_slider.on_changed(update)
plt.show()