from collections import deque

def min_moves_to_destination(grid, M, N, src, dest, move_rule):
    directions = [
        move_rule,
        (move_rule[1], -move_rule[0]),
        (-move_rule[1], move_rule[0]),
        (-move_rule[0], -move_rule[1])
    ]
    
    queue = deque([(src[0], src[1], 0)])
    visited = set([(src[0], src[1])])
    
    while queue:
        x, y, moves = queue.popleft()
        
        if (x, y) == dest:
            return moves
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))
    
    return -1

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
src = tuple(map(int, input().split()))
dest = tuple(map(int, input().split()))
move_rule = tuple(map(int, input().split()))

print(min_moves_to_destination(grid, M, N, src, dest, move_rule))
