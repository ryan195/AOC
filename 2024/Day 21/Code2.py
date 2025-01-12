from functools import lru_cache
d1={7:(0,0),8:(0,1),9:(0,2),4:(1,0),5:(1,1),6:(1,2),1:(2,0),2:(2,1),3:(2,2),0:(3,1),-1:(3,2)}
d2={"^":(0,1),"A":(0,2),"<":(1,0),"v":(1,1),">":(1,2)}

@lru_cache
def dp(start, end, limit):
    # print(start + " " + end + " " + str(limit))
    if limit == 25:
        a, b = d2[start]
        c, d = d2[end]
        vertical = ("^" * (a - c)) if a > c else ("v" * (c - a))
        horizontal = ("<" * (b - d)) if b > d else (">" * (d - b))
        str1 = horizontal + vertical + "A"
        str2 = vertical + horizontal + "A"
        if ((start in ["^", "A"]) and (end == "<")):
            return len(str2)
        elif ((start == "<") and (end in ["^","A"])):
            return len(str1)
        else:
            return min(len(str2),len(str1))
    else:
        tot1, tot2 = 0, 0
        a, b = d2[start]
        c, d = d2[end]
        vertical = ("^" * (a - c)) if a > c else ("v" * (c - a))
        horizontal = ("<" * (b - d)) if b > d else (">" * (d - b))
        str1 = horizontal + vertical + "A"
        str2 = vertical + horizontal + "A"
        prev = "A"
        for k in str1:
            tot1 += dp(prev, k, limit+1)
            prev = k
        prev = "A"
        for k in str2:
            tot2 += dp(prev, k, limit+1)
            prev = k
        if ((start in ["^", "A"]) and (end == "<")):
            return tot2
        elif ((start == "<") and (end in ["^","A"])):
            return tot1
        else:
            return min(tot1, tot2)

ans = 0
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst = []
        for char in line:
            if char == "A":
                lst.append(-1)
            elif char != "\n":
                lst.append(int(char))
        prev = -1
        str2 = ""
        # print(lst)
        lst2 = []
        for x in lst:
            if x == "A":
                x = -1
            a,b = d1[prev]
            c,d = d1[x]
            e,f = c-a,d-b
            str1 = ""
            if f < 0:
                str1 += ("<"*abs(f))
            if f > 0:
                str1 += (">"*f)
            if e < 0:
                str1 += ("^"*abs(e))
            if e > 0:
                str1 += ("v"*e)
            str2 = str1[::-1]
            str1 += "A"
            str2 += "A"
            if len(lst2) == 0:
                # if can go left then up
                if not ((prev in [0,-1]) and (x in [1,4,7])):
                    lst2.append(str1)
                # if can go down then right
                if not ((prev in [1,4,7]) and (x in [0,-1])):
                    lst2.append(str2)
            else:
                comb_lst = []
                for y in lst2:
                    if not ((prev in [0,-1]) and (x in [1,4,7])):
                        comb_lst.append(y+str1)
                    if not ((prev in [1,4,7]) and (x in [0,-1])):
                        comb_lst.append(y+str2)
                lst2 = comb_lst
                lst2 = list(dict.fromkeys(lst2))
            prev = x
        # print(lst2)
        val = 1000000000000000000000000000000000000000
        for guess in lst2:
            tota = 0
            prev = "A"
            for key in guess:
                tota += dp(prev, key, 1)
                prev = key
            val = min(val, tota)
        # print(val)
##        for i in range(2):
##            lst3 = []
##            # print(len(lst2))
##            for guess in lst2:
##                prev = "A"
##                lst4 = [""]
##                for key in guess:
##                    combo_lst = []
##                    for thing in lst4:
##                        combo_lst.append(thing + d3[prev][key])
##                    lst4 = combo_lst
##                    prev = key
##                lst3.extend(lst4)
##            lst2 = lst3
##        leng = 1000000000
##        min_length = min(len(path) for path in lst2)
        ans += val * int("".join(map(str, lst[:-1])))
print(ans)
