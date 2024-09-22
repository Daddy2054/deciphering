## Task0
*Description**: The problem involves retrieving the record from the dataset.

**Approach**: Directly accessing the first and last elements of the arrays using indexing.

**Complexity Analysis**:
- **Algorithm**: Directly accessing elements of the array once.
- **Big O Notation**: $O(1)$ which means it executes in constant time.
- **Justification**: Accessing an element in a list by its index takes the same amount of time regardless of the list's size.

## Task1
**Description**: The problem involves calculating the size of data structure.

**Approach**: Build a summary of input.

**Complexity Analysis**:
- **Algorithm**: Iterating through all elements in texts and calls once each and performing two add operations on the set.

- **Big O Notation**: $O(n)$ which means two set add operation on each element in the input of size $n$ for time complexity and  $n$ as total number of unique elements in output for space complexity.


- **Justification**: It perform a constant number of operations for each element in the input and in worst case the output will contain all input elements.


## Task2
**Description**: The problem involves calculating the sum of elements in the input array.

**Approach**: Iterating through the array a single time, summing each element.

**Complexity Analysis**:
- **Algorithm**: Iterating through all elements in calls once using a for loop and performing four constant-time operations.

- **Big O Notation**: $O(n)$ where $n$ is the number of elements in the array.


- **Justification**: One for loop and four constant-time operations with $O(1)$ and $max$ on dictionary with $O(n)$ .

## Task3 part A
**Description**: The problem involves slicing all elements in the input array and calculating the sum of elements.

**Approach**: Iterating through the input array twice and summing each element.

**Complexity Analysis**:
- **Algorithm**: Iterating through all elements in calls once using a for loop and performing checking and appending operations. Aftewards converting and sorting of output array.

- **Big O Notation**: $O(n + m$ log $m)$ for time complexity and $O(n+m)$ for space complexity, where $n$ is the number of calls and $m$ is the number of unique called numbers ($m$ ≤ $n$).


- **Justification**: One for loop and three constant-time operations with $O(1)$, afterwards the most expensive operations are converting to set and back to eliminate duplicates with $O(m)$ and sorting the output list with $O(m$ log $m)$ .

## Task3 part B
**Description**: The problem involves comparing all the elements in the input array and calculating the percentage to the total size.

**Approach**: Iterating through the input array once and summing selected elements.

**Complexity Analysis**:
- **Algorithm**: Iterating through all elements in calls once using a for loop and conditionally incrementing a variable.

- **Big O Notation**: $O(n)$ where $n$ is the number of calls.


- **Justification**: One for loop and four constant-time operations with $O(1)$, accessing by index twice, calling a function and incrementing .

## Task4

**Description**: The problem involves filtering two input arrays.

**Approach**: Iterating through the input array  twice. Firstly to build a set according to conditions and secondly to eliminate elements according to condition.

**Complexity Analysis**:
- **Algorithm**: ___texters__ function: basically builds a set from all elements of the __texts__ input array. __not_called__ function iterates on calls, adding to set elements on condition. Aftewards it makes second iteration on the same input array __calls__ to remove elements according to condition.

- **Big O Notation**: $O(t + c)$ where $t$ is the number of texts and $c$ is the number of calls.


- **Justification**: 
__texters__ function: for loop with constant-time operation with $O(t)$, __not_called__ calling a function with $O(t)$, for loop with three constant-time operations with $O(c)$, second for loop with constant-time operation with $O(c)$.

