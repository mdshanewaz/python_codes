with open('text_f.txt', 'a') as file:
    my_lst = ["list 1\n", "list 2\n", "list 3\n"]
    file.write("This is from the write_f.py for not over witting.\n")
    file.writelines(my_lst)