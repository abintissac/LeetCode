def can_place_flowers(flowerbed, n):
    length = len(flowerbed)
    count = 0
    i = 0

    while i < length:
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
            if count == n:
                return True
        i += 1

    return False
flowerbed = [1, 0, 0, 0, 1]
n = 1
result = can_place_flowers(flowerbed, n)
print(result)
