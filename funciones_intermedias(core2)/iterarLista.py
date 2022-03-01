student = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(student):
#     for i in student:
#         x = i
#         for k in x:
#             print(f"{k} - {x[k]}")

def iterateDictionary(student):
    for i in range(len(student)):
        for key, value in student[i].items():
            print(key, value)
    

# def iterateDictionary(student):
#     for k in student:
#         x = k
#         y = x['first_name']
#         z = x['last_name']
#         print(f"first_name - {y}, last_name - {z}")

print(iterateDictionary(student))