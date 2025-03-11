// C program for implementation of Bubble sort
#include "../include/bubble_sort.h"
#include <stdio.h>

void bubble_sort(int arr[], int n, void (*callback)(int*, int)) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if(arr[j] > arr[j + 1]) {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;

                if (callback != NULL) {
                    callback(arr, n);
                }
            }
        } 
    }
}


