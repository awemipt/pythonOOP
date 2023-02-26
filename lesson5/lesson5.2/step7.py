def get_loss(w1, w2, w3, w4):
    y = 1
    try:
        y = 10 * w1 // w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        y = y - 5 * w2 * w3 + w4
    finally:
        return y

print(get_loss(1, 0, 1, 1))