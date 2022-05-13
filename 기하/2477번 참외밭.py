from sys import stdin

density = map(int, stdin.readline().rstrip())
EAST = 1
WEST = 2
SOUTH = 3
NORTH = 4

for _ in range(6):
    direction, length = map(int, stdin.readline().rstrip().split())
    if direction == EAST or direction == WEST:
        
        
