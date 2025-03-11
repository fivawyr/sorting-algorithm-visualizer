# c_interface.py

import ctypes
import os
import time
from draw import draw_array  
from shared import abort_flag


global_vars = {
    "canvas": None,
    "speed": 0.5
}


# Load the shared library
if os.name == "nt":  # Windows
    lib_path = "../lib/algorithms.dll"
else:  # Linux/macOS
    lib_path = "../lib/algorithms.so"

lib = ctypes.CDLL(lib_path)


Callback = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int), ctypes.c_int)
"""
This file contains the C interface for the sorting algorithms.
"""    

def callback(arr_ptr, n):
    """
    This function is called by the C code to update the array on the canvas.
    :param arr_ptr: The pointer to the array.
    :param n: The length of the array.
    """
    arr = list(arr_ptr)
    draw_array(global_vars["canvas"], arr)
    time.sleep(global_vars["speed"])


lib.bubble_sort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, Callback]
lib.bubble_sort.restype = None
# Define the argument types and return type of the bubble_sort function

lib.merge_sort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, Callback]
lib.merge_sort.restype = None
# ... merge_sort function

lib.quick_sort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, Callback]
lib.quick_sort.restype = None
# ... quick_sort function

lib.insertion_sort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, Callback]
lib.insertion_sort.restype = None
# ... insertion_sort function

lib.selection_sort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, Callback]
lib.selection_sort.restype = None
# ... selection_sort function


def convert_array(arr):
    """
    This function converts a Python list to a C array.
    :param arr: The Python list.
    :return: The C array and its length.
    """
    n = len(arr)
    arr_c = (ctypes.c_int * n)(*arr)
    return arr_c, n


def bubble_sort(arr, canvas, speed):
    """
    This function sorts the array using the bubble sort algorithm."
    """
    global_vars["canvas"] = canvas
    global_vars["speed"] = speed
    arr_c, n = convert_array(arr)
    lib.bubble_sort(arr_c, n, Callback(callback))
    return list(arr_c)

def merge_sort(arr, canvas, speed):
    """
    ... merge_sort function
    """
    global_vars["canvas"] = canvas
    global_vars["speed"] = speed
    arr_c, n = convert_array(arr)
    lib.merge_sort(arr_c, n, Callback(callback))
    return list(arr_c)

def quick_sort(arr, canvas, speed):
    """
    ... quick_sort function
    """
    global_vars["canvas"] = canvas
    global_vars["speed"] = speed
    arr_c, n = convert_array(arr)
    lib.quick_sort(arr_c, n, Callback(callback))
    return list(arr_c)

def insertion_sort(arr, canvas, speed):
    """
    ... insertion_sort function
    """
    global_vars["canvas"] = canvas
    global_vars["speed"] = speed
    arr_c, n = convert_array(arr)
    lib.insertion_sort(arr_c, n, Callback(callback))
    return list(arr_c)

def selection_sort(arr, canvas, speed):
    """
    ... selection_sort function
    """
    global_vars["canvas"] = canvas
    global_vars["speed"] = speed
    arr_c, n = convert_array(arr)
    lib.selection_sort(arr_c, n, Callback(callback))
    return list(arr_c)

def callback(arr_ptr, n):
    """
    This function is called by the C code to update the array on the canvas.
    """
    arr = list(arr_ptr)
    draw_array(global_vars["canvas"], arr)
    time.sleep(global_vars["speed"])