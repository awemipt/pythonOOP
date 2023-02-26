# считывание строки и разбиение ее по пробелам
def isint(s):
    if s.isdigit():
        return True
    if s[0] == '-' and s[1:].isdigit():
        return True
    return False
lst_in = input().split()
print(sum(map(int, filter(isint, lst_in))))