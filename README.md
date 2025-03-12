# Sorting Algorithm Visualizer  

>A Python-based GUI application to visualize sorting algorithms in real-time. 

- This project demonstrates popular sorting algorithms (Bubble Sort, Merge Sort, Quick Sort, Insertion Sort, Selection Sort) with an interactive Tkinter interface. 
- It was developed as part of my current university module, Datenstrukturen, Algorithmen und Programmierung 1 (English: Data Structures, Algorithms, and Programming 1). 
- All comments are written in English to ensure international readability and maintainability.

### Code of Conduct
Please read [Code of Conduct](CODE_OF_CONDUCT.md), before submitting pull request to me, thank you very much.

### Demo

![Demo](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnZyaG9yMDUwcmtlazI2NnlvZGowMTJ4cnp2dWxyZnB3amhoaHJkZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ch1gi4xZHJgCjL0dwH/giphy.gif)  

###  Features  
- **Interactive GUI**: Adjustable speed control and random array generation.  
- **Algorithm Visualization**:  
  - Bubble Sort  
  - Merge Sort  
  - Quick Sort  
  - Insertion Sort  
  - Selection Sort  
- **Real-Time Updates**: Watch elements get sorted step-by-step.  
- **Speed Control**: Three speed settings (Slow, Medium, Fast).  

## Getting Started  

### Prerequisites  
- **Python 3.9+**: [Download Python](https://www.python.org/downloads/)  
- **Tkinter**: Included with Python (no separate installation needed).  
- **C Compiler**: Required to build the shared library (e.g., GCC for Linux/macOS, MinGW for Windows).  

### Installing  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/fivawyr/sorting-algorithm-visualizer.git  
   cd sorting-algorithm-visualizer  
2. **Compile the C library**:
    **For Linux/macOS:**
   ```bash  
    gcc -shared -o lib/algorithms.so -fPIC src/algorithms.c  
``
    **For Windows (using MinGW):**
```bash  
    gcc -shared -o lib/algorithms.dll src/algorithms.c
```
4. **Install Python dependencies**
    all python moduls (ctypes, os, time, tkinter, random, threading) are standard python bibs, no need for a requirments.txt
5. **Run the application**
    python main.py  

## Usage

1. **Input options**
    - Enter a comma-separated list (e.g., 3,1,4,2) in the text field.
    - Click "Random Array" to generate a random array.
2. **Select Algorithm**
    - Choose from the dropdown menu.
3. **Adjust Speed**
    - Use the slider to control visualization speed(3 differen levels). 
4. **Start Sorting**
    - Click "Start Sorting" to begin the visualization.

### Built With 
**-Python:** GUI, GUI logic and interface (between C and Python)
**-Tkinter:** GUI framework
**-C:** High-performance sorting algorithm implementations
**-Git:** Version control

### Author
- Finn W. [GitHub Profile](https://github.com/fivawyr) 

### Acknowledgments 
- Inspiration from my university professor, GeeksforGeeks: [Website](https://www.geeksforgeeks.org/fundamentals-of-algorithms/), @CodeWithLewis: [Youtube](https://www.youtube.com/@CodingWithLewis) 
- Special thanks to Billie Thomson for helpful and beginner friendly repositories:  [GitHub](https://gist.github.com/PurpleBooth) 
- My study group and my uni colleagues, with whom I learn together and we help each other 
