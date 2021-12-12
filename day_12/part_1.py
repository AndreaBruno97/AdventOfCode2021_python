import common.file_read as fr

start = "start"
end = "end"


def path_search(cave_graph, cur_path, total_paths, small_caves_visited):
    cur_cave = cur_path[-1]

    if cur_cave == end:
        total_paths.append(cur_path)
        return total_paths

    new_small_caves_visited = small_caves_visited.copy()
    if cur_cave.islower():
        new_small_caves_visited.append(cur_cave)

    for next_cave in cave_graph[cur_cave]:
        if next_cave not in small_caves_visited:
            total_paths = path_search(cave_graph, cur_path + [next_cave], total_paths, new_small_caves_visited)

    return total_paths


file = fr.open_file_lines()

cave_graph = {}

for line in file:
    cave_1, cave_2 = line.strip().split("-")

    for cave in [cave_1, cave_2]:
        if cave not in cave_graph:
            cave_graph[cave] = set()

    cave_graph[cave_1].add(cave_2)
    cave_graph[cave_2].add(cave_1)

total_paths = path_search(cave_graph, [start], [], [])

print(len(total_paths))