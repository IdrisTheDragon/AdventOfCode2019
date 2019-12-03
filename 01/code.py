import math


    
def part1():
    with open('input.txt') as fp:
        t = fp.readline()
        sum = 0
        while t:   
            t = int(t)
            sum = sum + math.floor(t/3) - 2
            t = fp.readline()
        print("part 1:",sum)   
 
def fuelMass(t):
    m = math.floor(t/3) - 2
    if m<=0:
        return 0
    else:
        return m + fuelMass(m)
    
def part2():
    with open('input.txt') as fp:
        t = fp.readline()
        sum = 0
        while t:   
            t = int(t)
            sum = sum + fuelMass(t)
            t = fp.readline()
        print("part 2:",sum)
            
part1()
part2()