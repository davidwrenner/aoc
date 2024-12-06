

def find_single_char_in_list_strs(lst, c):
    for i, s in enumerate(lst):
        if c in s:
            return i, s.find(c)
    return -1, -1

def is_loc_in_2d_grid(arr, loc):
    return 0<=loc[0]<len(arr) and 0<=loc[1]<len(arr[0])