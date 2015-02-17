#!/usr/bin/python

import sys


class Employee:
    def __init__(self, index, boss, value):
        self.index = index
        """:type: int"""
        self.boss = boss
        """:type: Employee"""
        self.value = value
        """:type: int"""
        if self.boss is None:
            self.tot_value = 0
            """:type: int"""
        else:
            self.tot_value = value + boss.tot_value
            """:type: int"""
        self.used = False
        """:type: bool"""
        self.leaf = True
        """:type: bool"""
        self.leafs_under = []
        """:type: list of [Employee]"""
        self.heap_posn = -1
        """:type: int"""
        self.to_subtract = 0
        """:type: int"""

    def add_leafs_under(self):
        """
        Adds this leaf to every boss above it
        """
        current_boss = self.boss
        while current_boss is not None:
            current_boss.leafs_under.append(self)
            current_boss = current_boss.boss


class MaxHeap:
    def __init__(self):
        self.heap_array = [Employee(0, None, 0)]
        """:type : list of Employee"""
        self.size = 0
        """:type : int"""

    def upheap(self, i):
        """
        Upheaps the item at index i in this heap
        :param i: the index of the item to upheap
        :type i: int
        """
        while i // 2 > 0:
            if self.heap_array[i].tot_value > self.heap_array[i // 2].tot_value:
                old_leaf = self.heap_array[i]
                self.heap_array[i] = self.heap_array[i // 2]
                self.heap_array[i].heap_posn = i
                self.heap_array[i // 2] = old_leaf
                self.heap_array[i // 2].heap_posn = i // 2
            i //= 2

    def insert(self, leaf):
        """
        Inserts a leaf employee into this heap
        :param leaf: the employee to be inserted
        :type leaf Employee
        """
        self.heap_array.append(leaf)
        self.size += 1
        leaf.heap_posn = self.size
        self.upheap(self.size)

    def max_child_index(self, i):
        """
        Finds the index of the largest child under a node in this heap
        :param i: the index of the node
        :type i int
        :return: the index of the largest child
        :rtype int
        """
        if i * 2 + 1 > self.size:
            # only one child
            return i * 2
        elif self.heap_array[i * 2].tot_value > self.heap_array[i * 2 + 1].tot_value:
            # first child is greater
            return i * 2
        else:
            # second child is greater
            return i * 2 + 1

    def downheap(self, i):
        """
        Downheaps the item at index i in this heap
        :param i: the index of the item to downheap
        :type i int
        """
        while i * 2 <= self.size:
            target = self.max_child_index(i)
            if self.heap_array[i].tot_value < self.heap_array[target].tot_value:
                old_leaf = self.heap_array[i]
                self.heap_array[i] = self.heap_array[target]
                self.heap_array[i].heap_posn = i
                self.heap_array[target] = old_leaf
                self.heap_array[target].heap_posn = target
            i = target

    def delete_max(self):
        """
        Deletes the maximum value leaf in this heap and adjusts the remaining heap
        :return: the maximum value leaf
        :rtype Employee
        """
        max_leaf = self.heap_array[1]
        self.heap_array[1] = self.heap_array[self.size]
        self.size -= 1
        self.heap_array.pop()
        self.downheap(1)
        return max_leaf






f = open("18.in", "r")
n_and_k = (map(int, f.readline().split(" ")))
n = n_and_k[0]
k = n_and_k[1]

employees = [Employee(0, None, 0)]
for j in range(1, n+1):
    emp = (map(int, f.readline().split(" ")))
    employees.append(Employee(emp[0], employees[emp[1]], emp[2]))
    employees[emp[1]].leaf = False

f.close()


"""
n_and_k = (map(int, sys.stdin.readline().split(" ")))
n = n_and_k[0]
k = n_and_k[1]

employees = [Employee(0, None, 0)]
for j in range(1, n+1):
    emp = (map(int, sys.stdin.readline().split(" ")))
    employees.append(Employee(emp[0], employees[emp[1]], emp[2]))
    employees[emp[1]].leaf = False
"""

leafs = MaxHeap()
for e in employees:
    if e.leaf:
        leafs.insert(e)
        e.add_leafs_under()


def mark_and_fix(emp):
    """
    Makes adjustments for selecting this leaf by changing the values of
    every leaf it effects and adjusting their positions in the heap
    :param emp: the leaf employee chosen
    :type emp Employee
    """
    emp.used = True
    if emp.boss.used or emp.boss.value == 0:
        for leaf in emp.leafs_under:
            leaf.tot_value -= (leaf.to_subtract + emp.value)
            leaf.to_subtract = 0
            leafs.downheap(leaf.heap_posn)
    else:
        for leaf in emp.leafs_under:
            leaf.to_subtract += emp.value
        mark_and_fix(emp.boss)


def algorithm(choices):
    total = 0
    if choices > leafs.size:
        choices = leafs.size
    while choices > 0:
        leaf = leafs.delete_max()
        total += leaf.tot_value
        mark_and_fix(leaf)
        choices -= 1
    return total

print algorithm(k)