""" 장난 삼아 파이썬의 여러 기능을 이용하여 복잡하게 짠 절댓값 힙 """
def pop(heap):
    if len(heap) == 0:
        return 0
    heap[0], heap[-1] = heap[-1], heap[0] # Pythonic code
    ans = heap.pop()
    downheap(heap)
    return ans
    

def downheap(heap):
    idx = 0
    # Spaghetti code
    left_child_idx = lambda : idx * 2 + 1
    right_child_idx = lambda : idx * 2 + 2
    min_child_idx = lambda : abs_smaller_idx(heap, left_child_idx(), right_child_idx())
    while -1 < min_child_idx() < len(heap) and \
          abs_smaller_idx(heap, idx, min_child_idx()) == min_child_idx():
        min_child = min_child_idx()
        heap[min_child], heap[idx] = heap[idx], heap[min_child]
        idx = min_child
    
def upheap(heap):
    idx = len(heap) - 1
    parent_idx = lambda : (idx - 1) // 2 # Spaghetti code
    while abs_smaller_idx(heap, idx, parent_idx()) == idx and idx > 0:
        parent = parent_idx()
        heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = parent_idx()
    

def abs_smaller_idx(heap, idx_a, idx_b):
    if idx_a >= len(heap):
        if idx_b >= len(heap):
            return -1
        return idx_b
    if idx_b >= len(heap):
        return idx_a
    if abs(heap[idx_a]) > abs(heap[idx_b]):
        return idx_b
    if abs(heap[idx_a]) < abs(heap[idx_b]):
        return idx_a
    if heap[idx_a] > heap[idx_b]:
        return idx_b
    return idx_a


from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n = int(f_input())
heap = []

for _ in range(n):
    op = int(f_input())
    if op == 0:
        ans = pop(heap)
        print(ans)
    else:
        heap.append(op)
        upheap(heap)
