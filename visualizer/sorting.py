#sorting.py

import c_interface  
from draw import draw_array
import time
import threading
from shared import is_sorting, abort_flag
import tkinter as tk 
import threading


sorting_thread = None


def start_sorting(array_str, algorithm, canvas, speed, sorted_array_label):
    """
    Starts the sorting process in a separate thread.

    Args:
        array_str (str): The array to be sorted as a string
        algorithm (str): The algorithm to be used for sorting
        canvas (tk.Canvas): The canvas on which the array is visualized
        speed (float): The speed at which the array is sorted
        sorted_array_label (tk.Label): The label in which the sorted array is displayed
    """
    global is_sorting, abort_flag, sorting_thread
    if is_sorting:
        return

    is_sorting = True
    abort_flag = False

    def sorting_thread_func():
        """
        The sorting process in a separate thread.
        """
        global is_sorting, abort_flag
        try:
            arr = list(map(int, array_str.split(",")))
            c_interface.global_vars["speed"] = speed

            algo_functions = {
                "Bubble Sort": bubble_sort_visualized,
                "Merge Sort": merge_sort_visualized,
                "Quick Sort": quick_sort_visualized,
                "Insertion Sort": insertion_sort_visualized,
                "Selection Sort": selection_sort_visualized
            }

            if algorithm in algo_functions:
                sorted_arr = algo_functions[algorithm](arr, canvas, speed)
                if not abort_flag:
                    draw_array(canvas, sorted_arr, is_sorted=True)
                    sorted_array_label.config(text=f"Sortiert: {sorted_arr}")

        except Exception as e:
            print(f"Fehler: {e}")
        finally:
            is_sorting = False

    sorting_thread = threading.Thread(target=sorting_thread_func)
    sorting_thread.start()


def draw_array(canvas, arr, highlight_indices=[], is_sorted=False):
    """
    Draws the array on the canvas.

    Args:
        canvas (tk.Canvas): The canvas on which the array is visualized
        arr (list): The array to be visualized
        highlight_indices (list): The indices to be highlighted
        is_sorted (bool): Whether the array is sorted
    """
    if not canvas.winfo_exists():
        return

    canvas.delete("all")
    bar_width = 800 // len(arr)
    max_height = max(arr) if max(arr) > 0 else 1

    for i, value in enumerate(arr):
        if is_sorted:
            fill_color = "green"
        elif i in highlight_indices:
            fill_color = "red"
        else:
            fill_color = "blue"

        bar_height = (value / max_height) * 380
        canvas.create_rectangle(
            i * bar_width, 400,
            (i + 1) * bar_width, 400 - bar_height,
            fill=fill_color
        )

    canvas.update_idletasks()
    canvas.after(10)  


def bubble_sort_visualized(arr, canvas, speed):
    """
    Sorts the array visually with the bubble sort algorithm as a canvas

    Args: 
        arr (list): The array to be sortedy
        canvas (tk.Canvas): The canvas on which the array is visualized
        speed (float): The speed at which the array is sorted

    Returns:
        list: The array to be sortedy

    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if j % 10 == 0:  
                draw_array(canvas, arr, highlight_indices=[j, j + 1])
                canvas.update_idletasks()
                canvas.after(int(speed * 1000))  

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                if j % 10 == 0:  
                    draw_array(canvas, arr, highlight_indices=[j, j + 1])
                    canvas.update_idletasks()
                    canvas.after(int(speed * 1000))   
    return arr


def merge_sort_visualized(arr, canvas, speed):
    """
    Sorts the array visually with the merge sort algorithm as a canvas

    Args:
        arr (list): The array to be sorted
        canvas (tk.Canvas): The canvas on which the array is visualized
        speed (float): The speed at which the array is sorted
    """
    def merge(arr, left, right, canvas, speed):
        """
        Merges the two arrays and visualizes the process. 

        Args:
            arr (list): The array to be sorted
            left (list): The left array
            right (list): The right array
            canvas (tk.Canvas): The canvas on which the array is visualized
            speed (float): The speed at which the array is sorted 
        """
        i = j = k = 0
        while i < len(left) and j < len(right):
            if k % 10 == 0:  
                draw_array(canvas, arr, highlight_indices=[k])
                canvas.update_idletasks()
                canvas.after(int(speed * 1000))  

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        draw_array(canvas, arr)
        canvas.update_idletasks()
        canvas.after(int(speed * 1000))  
        return arr

    def sort(arr, canvas, speed):
        """
        Sorts the array and visualizes the process.
        
        Args:
            arr (list): The array to be sorted
            canvas (tk.Canvas): The canvas on which the array is visualized
            speed (float): The speed at which the array is sorted
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = sort(left, canvas, speed)
        right = sort(right, canvas, speed)

        return merge(arr, left, right, canvas, speed)

    return sort(arr, canvas, speed)


