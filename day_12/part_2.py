import common.file_read as fr

start = "start"
end = "end"


def path_search(cave_graph, cur_path, total_paths, small_caves_visited, second_visit):
    cur_cave = cur_path[-1]

    if cur_cave == end:
        total_paths.append(cur_path)
        return total_paths

    new_small_caves_visited = small_caves_visited.copy()
    if cur_cave.islower():
        new_small_caves_visited.append(cur_cave)

    for next_cave in cave_graph[cur_cave]:
        new_second_visit = second_visit
        if next_cave != start and next_cave.islower() and next_cave in small_caves_visited and second_visit is None:
            new_second_visit = next_cave

        if next_cave not in small_caves_visited or new_second_visit != second_visit:
            total_paths = path_search(cave_graph, cur_path + [next_cave], total_paths, new_small_caves_visited, new_second_visit)

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

total_paths = path_search(cave_graph, [start], [], [], None)

print(len(total_paths))