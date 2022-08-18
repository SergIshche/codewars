dic = {"NORTH": "SOUTH", "EAST": "WEST", "SOUTH": "NORTH", "WEST": "EAST"}

def dirReduc(arr):
    res = []
    for i in arr:
        if res and res[-1]==dic[i]:
            res.pop()
        else:
            res.append(i)
    return res