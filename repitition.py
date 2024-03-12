# # Repetition Statements
# # Data types allowed to be iterated: Lists, Ranges, Sets, Tuple, Dictionaries, Strings

# x = range(5,11)
# petName = ["snowy", "blacky", "bruno"]

# # for loop
# #for(inititialization;condition,increamentation/decre) - JAVA           

# for num in x:
#     print(num)      
# for name in petName[0:2]:
#     print(name)

# # Looping Dictionaries
#     # key: value
    
user = {
    "first_name" : "johhny",
    "last_name" : "Tadea",
    "age" : 25, 
    "average" : 81.76,
    "list_subjects": ["Progamming", "Mathematics", "English"]
}

for key in user:
    print(key, ":", user[key])

#Looping list of Dictionaries
list_of_users = [
    {        
        "first_name" : "johnny",
        "last_name" : "Tadea",
        "age" : 25, 
        "average" : 81.76,
        "list_subjects": ["Progamming", "Mathematics", "English"]
    },
    {
        "first_name" : "rose",
        "last_name" : "Tadea",
        "age" : 23, 
        "average" : 82.54,
        "list_subjects": ["Progamming", "Mathematics", "English"]
    },
    {
        "first_name" : "Angel",
        "last_name" : "Tadea",
        "age" : 27, 
        "average" : 86,
        "list_subjects": ["Progamming", "Mathematics", "English"]
    }
]


for key in list_of_users:
    for x in key:
        print(x, ":", key [x])

#looping in reversed
x = range(1,10)
for i in x[::-1]:
    print(i)
