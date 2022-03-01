student = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        for key, value in some_list[i].items():
            if key == key_name:
                print(value)


iterateDictionary2("last_name", student)

iterateDictionary2("First_name", student)