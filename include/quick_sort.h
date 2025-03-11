// header file for quick_sort.c
#ifndef QUICK_SORT_H
#define QUICK_SORT_H

void quick_sort(int arr[], int n, void (*callback)(int*, int));  
int partition(int arr[], int low, int high);

#endif