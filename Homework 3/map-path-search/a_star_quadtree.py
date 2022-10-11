import queue
import quadtreemap
import math
from heapq import heappush, heappop
from utils import dist2d


def _get_movements_4n(qtm, tile):
    neighborList = []
    neighborList.append(qtm.quadtree.tileIntersect(quadtreemap.BoundingBox(tile.boundary.x0 - 1, tile.boundary.y0,
                                                                           tile.boundary.width + 2,
                                                                           tile.boundary.height)))
    neighborList.append(qtm.quadtree.tileIntersect(quadtreemap.BoundingBox(tile.boundary.x0, tile.boundary.y0 - 1,
                                                                           tile.boundary.width,
                                                                           tile.boundary.height + 2)))
    movements = [(til, quadtreemap.Point.disOf2Points(tile.getCenter(), til.getCenter())) for til in neighborList]
    return movements


def _get_movements_8n(qtm: quadtreemap.QuadTreeMap, tile: quadtreemap.Tile):
    neighborList = qtm.quadtree.tileIntersect(quadtreemap.BoundingBox(tile.boundary.x0 - 1, tile.boundary.y0 - 1,
                                                                      tile.boundary.width + 2,
                                                                      tile.boundary.height + 2))
    movements = [(til, quadtreemap.Point.disOf2Points(tile.getCenter(), til.getCenter())) for til in neighborList]
    return movements


def a_star_quadtree(start_m, goal_m, qtm, movement='8n', occupancy_cost_factor=3):
    candidates = queue.PriorityQueue()

    # get array indices of start and goal
    start = qtm.quadtree.searchTileByIdx(quadtreemap.Point(start_m[0], start_m[1]))
    goal = qtm.quadtree.searchTileByIdx(quadtreemap.Point(goal_m[0], goal_m[1]))

    start_tile_cost = 0
    start_tile_estimated_cost_to_goal = quadtreemap.Point.disOf2Points(start.getCenter(), goal.getCenter()) * occupancy_cost_factor
    front = [(start_tile_estimated_cost_to_goal, start_tile_cost, start, None)]

    # use a dictionary to remember where we came from in order to reconstruct the path later on
    came_from = {}

    # check if start and goal nodes correspond to free spaces
    if not start or start.tile_points:
        raise Exception('Start node is not traversable')
    if not goal or goal.tile_points:
        raise Exception('Goal node is not traversable')

    while front:
        element = heappop(front)
        total_cost, cost, pos, previous = element

        # if this node has been visited already, skip it
        if pos in came_from:
            continue

        # set its previous node
        came_from[pos] = previous

        # if the goal has been reached, we are done!
        if pos == goal:
            break

        # get possible movements
        if movement == '4N':
            movements = _get_movements_4n(qtm, pos)
        elif movement == '8N':
            movements = _get_movements_8n(qtm, pos)
        else:
            raise ValueError('Unknown movement')

        # check neighbors, use heuristic
        for til, deltacost in movements:
            # check whether new position is inside the map or is an obstacle
            # if not, skip node
            if til.tile_points:
                continue

            # add node to front if it was not visited before and is not an obstacle
            if til not in came_from:
                potential_function_cost = til.tile_capacity * occupancy_cost_factor
                new_cost = cost + deltacost + potential_function_cost
                new_total_cost_to_goal = new_cost + potential_function_cost

                heappush(front, (new_total_cost_to_goal, new_cost, til, pos))

    # reconstruct path backwards (only if we reached the goal)
    path = []
    path_idx = []
    # print(len(path_record))
    # print(path_record)
    if goal in came_from:
        node = goal
        while node:
            path_idx.append(node)
            # transform array indices to meters
            # node_m_x, node_m_y = gmap.get_coordinates_from_index(node[0], node[1])
            # path.append((node_m_x, node_m_y))
            node = came_from[node]
        # reverse so that path is from start to goal.
        path.reverse()
        path_idx.reverse()

    # print("path_idx len: ", len(path_idx))
    # print("path_idx:\n", path_idx)
    return path, path_idx
