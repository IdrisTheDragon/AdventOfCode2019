# -*- coding: utf-8 -*-

def process(index, prog):
    op = prog[index]
    if op is 99:
        return prog
    elif op is 1:
        pos1 = prog[index+1]
        pos2 = prog[index+2]
        pos3 = prog[index+3]
        prog[pos3] = prog[pos1] + prog[pos2]
        return process(index+4,prog)
    elif op is 2:
        pos1 = prog[index+1]
        pos2 = prog[index+2]
        pos3 = prog[index+3]
        prog[pos3] = prog[pos1] * prog[pos2]
        return process(index+4,prog)
    else:
        print("invalid op code")
    
def part1():
    with open('input.txt') as fp:
        t = fp.readline()
        t = t.split(',')
        t = list(map(int,t))
        result = process(0,t)
        print(result[0])
        
def part2():
    for i in range(80):
        for j in range(100):
            with open('input.txt') as fp:
                t = fp.readline()
                t = t.split(',')
                t = list(map(int,t))
                t[1] = i
                t[2] = j
                result = process(0,t)
                if result[0] == 19690720:
                    print(result[0],i,j,100*i+j)
                    return
#part1()               
part2()
