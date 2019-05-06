class Enemy():
    def attack(self):
        print("Attacking wildly with {0}!".format(self.weapon))


class Orc(Enemy):
    def __init__(self):
        self.weapon = "greataxe"


class Skeleton(Enemy):
    def __init__(self):
        self.weapon = "greatsword"


class Dragon(Enemy):
    def __init__(self):
        self.weapon = "fire breathing"


def factory(enemy_type):
    if (enemy_type == Orc):
        return Orc()
    elif (enemy_type == Skeleton):
        return Skeleton()
    elif (enemy_type == Dragon):
        return Dragon()
    else:
        raise TypeError


if __name__ == '__main__':
    d = factory(Dragon)
    d.attack()
