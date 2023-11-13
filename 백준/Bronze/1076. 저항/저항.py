first = input()
second = input()
third = input()


if first == "black":
    r_first = "0"

elif first == "brown":
    r_first = "1"

elif first == "red":
    r_first = "2"

elif first == "orange":
    r_first = "3"

elif first == "yellow":
    r_first = "4"

elif first == "green":
    r_first = "5"

elif first == "blue":
    r_first = "6"

elif first == "violet":
    r_first = "7"

elif first == "grey":
    r_first = "8"

elif first == "white":
    r_first = "9"



if second == "black":
    r_second = "0"

elif second == "brown":
    r_second = "1"

elif second == "red":
    r_second = "2"

elif second == "orange":
    r_second = "3"

elif second == "yellow":
    r_second = "4"

elif second == "green":
    r_second = "5"

elif second == "blue":
    r_second = "6"

elif second == "violet":
    r_second = "7"

elif second == "grey":
    r_second = "8"

elif second == "white":
    r_second = "9"





if third == "black":
    r_third = "1"

elif third == "brown":
    r_third = "10"

elif third == "red":
    r_third = "100"

elif third == "orange":
    r_third = "1000"

elif third == "yellow":
    r_third = "10000"

elif third == "green":
    r_third = "100000"

elif third == "blue":
    r_third = "1000000"

elif third == "violet":
    r_third = "10000000"

elif third == "grey":
    r_third = "100000000"

elif third == "white":
    r_third = "1000000000"



result1 = f"{r_first}{r_second}"
real_result = int(result1) * int(r_third)
print(real_result)


