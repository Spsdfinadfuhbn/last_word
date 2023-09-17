def kol_chisel(a):
    n = len(a)
    tmp = 0
    for i in ''.join(reversed(a)):
        if i != " ":
            tmp += 1
        else:
            return tmp


a = "asdasf aasfa fakamfokm"
print(kol_chisel(a))
