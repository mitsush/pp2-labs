def solve(numheads=35, numlegs=94):
    rabbits = (numlegs - (numheads * 2)) / 2
    chickens = numheads - rabbits
    print(f"Number of rabbits: {rabbits}\nNumber of chickens: {chickens}")

solve()
