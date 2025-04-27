from collections import defaultdict,deque

def check_set(list1):
    set1 = set(list1)
    set1.add(5)
    print(set1)
    print("element present") if 8 in set1 else print("Not present")

def check_list(list1):
    list_local = list1
    list_local.append(9)
    list_local.extend([12,15])
    list_local[1] = 100
    list_local.sort()
    print(list_local)
    list_local.append([22,26])
    print(list_local)


def check_dict(dict1:dict) -> None:
    print(dict1.keys())
    print(dict1.values())
    print(dict1.items())
    print("key present") if "name" in dict1.keys() else print("Key not present")
    dict1["test"] = "testvalue"
    print(f"length of dict1 {len(dict1)}")
    print(dict1)

def check_deque(list1):
    dq = deque(list1.copy())
    print(f"pop left {dq.popleft()}")
    print(f"pop right {dq.pop()}")
    dq.reverse()
    print(f"print length and reverse: {dq}")



if __name__ == "__main__":
    set1 = set()
    list1 = list([6,1,9])
    dict1 = dict()
   

    check_set(list1)

    list2 = list1.copy()
    check_list(list2)
    print(f"list1 after copy and operation on list2: \n list1 : {list1} \n list2 : {list2}")
    print("above is example of shallow copy where existing object is reflecting in both list, but extending or adding new element is not")    
    #dict
    dict1["name"] = "nandiesh"
    dict1["age"] = 37
    dict1["year"] = 1988

    check_dict(dict1)

    list2 = list1.copy()
    check_deque(list2)

    print(f"list1 after copy and operation on list2: \n list1 : {list1} \n list2 : {list2}")
