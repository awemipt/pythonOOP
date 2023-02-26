def input_int_numbers():
    nums =  input().split()
    ans = []
    for num in nums:
        ans.append(int(num))

    return tuple(ans)
while True:
    try:
        s = input_int_numbers()
    except ValueError:
        pass
    else:
        break
print(*s)

