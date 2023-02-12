import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

# unit cm-1 #
def frequency(eignval):
    return (eignval/(5.892*1e-5))**0.5



def plot_mol_mode(p_list,freq,eignvec,boundary = [-0.674, 3,-1, 1]):
#def plot_mol_mode():
      
    # First set up the figure, the axis, and the plot element we want to animate
    fig, ax = plt.subplots()

    ax.set_xlim(( boundary[0], boundary[1]))
    ax.set_ylim((boundary[2],boundary[3]))

    line, = ax.plot(p_list[:,0], p_list[:,1],'ro-', lw=2)
    
    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return (line,)
    # animation function. This is called sequentially
    def animate(i):
        t = np.linspace(0, 2*np.pi, 100)
        x = np.sin(2 * np.pi * freq*1e-6*(t[i]))
        line.set_data([p_list[0,0]+x*eignvec[0],p_list[1,0]+x*eignvec[1],p_list[2,0]+x*eignvec[2]],[0,0,0])
        return (line,)
    # call the animator. blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=100, interval=50, blit=True)
    plt.close(fig)
    return HTML(anim.to_html5_video())