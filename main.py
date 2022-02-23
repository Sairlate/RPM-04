import os

dict1 = {}


def userpath():
    while True:
        path1 = 'C:\\abc'
        if os.path.exists(path1):
            break
        else:
            print("Вы не правильно ввели путь")
    return path1


def dict(path):
    for i in os.listdir(path):
        file = os.path.join(path, i)
        if os.path.isdir(file):
            dict(file)
        else:
            dict1[file] = os.path.getsize(file)
    return dict1


def dubl(dict1):
    name = []
    weight = []
    for a in dict1.keys():
        name.append(os.path.basename(a))
    for b in dict1.values():
        weight.append(b)
    double = {}
    for i in range(len(name)):
        count = 0
        for j in range(len(name)):
            if name[i] == name[j]:
                if weight[i] == weight[j]:
                    count += 1
                double[name[i]] = count
    print(double)
    print(name)
    print(weight)
    return double


def console(double):
    for a, b in double.items():
        if b > 1:
            print(a + ': ' + str(b))


if __name__ == '__main__':
    (console(dubl(dict(userpath()))))
