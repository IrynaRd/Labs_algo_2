from math import inf

def read_from_file(filename):
    E = []
    with open(filename, "r") as f:
        for i, line in enumerate(f):
            line = line.strip()
            weights = line.split(",")
            
            for j, w in enumerate(weights):
                weight = float(w)

                if weight != 0.0 and i < j:
                    E.append((weight, i, j))
    
    return E, j+1

E, N = read_from_file("islands.csv")
U = {0}
T = []

def get_min(E, U):
    e_min = (inf, -1, -1)

    for v in U:
        candidates = [e for e in E if (e[1] == v and e[2] not in U) or (e[2] == v and e[1] not in U)]
        if not candidates:
            continue
        e_e = min(candidates, key = lambda x: x[0])
        if e_min[0] > e_e[0]:
            e_min = e_e
    
    return e_min

def prim_algorithm(E, N):
    while len(U) < N:
        e = get_min(E, U)
        if e[0] == inf:
            break

        T.append(e)
        if e[1] in U:
            U.add(e[2])
        else:
            U.add(e[1])
    
    return T

mst = prim_algorithm(E, N)
min = 0
for el in mst:
    w, i, j = el
    min += w

print(f"Minimal cable lenth: {min} km.")



