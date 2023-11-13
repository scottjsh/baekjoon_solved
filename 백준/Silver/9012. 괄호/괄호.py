count = int(input())

i=0
while i < count:
    a = input()
    i += 1
    if a[0] == ")" or a[-1] == "(":
        print("NO")
    else:
        while True:
            if "()" in a:
                a = a.replace("()", "")
                if a == "":
                    print("YES")
                    break
            else:
                print("NO")
                break