import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 4
p = 0.8
vals = [False, True]
grid = np.random.choice(vals, N*N, p=[1-p, p]).reshape(N, N)

fig, ax = plt.subplots()
mat = ax.matshow(grid)

skip = 1


def update(frame):
    if frame % skip != 0:
        return [mat]
    grid = np.random.choice(vals, N*N, p=[1-p, p]).reshape(N, N)
    mat.set_data(grid)
    return [mat]


ani = animation.FuncAnimation(fig, update, interval=10, save_count=50)


def on_press(event):
    # Quand on modifie une variable globale, il faut ajouter cette ligne
    global skip
    skip += 5


fig.canvas.mpl_connect('key_press_event', on_press)

plt.show()
