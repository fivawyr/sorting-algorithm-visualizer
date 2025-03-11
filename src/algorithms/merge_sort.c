// C program for implementation of Merge sort
#include "../include/merge_sort.h"
#include "../include/utils.h"
#include <stdio.h>
#include <stdlib.h>

void merge_sort(int arr[], int n, void (*callback)(int*, int)) {

    if (n > 1) {
        int mid = n / 2;
        int left[mid];
        int right[n - mid];

        for (int i = 0; i < mid; i++) {
            left[i] = arr[i];
        }
        for (int i = mid; i < n; i++) {
            right[i - mid] = arr[i];
        }

        merge_sort(left, mid, callback);
        merge_sort(right, n - mid, callback);

        int i = 0, j = 0, k = 0;
        while (i < mid && j < n - mid) {
            if (left[i] < right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }

        while (i < mid) {
            arr[k++] = left[i++];
        }
        while (j < n - mid) {
            arr[k++] = right[j++];
        }

        if (callback != NULL) {
            callback(arr, n);
        }
    }
}

