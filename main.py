import os


def userpath():
    while True:
        path = "C:\\abc"
        if os.path.exists(path):
            break
        else:
            print("Вы не правильно ввели путь")
    return path

def dict(path):
    dict1 = {}
    for i in os.listdir(path):
        if os.path.isdir(path + i):
            dict1[path + "\\" + i] = os.path.getsize(path + "\\" + i)
        else:
            dict(path + "\\" + i)
    print(dict) 
           

def dubl():
    pass

def console():
    pass

dict(userpath())


# a = {
#     1:41,
#     2:22,
#     3:3
# }
# a[1] = "gssefd"
# print(a[])

