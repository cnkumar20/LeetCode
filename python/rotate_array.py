#Rotate array
def rotateArray(a,steps):
    rotated_array = {}
    if(type(a)==type([])):
        steps = steps % len(a)
        rotated_array = a[steps:len(a)]
        rotated_array.extend    (a[0:steps])
    print(rotated_array)
rotateArray([1,2,3,4,5,6],8)