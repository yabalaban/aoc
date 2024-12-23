from collections import defaultdict, deque
from utils import site 

rows = site.download_input(day=23)


connections = defaultdict(set)
hosts = set()


for connection in rows:
    a, b = connection.split("-")
    connections[b].add(a)
    connections[a].add(b)
    hosts.add(a)
    hosts.add(b)


def find_loops(connections):
    loops = set()
    for snode in connections.keys():
        visited = set()
        queue = deque()
        queue.append([snode])
        while queue:
            nodes = queue.popleft()
            node = nodes[-1]
            visited.add(node)
            for nn in connections[node]:
                if nn == snode:
                    loops.add(tuple(sorted(set(nodes + [nn]))))
                elif nn not in visited:
                    queue.append(nodes + [nn])
    return loops


loops = find_loops(connections)

loops = [l for l in loops if any([k.startswith("t") for k in l])]
print(len([l for l in loops if len(l) == 3]))


def max_clique(clique, hosts):
    remaining = set(hosts) - set(clique)
    for host in remaining:
        if all([host in connections[n] for n in clique]):
            return max_clique(clique + [host], hosts)
    return clique


maxclique = set()
for node in hosts:
    n = max_clique([node], hosts)
    if len(n) > len(maxclique):
        maxclique = n
print(",".join(sorted(maxclique)))