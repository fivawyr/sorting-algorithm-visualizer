# main.py

import tkinter as tk
from tkinter import ttk
from sorting import start_sorting
from shared import abort_flag
import c_interface  
import random


global root, sorting_thread
"""
This function is called when the window is closed.
It sets the abort flag, waits for the end of the thread and ends the program.
"""


def on_close():
    """
    This function is called when the window is closed.
    It sets the abort flag, waits for the end of the thread and ends the program.
    """
    global abort_flag, sorting_thread, root  
    abort_flag = True  


    if 'sorting_thread' in globals() and sorting_thread.is_alive():  
        sorting_thread.join(timeout=1.0) 

    root.quit() 
    root.destroy()  


def generate_random_array(array_entry):
    """
    This function generates a random array of 20 elements and inserts it into the array entry.
    :param array_entry: The entry field where the array should be inserted.
    """
    random_array = [random.randint(10, 100) for _ in range(20)]
    array_entry.delete(0, tk.END)
    array_entry.insert(0, ",".join(map(str, random_array)))


def get_speed(speed_value):
    """
    This function converts the speed value from the scale to a time value.
    :param speed_value: The speed value from the scale.
    :return: The time value for the speed.
    """
    speed_value = int(round(speed_value))
    if speed_value == 1:
        return 0.5  
    elif speed_value == 2:
        return 0.1  
    elif speed_value == 3:
        return 0.01  
    else:
        return 0.5  


def main():
    """
    Creates the main window and its components for the sorting visualizer.

    Components:
    - Canvas: Visualizes the array.
    - Entry field: Input for the array.
    - Random array button: Generates a random array.
    - Algorithm menu: Selects the sorting algorithm.
    - Speed scale: Controls the sorting speed.
    - Sorted array label: Displays the sorted array.
    - Start button: Begins the sorting process.

    Global variables:
    - root: Controls the main window.
    - sorting_thread: Manages the sorting thread.
    - c_interface.global_vars["canvas"]: Accesses the canvas from the sorting thread.
    - abort_flag, is_sorting: Control the sorting thread.

    Functions:
    - on_close: Handles window closure (aborts sorting and ends the program).
    - generate_random_array: Generates and displays a random array.
    - get_speed: Converts the speed scale value to a delay.
    - start_sorting: Starts the sorting thread with the selected algorithm.
    - main: Entry point of the program.
    """
    global root, sorting_thread  
    root = tk.Tk()
    root.title("Sorting Algorithm Visualizer")
    root.protocol("WM_DELETE_WINDOW", on_close)

    canvas = tk.Canvas(root, width=800, height=400, bg="white")
    canvas.pack()

    c_interface.global_vars["canvas"] = canvas  

    array_label = tk.Label(root, text="Array (comma separated):")
    array_label.pack()

    array_entry = tk.Entry(root)
    array_entry.pack()

    random_button = tk.Button(root, text="Random Array", command=lambda: generate_random_array(array_entry))
    random_button.pack()

    algorithm_label = tk.Label(root, text="Choose an Algorithm :")
    algorithm_label.pack()

    algorithm_var = tk.StringVar(value="Bubble Sort")
    algorithm_menu = tk.OptionMenu(root, algorithm_var, "Bubble Sort", "Merge Sort", "Quick Sort", "Insertion Sort", "Selection Sort")
    algorithm_menu.pack()

    speed_label = tk.Label(root, text="Speed:")
    speed_label.pack()

    speed_scale = ttk.Scale(root, from_=1, to=3, orient="horizontal")
    speed_scale.set(1)  
    speed_scale.pack()

    sorted_array_label = tk.Label(root, text="Sorted Array: ")
    sorted_array_label.pack()

    start_button = tk.Button(root, text="Start Sorting", command=lambda: start_sorting(array_entry.get(), algorithm_var.get(), canvas, get_speed(speed_scale.get()), sorted_array_label))
    start_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
    