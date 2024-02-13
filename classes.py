class cars:
    def __init__(self, hp, mod, tires, type):
        self.hp = hp
        self.mod = mod
        self.tires = tires
        if self.hp > "300" and self.mod == "Back traction":
            self.type = "sedan"
        else:
            self.type = "SUV"

jeep = cars("220 Horse power", "4 by 4", "Rali tires", "")


BMW = cars("320 Horse power", "Back traction", "Race tires", "")

print(BMW.type)
print(jeep.type)


