def generate_multiplication_table(input_number):
    list_1 = []
    for i in range(1, input_number + 1):
        list_2 = []
        for j in range(1, i + 1):
            list_2.append(i * j)
        list_1.append(list_2)
    return list_1
input_number = int(input("Write a number from 1 to 10: "))
result = generate_multiplication_table(input_number)
print(result)