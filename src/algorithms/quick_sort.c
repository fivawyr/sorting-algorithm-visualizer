// C program for implementation of Quick sort
#include "../include/quick_sort.h"

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;

            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return (i + 1);
}

void quick_sort_helper(int arr[], int low, int high) {
    // quick_sort_helper is a helper function for quick_sort
    // It sorts the array in ascending order
    if (low < high) {
        int pi = partition(arr, low, high);
        quick_sort_helper(arr, low, pi - 1);
        quick_sort_helper(arr, pi + 1, high);
    }
}

void quick_sort(int arr[], int n, void (*callback)(int*, int)) {
    quick_sort_helper(arr, 0, n - 1);  
    if (callback != NULL) {
        callback(arr, n);
    }
}
