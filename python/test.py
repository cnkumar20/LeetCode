'''

well there are main thing to take first

=> arr = [3,4,5,6]
=> arr2 = [5,3,6,7]


cur_cost = 0 


i = 0
cur_cost += 3-5 => -2 => index = 0+1, cur_cost = 0 and over_by = abs(-2)

i=1
cur_cost += 4-3=>1 

i=2
cur_cost(1) += 4-3 => 2 cur_cost = 2 

...
...


cur_cost =3 , index=1 and cur_cost >= over_by => index

or 



'''


dict_1 = dict()

dict_1['name'] = "kumar"
dict_1['age'] = 35

for k in dict_1:
    print(dict_1[k])

try:
    dict_1['lame']
except KeyError as k:
    print(k)
