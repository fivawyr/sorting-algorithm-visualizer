#include <stdio.h>
#include "../include/bubble_sort.h"
#include "../include/merge_sort.h"
#include "../include/quick_sort.h"
#include "../include/insertion_sort.h"
#include "../include/selection_sort.h"

void print_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {

    int arr1[] = {64, 34, 25, 12, 22, 11, 90};
    int n1 = sizeof(arr1)/sizeof(arr1[0]);

    int arr2[] = {5, 1, 4, 2, 8};
    int n2 = sizeof(arr2)/sizeof(arr2[0]);

    printf("Testing Insertion Sort:\n");
    int insertion_test[] = {64, 34, 25, 12, 22, 11, 90};
    insertion_sort(insertion_test, n1);
    print_array(insertion_test, n1);



    printf("Testing Quick Sort:\n");
    int quick_test[] = {64, 34, 25, 12, 22, 11, 90};
    quick_sort(quick_test, n1);  // Korrekter Aufruf mit zwei Parametern
    print_array(quick_test, n1);

    printf("Testing Selection Sort:\n");
    int selection_test[] = {64, 34, 25, 12, 22, 11, 90};
    selection_sort(selection_test, n1);
    print_array(selection_test, n1);

    return 0;
}


