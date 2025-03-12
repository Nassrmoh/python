def sort_numbers():
    num = []
    for x in range(5):
        y = int(input(f"Enter a number {x}: ")) 
        num.append(y)
    num_1 = sorted(num)  # Ascending order
    num_2 = sorted(num, reverse=True)  # Descending order
    print("Ascending order:", num_1)
    print("Descending order:", num_2)
sort_numbers()