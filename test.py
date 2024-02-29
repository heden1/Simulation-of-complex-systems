import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def update_plot():
    mean = slider_mean.get()
    std_dev = slider_std_dev.get()

    x = np.linspace(-10, 10, 1000)
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

    ax.clear()
    ax.plot(x, y, linewidth=2, color='blue')
    ax.set_title('Gaussian Bell Curve')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    canvas.draw()

root = tk.Tk()
root.title("Gaussian Bell Curve Generator")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

slider_mean = tk.Scale(root, from_=-5, to=5, resolution=0.1, label="Mean",
                        orient=tk.HORIZONTAL, command=update_plot)
slider_mean.pack()

slider_std_dev = tk.Scale(root, from_=0.1, to=5, resolution=0.1, label="Standard Deviation",
                          orient=tk.HORIZONTAL, command=update_plot)
slider_std_dev.pack()

update_plot()

root.mainloop()