def quick_sort_visualized(arr, canvas, speed):
    def partition(arr, low, high, canvas, speed):
        """
        Partitions the array for Quick Sort and visualizes the process.

        Args:
            arr (list): The array to be sorted
            low (int): The lower index of the array
            high (int): The higher index of the array
            canvas (tk.Canvas): The canvas on which the array is visualized
            speed (float): The speed at which the array is sorted
        """
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if j % 10 == 0:  
                draw_array(canvas, arr, highlight_indices=[j, high])
                canvas.update_idletasks()
                canvas.after(int(speed * 1000))   

            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                if j % 10 == 0:  
                    draw_array(canvas, arr, highlight_indices=[i, j])
                    canvas.update_idletasks()
                    canvas.after(int(speed * 1000))   

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        draw_array(canvas, arr, highlight_indices=[i + 1, high])
        canvas.update_idletasks()
        canvas.after(int(speed * 1000))   
        return i + 1


    def sort(arr, low, high, canvas, speed):
        """
        Sorts the array and visualizes the process.

        Args:
            arr (list): The array to be sorted
            low (int): The lower index of the array
            high (int): The higher index of the array
            canvas (tk.Canvas): The canvas on which the array is visualized
            speed (float): The speed at which the array is sorted
        """
        if low < high:
            pi = partition(arr, low, high, canvas, speed)
            sort(arr, low, pi - 1, canvas, speed)
            sort(arr, pi + 1, high, canvas, speed)

    sort(arr, 0, len(arr) - 1, canvas, speed)
    return arr


def insertion_sort_visualized(arr, canvas, speed):
    """
    Sorts the array visually with the insertion sort algorithm as a canvas
    
    Args:
        arr (list): The array to be sorted
        canvas (tk.Canvas): The canvas on which the array is visualized
        speed (float): The speed at which the array is sorted
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        if i % 10 == 0:  
            draw_array(canvas, arr, highlight_indices=[i])
            canvas.update_idletasks()
            canvas.after(int(speed * 1000))   

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

            if i % 10 == 0:  
                draw_array(canvas, arr, highlight_indices=[j + 1])
                canvas.update_idletasks()
                canvas.after(int(speed * 1000))   

        arr[j + 1] = key

        if i % 10 == 0:  
            draw_array(canvas, arr, highlight_indices=[j + 1])
            canvas.update_idletasks()
            canvas.after(int(speed * 1000))    
    return arr


def selection_sort_visualized(arr, canvas, speed):
    """
    Sorts the array visually with the selection sort algorithm as a canvas

    Args:
        arr (list): The array to be sorted
        canvas (tk.Canvas): The canvas on which the array is visualized
        speed (float): The speed at which the array is sorted
    """
    for i in range(len(arr)):
        min_idx = i

        if i % 10 == 0: 
            draw_array(canvas, arr, highlight_indices=[i, min_idx])
            canvas.update_idletasks()
            canvas.after(int(speed * 1000))  

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

            if i % 10 == 0: 
                draw_array(canvas, arr, highlight_indices=[j, min_idx])
                canvas.update_idletasks()
                canvas.after(int(speed * 1000))  
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        if i % 10 == 0: 
            draw_array(canvas, arr, highlight_indices=[i, min_idx])
            canvas.update_idletasks()
            canvas.after(int(speed * 1000))  
    return arr 