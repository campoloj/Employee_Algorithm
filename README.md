# Employee_Algorithm
Employee Algorithm

Implementation of an algorithm to optimally choose employees to maximize total "value" in a employment tree.

In detail, this is the solution to the following prompt: Given a tree of n Employees, rooted at the CEO and with 
each employee having a boss and a value, and a value k, choose n Employees to maximize total value, given that:

 - Each employee adds its value plus the value of every boss in their chain (boss, boss's boss, etc.)
 - Each employee can only provide its value to the total once

I used a greedy algorithm technique of choosing the leaf employee with the greatest total value at each step and adjusting the 
total values of the employees affected by this choice. The leaf nodes were stored in a Priority Queue for efficient access to 
the maximum value node (O(1)) and readjustment (O(log n)).

All files consisting of number.in are the files that feed in the number of employees and number of choices in the first line, 
with subsequent lines being employees represented by 3 values; ID number, boss ID number, and value. Number.out files show the
correct maximum value for choosing the given number of employees in that tree. THe actual algorithm is solved in Main.py.


Code descriptions:

Class Employee:
  An employee object consisting of an employees index, boss index, value, total value (value + value of all bosses above),
  used (indicates if value givel already or not), leaf (is or is not a leaf node), leafs_under (list of leaf nodes under
  this boss), heap_posn (position in MaxHeap if a leaf), and to_subtract (an accumulator used for adjusting total value after
  employees are chosen).
  
Class MaxHeap:
  An implementation of a MaxHeap - a Priority Queue in which every child is lesser in value than its parent.
  
Lines 126 - 137:
  Functions to read the given files to assign n = number of employees, k = number of choices possible, and 
  employees = a list of Employees in order, starting with an "empty" Employee at index 0. As employees are created,
  their total values are assigned and their leaf status is determined.
  
