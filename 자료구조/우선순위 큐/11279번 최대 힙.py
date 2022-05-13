class ListMaxHeap:
    def __init__(self):
        self._list = []
        self._size = 0
        self._level = 0

    @staticmethod
    def heapify(*elements):
        num_elements = len(elements)
        level = 0
        while num_elements > 1:
            num_elements //= 2
            level += 1
        del num_elements

        
        heap = ListMaxHeap()
        heap._list = list(elements)
        heap._size = len(elements)
        heap._level = level

        cur_level = level - 1
        while cur_level >= 0:
            for node_idx in range(pow(2, cur_level) - 1, pow(2, cur_level + 1) - 1):
                heap._down_heap_starts_at(node_idx)
            cur_level -= 1
        return heap

    def __repr__(self):
        return f"ListMaxHeap.heapify({', '.join(map(str, self._list))})"

    def __len__(self):
        return self._size

    def level(self):
        return self._level

    def is_empty(self):
        return self._size == 0

    def add(self, element):
        self._list.append(element)
        self._size += 1

        if self._size >= pow(2, self._level + 1):
            self._level += 1
            
        if self._size > 1:
            self._up_heap()

    def _up_heap(self):
        node_idx = self._size - 1
        while node_idx > 0 and self._list[(node_idx - 1) // 2] < self._list[node_idx]:
            tmp = self._list[(node_idx - 1) // 2]
            self._list[(node_idx - 1) // 2] = self._list[node_idx]
            self._list[node_idx] = tmp
            del tmp # better gc
            node_idx = (node_idx - 1) // 2    

    def max(self):
        return self._list[0]

    def remove_max(self):
        if self._size <= 0:
            return 0
        if self._size == 1:
            self._size -= 1
            self._level = 0
            return self._list.pop()
        tmp = self._list[0]
        self._list[0] = self._list[self._size - 1]
        self._list[self._size - 1] = tmp
        del tmp
        ans = self._list[self._size - 1]
        self._list.pop()
        self._size -= 1

        if self._size < pow(2, self._level):
            self._level -= 1
        
        self._down_heap()
        return ans

    def _down_heap(self):
        self._down_heap_starts_at(0)

    def _down_heap_starts_at(self, s_idx):
        node_idx = s_idx
        big_child_node_idx = self._get_big_child_node_idx(node_idx)
        while big_child_node_idx is not None and self._list[node_idx] < self._list[big_child_node_idx]:
            tmp = self._list[node_idx]
            self._list[node_idx] = self._list[big_child_node_idx]
            self._list[big_child_node_idx] = tmp
            del tmp
            node_idx = big_child_node_idx
            big_child_node_idx = self._get_big_child_node_idx(node_idx)

    def _get_big_child_node_idx(self, node_idx):
        left_child = 2 * node_idx + 1
        right_child = 2 * node_idx + 2

        if left_child >= self._size:
            return None

        if right_child >= self._size:
            return left_child

        if self._list[left_child] > self._list[right_child]:
            return left_child

        return right_child

from sys import stdin

f_input = lambda : stdin.readline().rstrip()

t = int(f_input())
heap = ListMaxHeap()
for _ in range(t):
    op = int(f_input())
    if op == 0:
        print(heap.remove_max())
    else:
        heap.add(op)
