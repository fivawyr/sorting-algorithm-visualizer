// C program for implementation of Selection sort
#include "../include/selection_sort.h"
#include "../include/utils.h"
#include <stdio.h>

void selection_sort(int arr[], int n,  void (*callback)(int*, int)) {
    int i, j, min_idx;
    
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;

        for (j = i + 1; j < n; j++) {
            if(arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        int tmp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = tmp;

        if (callback != NULL) {
            callback(arr, n);
        }
    }
}




