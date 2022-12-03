from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Plotter')
root.geometry("400x200")


def plot():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.polar(house_prices)
    plt.show()


my_button = Button(root, text='Plot', command=plot)
my_button.pack()

root.mainloop()
