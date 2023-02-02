#!/usr/bin/env python3
def sort_items(items):
    if len(items) == 1:
        mark, k, v = items[0]
        return {f"{mark} {k}" if mark != "" else k: filt(v)}

    sorted_items = sorted(items, key=lambda x: x[1])
    prev_item = ["", "", ""]
    
    for num, x in enumerate(sorted_items):
        if x[1] == prev_item[1] and prev_item[0] == "+":
            sorted_items[num-1] = x
            sorted_items[num] = prev_item
        prev_item = x

    sort_list = {f"{mark} {k}" if mark != "" else k: filt(v) for mark, k, v in sorted_items}

    return sort_list

def filt(z):
    if z == None:
        return "null"
    if isinstance(z, bool):
        return str(z).lower()
    else:
        return z
    
    
