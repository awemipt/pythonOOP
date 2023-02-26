lst_in = input().split()

def to_value(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return x
lst_out = list(map(to_value, lst_in))