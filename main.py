from gen_map import rand_map
from mymap import myMap
from astar import AStar


rand_map(n_points=10, max_next_node=3)

start = 6
target = 2

my_map, costs = myMap()
print(my_map)
print(costs)
AStar(start, target, my_map, costs)
