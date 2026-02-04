class Parrot:

    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age


blueparrot = Parrot('blu', 10)
greenparrot = Parrot('Woo', 15)

print("Blu is a {}".format(blueparrot.species))
print("Woo is a {}".format(greenparrot.species))

print("{} is {} years old".format(blueparrot.name,blueparrot.age))
print("{} is {} years old".format(greenparrot.name,greenparrot.age))