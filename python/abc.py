def nested_parenthesis_depth(input):
    """Count the maximum depth of parenthesis nesting.

    Examines an input string and reports the deepest level of
    nested parentheses, as an integer.  For example:
        "abc(123(xyz))m(((n)))o" -> 3

    Args:
        input: Any string, which may or may not contain parentheses.

    Returns:
        the highest level of nested parentheses found anywhere in the input.

    Raises:
        ValueError: if the parenthesization is invalid, example: "a)b(c" or "a(b".
    """
    #(())((()))
    inputList = input
    if(len(inputList)==0):
        return 0
        
    maxCount = 0
    #(ab)
    countp = 0
    
    for x in inputList:
        if(x == '('):
            countp += 1
            maxCount= max(maxCount,countp) 
        if(x == ')'):
            countp -=1
            if(countp<0):
                    raise ValueError

    if(countp==0):
        return maxCount
    else:
        raise ValueError
            
print(nested_parenthesis_depth("abc()()d"))
