from math import pi, tan

sides_number = int(input("Number of sides: "))
side_length = int(input("the length of a side: "))

print(
    f"The area of the polygon is: {round(sides_number * pow(side_length, 2) / 4 * tan(pi/sides_number))}"
)
