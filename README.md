# Employee_Algorithm
Employee Algorithm

Implementation of an algorithm to optimally choose employees to maximize total "value" in a employment tree.

In detail, this is the solution to the following prompt: Given a tree of n Employees, rooted at the CEO and with 
each employee having a boss and a value, and a value k, choose k Employees to maximize total value, given that:

 - Each employee adds its value plus the value of every boss in their chain (boss, boss's boss, etc.)
 - Each employee can only provide its value to the total once

I used a greedy algorithm technique of choosing the leaf employee with the greatest total value at each step and adjusting the total values of the employees affected by this choice. Because total value is dependent on the values of every boss above it, the leaf nodes will have the highest total values to offer. By choosing the maximum total value available at each step, this algorithm results in the overall maximum value possible from the employee tree. The leaf nodes were stored in a Priority Queue for efficient access to the maximum value node (O(1)), and efficient readjustment (O(log n)) of affected nodes.

All files consisting of number.in are the files that feed in the number of employees and number of choices in the first line, 
with subsequent lines being employees represented by 3 values; ID number, boss ID number, and value. Number.out files show the
correct maximum value for choosing the given number of employees in that tree. The actual algorithm is solved in Main.py.


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
  
Lines 140 - 150:
  Similar to Lines 126 - 137, but designed to use stdin rather than the explicit input files provided.
  
Lines 152 - 156:
  Creates a MaxHeap, and for each leaf in the employees list, adds that leaf to the heap and adds that leaf to the
  leafs_under field of every boss above it. The heap is ordered by total_value.
  
Lines 159 - 175:
  A function for making adjustments after choosing an employee. This function adds the employees value to the to_subract
  field of every leaf under it (to account for it being used and unable to provide further value), and recursively does the
  same for every boss above the employee. Once reaching a used boss or the CEO, every leaf under this boss has its
  total_value decremented by its to_subtract value and is downheaped to readjust its position in the PriorityQueue.
  
Lines 178 - 187:
  The main algorithm function. This function allocates an accumulater for total value, adjusts the choices to not exceed
  the number of leaves (because by then all employees would be used), and for each employee choice it pops the max 
  total_value leaf off the Heap, adds its value to the total, and adjusts every employee / leaf affected by this choice
  Returns the total once number of choices reaches 0.
