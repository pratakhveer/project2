def functions():
    file1 = input("paste the path for file 1:")
    file2 = input("paste the path for file 2:")

    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file2, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a)

    print(data_a, ",", data_b)


functions()
