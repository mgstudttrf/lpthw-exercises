def func(step, ceil):
    listz = []
    i = 0
    while i < ceil:
        print(i)
        listz.append(i)
        i+=step
        print(i, "_----")

    return listz

els = func(2,30)

for i in els:
    print(i)
