infile = open("input3_2.txt", 'r')
outfile = open("output3_2.txt", 'w')

def find_representative(a):
    if parent[a] == a:
        return a
    return find_representative(parent[a])


def union(a, b):
    u = find_representative(a)
    v = find_representative(b)
    if u != v:
        parent[u] = v
        circle[v] += circle[u]

    outfile.write(str(circle[v]) + '\n')


person, query = map(int, infile.readline().split())
parent = [ i for i in range(person) ]
circle = [ 1 for i in range(person) ]

for i in range(query):
    a, b = map(int, infile.readline().split())
    union(a, b)

infile.close()
outfile.close()