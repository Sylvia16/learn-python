#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Sylvia'

'''二分法'''
def binarysearch(array, target):
    if len(array) <= 0:
        return False
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (low + high) / 2
        if array[middle] > target:
            low = middle + 1
        elif array[middle] < target:
            high = middle - 1
        else:
            return True

'''快排 分治法(Divide-and-ConquerMethod)'''
def quicksort(array, left, right):
    if len(array) <= 1:
        return array

    if left < right:
        index = partition(array, left, right)
        quicksort(array, left, index-1)
        quicksort(array, index+1, right)
    return array

def partition(arr, left, right):
    #找基准
    index = left
    pivot = arr[left]
    while (left < right):
        while (left < right and arr[right] >= pivot):
            right -= 1
        arr[left] = arr[right]
        while (left < right and arr[left] <= pivot):
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot
    return left


if __name__ == '__main__':
    #考虑极值
    # array = [ 9, 1, 3, 3, 5, 7, 8]
    array = [ 5 ]
    target = 5
    if len(array) <= 0:
        result = False
    ordered_array = quicksort(array, 0, len(array)-1)
    result = binarysearch(ordered_array, target)
    print result
