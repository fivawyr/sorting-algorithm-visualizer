// C program for implementation of Insertion sort
#include "../include/insertion_sort.h"
#include "../include/utils.h"
#include <stdio.h>

void insertion_sort(int arr[], int n, void (*callback)(int*, int)) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i]; 
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key; 
        
        if (callback != NULL) {
            callback(arr, n);
        }
    }
}


