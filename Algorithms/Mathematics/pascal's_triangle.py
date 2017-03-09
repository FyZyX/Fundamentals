def pascal(p):
    result = [[1]]
    [result.append(list(map(sum, zip([0] + result[-1], result[-1] + [0])))) for _ in range(p - 1)]
    return result

print(pascal(5))
