from typing import List, Tuple

def find_single_char_in_list_strs(lst: List[str], c: str) -> Tuple[int, int]:
    for i, s in enumerate(lst):
        if c in s:
            return i, s.find(c)
    return -1, -1

def find_all_char_in_list_strs(lst: List[str], c: str) -> List[Tuple[int, int]]:
    cs = []
    for i, s in enumerate(lst):
        for j, ch in enumerate(s):
            if ch == c:
                cs.append( (i, j) )
    return cs

def is_loc_in_2d_grid(arr: List[str], loc: Tuple[int, int]) -> bool:
    return 0<=loc[0]<len(arr) and 0<=loc[1]<len(arr[0])


def grid_2d(w: int, h: int, c: str) -> List[List[str]]:
    return [[c for _ in range(w+1)] for _ in range(h+1)]

def adjacent(loc: Tuple[int, int]) -> List[Tuple[int, int]]:
    return [(loc[0]+1, loc[1]),(loc[0], loc[1]+1),(loc[0]-1, loc[1]),(loc[0], loc[1]-1)]
