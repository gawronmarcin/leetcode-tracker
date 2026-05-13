"""
Task:
Task

Bajtek has always been fascinated by airplanes. Yesterday he learned that they do not fly randomly,
but have designated corridors through which they can fly. Corridors have their target altitudes, thanks to which planes do not collide. You can read more about corridors here.

Unfortunately, Bajtek suffers from airsickness; if his plane changes altitude too much, he feels very sick. Therefore, since he found out about the corridors,
he transcribed the connection map of his airport into a weighted graph and started wondering if there is a connection via some corridors that will allow him to fly from A to B.

Output

The output should contain q lines; in the i-th line, the program should print TAK if there is a path from vertex v_i to u_i
whose corridor altitude differences k_1, k_2, ..., k_s satisfy the condition max(k_i) - min(k_i) <= d (for i in {1, ..., s}), where s is the length of the path along these corridors. Otherwise, the program should print NIE.

Algorithm description:
This solution evaluates all possible valid ranges of corridor heights using a brute-force
approach optimized with a pseudo sliding window. It sorts all edges by weight. For each
edge treated as the minimum weight of a valid path, it adds subsequent edges to a Disjoint
Set Union (DSU) as long as the weight difference does not exceed max_diff. To process
queries efficiently, it uses path compression and union by size. To avoid the O(N) cost
of clearing the entire DSU array for each window, it tracks "touched" vertices and resets
only those. Early exits are triggered if all queries are resolved or the upper weight
limit is breached.
"""

class Solution:
    def solve(self,num_vertices: int, max_diff: int, edges: list[tuple[int, int, int]], queries: list[tuple[int, int]]) -> list[
        str]:
        num_edges = len(edges)
        num_queries = len(queries)

        sorted_edges = sorted(edges, key=lambda x: x[2])
        queries_solved = [0] * num_queries
        solved_count = 0

        parent = list(range(num_vertices + 1))
        size = [1] * (num_vertices + 1)

        def find(u: int) -> int:
            curr = u
            while parent[curr] != curr:
                curr = parent[curr]

            curr2 = u
            while curr2 != curr:
                nxt = parent[curr2]
                parent[curr2] = curr
                curr2 = nxt

            return curr

        for i in range(num_edges):
            if solved_count == num_queries:
                break

            min_val = sorted_edges[i][2]
            touched = []

            for j in range(i, num_edges):
                current_u, current_v, current_weight = sorted_edges[j]

                if current_weight - min_val <= max_diff:
                    touched.append(current_u)
                    touched.append(current_v)

                    root_u = find(current_u)
                    root_v = find(current_v)

                    if root_u != root_v:
                        if size[root_u] >= size[root_v]:
                            parent[root_v] = root_u
                            size[root_u] += size[root_v]
                        else:
                            parent[root_u] = root_v
                            size[root_v] += size[root_u]
                else:
                    break

            for q_idx in range(num_queries):
                if queries_solved[q_idx] == 0:
                    query_u, query_v = queries[q_idx]
                    if find(query_u) == find(query_v):
                        queries_solved[q_idx] = 1
                        solved_count += 1

            for node in touched:
                parent[node] = node
                size[node] = 1

        return ["TAK" if is_solved == 1 else "NIE" for is_solved in queries_solved]