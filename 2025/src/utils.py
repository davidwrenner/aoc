from typing import List, Tuple

def find_single_char_in_list_strs(lst: List[str], c: str) -> Tuple[int, int]:
    for i, s in enumerate(lst):
        if c in s:
            return i, s.find(c)
    return -1, -1

def is_loc_in_2d_grid(arr: List[str], loc: Tuple[int, int]) -> bool:
    return 0<=loc[0]<len(arr) and 0<=loc[1]<len(arr[0])
