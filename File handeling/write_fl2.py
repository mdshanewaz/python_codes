user_data = [
    {
        'file_name' : 'user_1.txt',
        'context' : "Hello this from user 1"
    },

    {
        'file_name' : 'user_2.txt',
        'context' : "Hello this from user 2"
    },

    {
        'file_name' : 'user_3.txt',
        'context' : "Hello this from user 3"
    }
]

i = 0
# while i < len(user_data):
#     data = user_data[i]['context']
#     print(data)
#     i += 1


while i < len(user_data):
    with open(user_data[i]['file_name'], 'w') as files:
        data = user_data[i]['context']
        files.write("{}".format(data))
    i += 1