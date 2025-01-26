import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length, width, height = 1, 1, 1
x, y, z = 0, 0, 0.5


for x_ in range(5):
    z = 0.5
    length, width, height = 1, 1, 1
    for y_ in range(5):
        z = 0.5
        length, width, height = 1, 1, 1
        for z_ in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x + x_, y + y_, z], size=[length, width, height])
            length, width, height = length * 0.9, width * 0.9, height * 0.9
            z += height + height * 0.05  # 0.05 is half of the decrease in height

pyrosim.End()

