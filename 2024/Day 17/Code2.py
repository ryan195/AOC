##
lst = [2,4,1,3,7,5,0,3,1,4,4,7,5,5,3,0]

def test(a):
    b, c = a%8, 0
    b ^= 3
    c = int(a/(2**b))
    b ^= 4
    b ^= c
    return (b%8)

lst = lst[::-1]
x = 0
y = 0
def recur(a, counter):
    print(a)
    print(counter)
    if counter == len(lst):
        return int(a>>3)
    else:
        for i in range(a, a+8):
            if test(i) == lst[counter]:
                x = recur(i<<3, counter+1)
                if x:
                    return x
        return 0

print(recur(x,y))

##from re import findall
##a, b, c, *prog = [int(n) for n in findall("(\d+)", open("input.txt").read())]
##def run(prog, a):
##    ip, b, c, out = 0, 0, 0, []
##    while ip>=0 and ip<len(prog):
##        lit, combo = prog[ip+1], [0,1,2,3,a,b,c,99999][prog[ip+1]]
##        if prog[ip] == 0: a = int(a / 2**combo)       # adv
##        elif prog[ip] == 1: b = b ^ lit                 # bxl
##        elif prog[ip] == 2: b = combo % 8               # bst
##        elif prog[ip] == 3: ip = ip if a==0 else lit-2  # jnz
##        elif prog[ip] == 4: b = b ^ c                   # bxc
##        elif prog[ip] == 5: out.append(combo % 8)       # out
##        elif prog[ip] == 6: b = int(a / 2**combo)       # bdv
##        elif prog[ip] == 7: c = int(a / 2**combo)       # cdv
##        ip+=2
##    return out
##print("Part 1:", ",".join(str(n) for n in run(prog, a)))
##
##target = prog[::-1]
##def find_a(a=0, depth=0):
##    print(a)
##    print(depth)
##    if depth == len(target):
##        return a
##    for i in range(8):
##        output = run(prog, a*8 + i)
##        if output and output[0] == target[depth]:
##            if result := find_a((a*8 + i), depth+1): 
##                return result
##    return 0
##print("Part 2:", find_a())
