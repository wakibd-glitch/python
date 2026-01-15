my_dic = {

    'codingal' : 2,
    'is' : 2,
    'the' : 2,
    'best' : 2,
    'way' : 2,
    'to' : 2,
    'learn' : 2,
    'coding' : 1
}

print("the original dictionary: " , str(my_dic))

KEY = 2
result = 0

for key in my_dic:
    if my_dic[key] == KEY:
        result = result + 1

print("frequency of 2 is: " , str(result))