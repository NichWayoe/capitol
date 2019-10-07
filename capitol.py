# Capitol Maps: Find your way around D.C.!
latitude = float(input("Insert your latitude: "))
longitude = float(input("Insert your longitude: "))
K_St = (38.902649, 0)
The_white_House = (38.897789, -77.036562)
Dupont_Circle = (38.909760, -77.043479)
Downing_Hall = (38.921669, -77.021361)
Union_Station = (38.897698, -77.007200)

# calculating position of location relative to K street
if latitude < K_St[0]:
    print("You are south of K St")
elif latitude > K_St[0]:
    print("You are north of K St")

# calculating position of location relative to the white house
if latitude < The_white_House[0]:
    print("You are south of the White House")
elif latitude > The_white_House[0]:
    print("You are north of the White House")
if longitude < The_white_House[1]:
    print("You are west of the White House")
elif longitude > The_white_House[1]:
    print("You are east of the White House")

# calculating position of location relative to Dowing Hall
if latitude < Downing_Hall[0]:
    print("You are south of Downing Hall")
elif latitude > Downing_Hall[0]:
    print("You are north of Downing Hall")
if longitude < Downing_Hall[1]:
    print("You are west of Downing Hall")
elif longitude > Downing_Hall[1]:
    print("You are east of Downing Hall")

# calculating position of location relative to Dupont Circle
if latitude < Dupont_Circle[0]:
    print("You are south of Dupont Circle")
elif latitude > Dupont_Circle[0]:
    print("You are north of Dupont Circle")
if longitude < Dupont_Circle[1]:
    print("You are west of Dupont Circle")
elif longitude > Dupont_Circle[1]:
    print("You are east of Dupont Circle")

# calculating position of location relative to Union Station
if latitude < Union_Station[0]:
    print("You are south of Union Station")
elif latitude > Union_Station[0]:
    print("You are north of Union Station")
if longitude < Union_Station[1]:
    print("You are west of Union Station")
elif longitude > Union_Station[1]:
    print("You are east of Union Station")

# for caluculating the distance from Downing_Hall
from math import sin, cos, atan2, radians, sqrt

# changing from degree to radians
Downing_Hall = (radians(38.921669), radians(-77.021361))
latitude = radians(latitude)
longitude = radians(longitude)
clat = Downing_Hall[0] - latitude
clong = Downing_Hall[1] - longitude

# using the heversine formula
a = sin(clat / 2) ** 2 + cos(Downing_Hall[0]) * cos(latitude) * sin(clong / 2) ** 2
c = 2 * atan2(sqrt(a), sqrt(1 - a))
d = round(3958.8 * c, 1)
r = (d + 1, d + 2)
print("You are " + str(d) + " miles from Downing Hall")


