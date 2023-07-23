import os

#delet file
# path = 'text_d.txt'

# if os.path.isfile(path):
#     os.remove(path)

#delet folder
path2 = 'test_fld/B'
if os.path.exists(path2):
    files = os.listdir(path2)
    for file in files:
        print(file)
        path3 = os.path.join(path2, file)
        path3 = path3.replace("\\", "/")
        print(path3)
        if os.path.isfile(path3):
            os.remove(path3)
    os.removedirs(path2)