x = 1
y = 1
z = 1
MAX = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000
done = False


def isDone(x, y, z):
    if x == 0 or y == 0 or z == 0:
        return False
    print('{} / ({} + {}) + {} / ({} + {}) + {} / ({} + {}) = {}'.format(
        x, y, z, y, x, z, z, x, y, x / (y + z) + y / (x + z) + z / (x + y)))
    return x / (y + z) + y / (x + z) + z / (x + y) == 4.0


print("Calculating...")
for i in range(1, MAX):
    x = i
    if done:
        break
    else:
        done = isDone(x, y, z)
    for j in range(1, MAX):
        y = j
        if done:
            break
        else:
            done = isDone(x, y, z)
        for k in range(1, MAX):
            z = k
            if done:
                break
            else:
                done = isDone(x, y, z)

print("=============================Solution=============================")
print("x =", x)
print("y =", y)
print("z =", z)
