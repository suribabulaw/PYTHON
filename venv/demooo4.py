no_1 = 10
no_2 = 2
def add():
    return no_1 + no_2
def sub():
    print(add())
    return no_1 - no_2
def div():
    print(sub())
    return no_1 / no_2
def malti():
    print((div()))
    return no_1*no_2
print(malti())