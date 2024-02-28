import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

N = 3
p = 0.8
vals = [0, 1, 2]
grid = np.random.choice(vals, (N, N), p=[0.25, 0.25, 0.5])
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap=ListedColormap(["w", "k", "r"]))

grid = np.random.choice(vals, (N, N), p=[1 - p, p, 0])
mat.set_data(grid)

last_key_pressed = None

figtext = plt.figtext(
    0.5, 0.01, "", wrap=True, horizontalalignment="center", fontsize=12
)


def update(frame):
    figtext.set_text(f"Frame: {frame}. Last key pressed: {last_key_pressed}")
    grid = np.random.choice(vals, (N, N), p=[0.25, 0.75, 0])
    print(grid)
    mat.set_data(grid)


ani = animation.FuncAnimation(fig, update, interval=100, save_count=50)


def on_press(event):
    # Quand on modifie une variable globale, il faut ajouter cette ligne
    global last_key_pressed
    last_key_pressed = event.key
    return event


fig.canvas.mpl_connect("key_press_event", on_press)

plt.show()
