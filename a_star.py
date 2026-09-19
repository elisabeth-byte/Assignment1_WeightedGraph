
import heapq
from helpers import reconstruct_path


def a_star(graph, start, goal, h):
    frontier = [(h(start), start)]
    cost_so_far = {start: 0}
    came_from = {}
    visited = []
    seen = set()

    while frontier:
        priority, node = heapq.heappop(frontier)

        if node not in seen:
            seen.add(node)
            visited.append(node)

        if node == goal:
            break

        for neighbour, weight in graph[node]:
            new_cost = cost_so_far[node] + weight

            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                came_from[neighbour] = node

                priority = new_cost + h(neighbour)
                heapq.heappush(frontier, (priority, neighbour))

    path = reconstruct_path(came_from, start, goal)
    return path, visited