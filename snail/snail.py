

def snail(snail_map):
    if snail_map == [[]]:
        return []
    result = []
    iteration = 0
    n = len(snail_map)
    runtime = n 
    while runtime >= 0:
        for i in range(iteration, n+iteration):
            result.append(snail_map[iteration][i])
        for j in range(iteration+1, n+iteration):
            result.append(snail_map[j][n-1+iteration])
        for z in range(len(snail_map)-(iteration+2), len(snail_map)-len(snail_map)+iteration-1, -1):
            result.append(snail_map[len(snail_map)-iteration-1][z])
        for y in range(len(snail_map)-2-iteration, len(snail_map)-len(snail_map)+iteration, -1):
            result.append(snail_map[y][iteration])
        runtime -= 1
        iteration += 1
        n -= 2
    return result

array = [[ 1, 2, 3, 4, 5],
         [ 6, 7, 8, 9,10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]]

expected = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13]
print(f"GOT: \t\t{snail(array)} \n EXPECTED: \t{expected}")