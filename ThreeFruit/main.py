import itertools
x = 1
y = 1
z = 1
done = False


def isDone(x, y, z):
    if x == 0 or y == 0 or z == 0:
        return False
    print('{} / ({} + {}) + {} / ({} + {}) + {} / ({} + {}) = {}'.format(
        x, y, z, y, x, z, z, x, y, x / (y + z) + y / (x + z) + z / (x + y)))
    return x / (y + z) + y / (x + z) + z / (x + y) == 4.0


print("Calculating...")
for i in itertools.count(1):
    x = i
    if done:
        break
    else:
        done = isDone(x, y, z)
    for j in itertools.count(1):
        y = j
        if done:
            break
        else:
            done = isDone(x, y, z)
        for k in itertools.count(1):
            z = k
            if done:
                break
            else:
                done = isDone(x, y, z)

print("=============================Solution=============================")
print("x =", x)
print("y =", y)
print("z =", z)
