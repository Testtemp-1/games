filename = raw_input("enter filename :")
file= open(filename)
line= file.read()
print line
file.close()