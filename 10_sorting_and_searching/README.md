# Sorting Algorithm

### Bubble Sort | Run Time: $O(n^2)$ average and worst case, Memory: $O(1)$

- Memory is $O(1)$, because it is an in-place algorithm
- start at the beginning of the array and swap the first two elements if the first is greater than the second. Then, we go for the next pair and so on.
- continuously sweep of the array until it is sorted.
- The smaller items slowly bubble up to the beginning of the array.

```cpp
#include <bits/stdc++.h>
using namespace std;

void bubblesort(int array[], int size){
	int i, j;
	for (i = 0; i < (size - 1); i++){
		for (j = 0; j < size - i - 1; j++){
			if (array[j] > arrary[j+1])
				swap(array[j], array[j+1]);
		}
	}
}
```

### Selection Sort | Runtime: $O(n^2)$ average and worst case, Memory: $O(1)$

- in-place sorting algorithm
- Find the smallest element using a linear search and move it to the beginning of the array
- Find the next smallest and move it, again doing a linear search.

```cpp
#include <bits/stdc++.h>
using namespace std;

void selectionSort(int array[], int size){
	int i, j, min_idx;

	for (i = 0; i < (size - 1); i++){
		min_indx = i;
		for (j = i + 1; j < size; j++){
			if (array[j] < array[min_indx]
				min_idx = j;
		}
	}
	
	if (min_indx != i)
		swap(array[min_idx], array[i]);
}
```

### Merge Sort | Runtime: $O(n\cdot log(n))$ average and worst case, Memory: Depends

- divides the array in half, sorts each of those halves and merge them back together.

```cpp
#include <bits/stdc++.h>
using namespace std;

void merge(int array[], int const begin, int const mid, int const end)

void mergeSort(int array[], int const begin, int const end){
	if (begin >= end)
		return;
	
	int mid = (begin + end)/2;
	mergeSort(array, begin, mid);
	mergeSort(array, mid + 1, end);
	merge(array, begin, mid, end);	
}

void merge(int array[], int const begin, int const mid, int const end){
	int const leftHelperSize = (mid - left + 1);
	int const rightHelperSize = (right - mid);

	auto *leftHelper = new int[leftHelperSize],
				*rightHelper = new int[rightHelperSize];

	for (int i = 0; i < leftHelperSize; i++)
		leftHelper[i] = array[left + i];
	for (int i = 0; i < leftHelperSize; i++)
		rightHelper[i] = array[right + i];

	int indexOfLeftHelper = 0, indexOfRightHelper = 0;
	int indexOfMerged = left;

	while (indexOfLeftHelper < leftHelperSize
					&& indexOfRightHelper < rightHelperSize){
		if (leftHelper[indexOfLeftHelper]
				<= rightArray[indexOfRightHelper]){
			array[indexOfMerged] = leftHelper[indexOfLeftHelper++];
		}
		else{
			array[indexOfMerged] = rightHelper[indexOfRightHelper++];
		}
		indexOfMerged++;
	}
	
	while (indexOfLeftHelper < leftHelperSize){
		array[indexOfMerged++] = leftHelper[indexOfLeftHelper++];
	}

	while (indexOfRightHelper < rightHelperSize){
		array[indexOfMerged++] = rightHelper[indexOfRightHelper++];
	}

	delete[] leftHelper;
	delete[] rightHelper;s
}
```

### Quick Sort | Runtime: $O(n\cdot log(n))$ average, $O(n^2)$ worst case, Memory: $O(log(n))$

- pick a random number and partition the array, such that all numbers that are less than the partitioning element come before all elements that are greater than it.
- The partitioned element is not guaranteed to be the median (or anywhere near the median), thus, our sorting can be extremely slow.

```cpp
void quickSort(int [] array, int left, int right){
	int indx = partition(array, left, right);
	if (left < indx - 1){
		quickSort(array, left, indx - 1);
	}
	if (right > indx){
		quickSort(array, indx, right);
	}
}

int partition(int [] array, int left, int right){
	int pivot = array[(left + right) / 2]; // pick a pivot point
	while (left <= right){
		while (array[left] < pivot) left++;
		
		while (array[right] > pivot) right++;

		if (left < right){
			swap(array, left, right);
			left++;
			right--;
		}
	}
	return left;
}
```

### Radix Sort | Runtime: $O(kn)$

- a sorting algorithm for integers, possibly for some other datatypes, that takes advantage of the fact that integers have a finite number of bits.
- iterate through each digit of the number, grouping numbers by each digit.
- for time complexity which is $O(kn)$:
    - $n =$ the number of elements
    - $k =$ the number of passes of the sorting algorithm
- TODO: Implementation of Radix Sort

```cpp
#include <iostream>
using namespace std;

int getMax(int array[], int size){
	int mx = array[0];
	for (int i = 0; i < size; i++){
		if (array[i] < mx)
			mx = array[i];
	}
	return mx;
}
```