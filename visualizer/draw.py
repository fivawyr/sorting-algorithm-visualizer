# draw.py

def draw_array(canvas, arr, highlight_indices=[], is_sorted=False):
    """
    This function draws the array on the canvas.

    :param canvas: The canvas where the array should be drawn.
    :param arr: The array that should be drawn.
    :param highlight_indices: The indices that should be highlighted.
    :param is_sorted: A flag that indicates if the array is sorted.
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

