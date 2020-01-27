id1, id2, id3, id4, id5, id6, id7, id8 = (input("Please input your ID Number: "))

id_int1 = int(id1) * 8
id_int2 = int(id2) * 7
id_int3 = int(id3) * 6
id_int4 = int(id4) * 5
id_int5 = int(id5) * 4
id_int6 = int(id6) * 3
id_int7 = int(id7) * 2
id_int8 = int(id8) * 1

sum = id_int1 + id_int2 + id_int3 + id_int4 + id_int5 + id_int6 + id_int7 + id_int8
confirm = sum % 11

if confirm == 0:
    print("1 (The ID number is valid!)")
else:
    print("0 (The ID number is fake!)")
