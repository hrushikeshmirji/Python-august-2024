 # p9 program for math problem 
input_num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 16):
    print('%02d * %02d = %03d' % (input_num, i, input_num * i))
