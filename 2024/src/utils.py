

def find_single_char_in_list_strs(lst, c):
    for i, s in enumerate(lst):
        if c in s:
            return i, s.find(c)
    return -1, -1

def find_all_char_in_list_strs(lst, c):
    cs = []
    for i, s in enumerate(lst):
        for j, ch in enumerate(s):
            if ch == c:
                cs.append( (i, j) )
    return cs

def is_loc_in_2d_grid(arr, loc):
    return 0<=loc[0]<len(arr) and 0<=loc[1]<len(arr[0])