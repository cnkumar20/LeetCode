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


