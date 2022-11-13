import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 4
p = 0.8
vals = [False, True]
grid = np.random.choice(vals, N*N, p=[1-p, p]).reshape(N, N)

fig, ax = plt.subplots()
mat = ax.matshow(grid)

last_key_pressed = None

figtext = plt.figtext(0.5, 0.01, "", wrap=True,
                      horizontalalignment='center', fontsize=12)


def update(frame):
    figtext.set_text(f"Frame: {frame}. Last key pressed: {last_key_pressed}")
    grid = np.random.choice(vals, N*N, p=[1-p, p]).reshape(N, N)
    mat.set_data(grid)
    return [mat]


ani = animation.FuncAnimation(fig, update, interval=10, save_count=50)


def on_press(event):
    # Quand on modifie une variable globale, il faut ajouter cette ligne
    global last_key_pressed
    last_key_pressed = event.key
    return event


fig.canvas.mpl_connect('key_press_event', on_press)

plt.show()
