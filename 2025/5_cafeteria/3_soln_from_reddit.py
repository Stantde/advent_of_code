def fresh_ingredients(filepath):
    rngs = []
    vals = []
    with open(filepath) as file:
        read_rngs = True
        for line in file:
            if not line.rstrip():
                read_rngs = False
            elif read_rngs:
                rng = [int(i) for i in line.split('-')]
                rngs.append(rng)
                vals += rng
    vals = sorted(set(vals))
    func = lambda x: any(r0 <= x <= r1 for r0, r1 in rngs)
    counter = 0
    for i in range(len(vals)-1):
        inter_val = (vals[i+1]+vals[i])//2
        n_between = vals[i+1]-vals[i]-1
        counter += func(inter_val)*n_between
    return counter+len(vals)

res=fresh_ingredients("/home/demetrius/build/advent_of_code/2025/5_cafeteria/input.txt")
print(res)