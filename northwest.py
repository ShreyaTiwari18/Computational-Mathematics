print("------------------------------------------------------------")
print("               NORTHWEST CORNER METHOD")
print("------------------------------------------------------------")

supply = [50, 60, 25]
demand = [30, 40, 20, 45]
m = len(supply)
n = len(demand)

cost = [
    [2, 3, 1, 4],
    [3, 2, 5, 9],
    [8, 4, 3, 7]
]

allocation = [[0 for _ in range(n)] for _ in range(m)]

print(f" Supply  : {supply}")
print(f" Demand  : {demand}\n")

print(" Cost Matrix (C[i][j]) :")
for row in cost:
    print(" ", row)

i, j = 0, 0
while i < m and j < n:
    x = min(supply[i], demand[j])
    allocation[i][j] = x
    supply[i] -= x
    demand[j] -= x

    if supply[i] == 0 and i < m - 1:
        i += 1
    elif demand[j] == 0 and j < n - 1:
        j += 1
    else:
        i += 1
        j += 1

print("\n------------------------------------------------------------")
print(" Allocation Matrix (X[i][j]) :")
for row in allocation:
    print(" ", row)

total_cost = 0
for i in range(m):
    for j in range(n):
        total_cost += allocation[i][j] * cost[i][j]

print("------------------------------------------------------------")
print(f" Total Transportation Cost = {total_cost}")
print("------------------------------------------------------------")
