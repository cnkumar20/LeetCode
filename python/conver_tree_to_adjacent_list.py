'''
    Given a start node in a binary tree find the number of minutes it takes to be infected completely/burning tree , at every minute spreads to left,right and parent from a start node
'''

from collections import deque

def convert(current_node,parent,dict_map):
    if current_node == None:
        return
    if current_node.val not in dict_map:
        dict_map[current_node.val] = set()
    adjacent_list = dict_map[current_node.val]
    
    if parent!=0:
        adjacent_list.add(parent)
    if current_node.left:
        adjacent_list.add(current_node.left.val)
    if(current_node.right):
        adjacent_list.add(current_node.right.val)

    convert(current_node.left,current_node.val,dict_map)
    convert(current_node.right,current_node.val,dict_map)

def amount_of_time(root,start ) -> int:
    tree_map= {}
    convert(root,0,tree_map)
    queue = deque([start])
    minute = 0
    visited = {start}

    while queue:
        len_size = len(queue)
        while len_size >0:
            current = queue.popleft()
            for num in tree_map[current]:
                if num not in visited:
                    visited.add(num)
                    queue.append(num)
            len_size -=1
        minute +=1
    return minute-1


