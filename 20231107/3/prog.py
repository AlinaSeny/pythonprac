class Undead(Exception):
    pass


class Skeleton(Undead):
    pass


class Zombie(Undead):
    pass


class Ghoul(Undead):
    pass


def necro(a):
    k = a % 3
    if k == 0:
        raise Skeleton
    elif k == 1:
        raise Zombie
    else:
        raise Ghoul


x, y = eval(input())
for i in range(x, y):
    try:
        necro(i)
    except Skeleton:
        print('Skeleton')
    except Zombie:
        print('Zombie')
    except Ghoul:
        print('Generic Undead')



