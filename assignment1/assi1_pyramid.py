def print_pyramid (hight):
    for i in range (1, hight+1):
      print (" " * (hight-i) + "*" * i)
print_pyramid (4)