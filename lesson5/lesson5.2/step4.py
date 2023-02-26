a, b = input().split()
try:
    c = int(a) + int(b)
except ValueError:
    try:
        c = float(a) + float(b)
    except:
        c = a + b
finally:
    print(c)