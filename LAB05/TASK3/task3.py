inpfile = open("input3_3.txt", 'r')
outfile = open("output3_3.txt", 'w')

v, e = list(map(int, inpfile.readline().strip().split()))

adj_list = [[] for i in range(v+1)]
adj_list_Inverse = [[] for i in range(v+1)]
visited = [0 for i in range(v+1)]
visited_Inverse = [0 for i in range(v+1)]
components = []
stack = []

def DFS_Traversal(source):
    visited[source] = 1
    for adj_node in adj_list[source]:
        if visited[adj_node] == 0:
            DFS_Traversal(adj_node)
            
    stack.append(source)        
    
def DFS_Traversal_Inverse(source, components):
    visited_Inverse[source] = 1
    for adj_node in adj_list_Inverse[source]:
        if visited_Inverse[adj_node] == 0:
            DFS_Traversal_Inverse(adj_node, components)
            
    components.append(source)

for i in range(1, (e+1)):
    f, t = list(map(int, inpfile.readline().strip().split()))
    adj_list[f].append(t)
    adj_list_Inverse[t].append(f)


for i in range(1, (v+1)):
    if visited[i] == 0:
        DFS_Traversal(i)

stack.reverse()
for i in stack:
    if visited_Inverse[i] == 0:
        components = []
        DFS_Traversal_Inverse(i, components)
        print(*components, file=outfile)
        
inpfile.close()
outfile.close()