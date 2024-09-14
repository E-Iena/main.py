calls=0


def count_calls():
    global calls
    calls+=0
    return calls


rez_1=count_calls()
print(rez_1)


string=str(input('Введите текст '))
def string_info(*string):
    global calls
    calls+=1
    return string, calls


print(string_info(len(string),string.upper,string.lower))

list_to_search=input('Введите список ')


def is_contain(list_to_search,*string):
    global calls
    calls+=1
    global string
    global list_to_search
    for i in list_to_search:
        fl=True
        if list_to_search(i, len(string))!=string:
            fl=False
    return calls, string, fl
    
    
rez_3=is_contain(string, list_to_search)
print(rez_3)
print(fl)
print(calls)
