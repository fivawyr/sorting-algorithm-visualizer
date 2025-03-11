// Contents: Utility functions for algorithms, such as printing arrays
#include "../include/utils.h"
#include <stdio.h>

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
