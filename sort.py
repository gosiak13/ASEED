import math
import numpy as np
import time
import sys

to_sort = []
rozmiar = 1000
for i in range(rozmiar):
    to_sort.append(np.random.randint(1, 5 * rozmiar))

to_sort2 = to_sort.copy()
to_sort3 = to_sort.copy()

print ('liczba elementów w tablicy: ', len(to_sort))
print()
print('tablica nieposortowana: ', to_sort)
print()

def bubble_sort(to_sort):
    for i in range (len(to_sort) - 1):
        for j in range (len(to_sort) - i -1):
             if (to_sort[j] > to_sort[j+1]):
                 to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
    return to_sort


def selection_sort(to_sort):
    i = 0
    for i in range(len(to_sort)-1):
        smallest = to_sort[i]
        for j in range(i, len(to_sort)-1):
            if to_sort[j] < smallest :
                smallest = to_sort[j] #funkcja to_sort.min() nie działała przy większych tablicach
                index_of_smallest = j
        #index_of_smallest = to_sort.index(smallest) #tak samo funkcja to_sort.index()
        to_sort[i], to_sort[index_of_smallest] = to_sort[index_of_smallest], to_sort[i]
    return to_sort


def quicksort(to_sort):
    less = []
    equal = []
    greater = []

    if len(to_sort) > 1:
        pivot = to_sort[0]
        for x in to_sort:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return quicksort(less) + equal + quicksort(greater)
    else:
        return to_sort


start = time.time()
print('Sortowanie przez wymianę: ', selection_sort(to_sort))
stop = time.time()
print("sortowanie trwa --- %s sekundy ---" % (stop - start))
print()

start = time.time()
print('Sortowanie bąbelkowe: ', bubble_sort(to_sort2))
stop = time.time()
print("sortowanie trwa --- %s sekundy ---" % (stop - start))
print()

start = time.time()
print('Sortowanie quicksort: ', quicksort(to_sort3))
stop = time.time()
print("sortowanie trwa --- %s sekundy ---" % (stop - start))

#print(do_sortu)

