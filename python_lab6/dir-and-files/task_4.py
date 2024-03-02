with open("examplefile.txt", "w+") as txt:
    txt.write("1 2\n")


with open("examplefile.txt", "r") as file:
    line_count = sum(1 for line in file)

print("Number of lines:", line_count)
