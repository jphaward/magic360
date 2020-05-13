import time
from datetime import datetime
import pandas as pd

x1 = 1.000000001
x2 = 2

def Project360(input_num):
	magic_num = input_num*60
	# Keep adding the character ints of magic_num together until only one chracter is left
	# z = 0 
	# for num in str(magic_num):
	# 	z += int(num)
	# if z % 9 == 0:
	# 	return 9
	# else:
	# 	return z % 9
	if magic_num % 9 == 0:
		return 9
	else:
		return magic_num % 9

def Project360_1(input_num):
	magic_num = input_num*60
	# Keep adding the character ints of magic_num together until only one chracter is left 
	while len(str(magic_num)) != 1:
		magic_num = remove_zeroes(magic_num)
		if len(str(magic_num)) == str(magic_num).count("9"):
			magic_num = 9
		else:
			magic_num = remove_nines(magic_num)
		magic_num = make_it_more_magical(magic_num)
	else:
		return magic_num

def make_it_more_magical(magic_num):
	# alwats starts at 0 when adding together a new set of character ints
	more_magic_num = 0

	# for each character int in magic_num, add them together onto more_magic_num
	for num in str(magic_num):
		more_magic_num += int(num)
		# print(str(more_magic_num - int(num)) + " + " + str(num) + " = " + str(more_magic_num))
	return more_magic_num

def how_many_decimal_places(input_num):
	if "." in str(input_num):
		num, decimal_places = str(input_num).split(".")
		return len(decimal_places)
	else:
		return 0

def remove_nines(x):
	return int(str(x).replace("9", ""))

def remove_zeroes(x):
	return int(str(x).replace("0", ""))

start_time = datetime.now()

decimal_len = max(how_many_decimal_places(x1), how_many_decimal_places(x2))
c = 10**decimal_len
print(c)

start_x = int(x1*c)
end_x = int(x2*c)

print(start_x)
print(end_x)

magic_num_list = []

while start_x <= end_x:
	# start_x_list = []
	magic_num = Project360(start_x)
	# start_x_list = [start_x/c, magic_num]
	# magic_num_list.append(start_x_list)

	if magic_num != 3 and magic_num != 6 and magic_num != 9:
		print(magic_num)
		break
	# else:
	# 	print(str((start_x/c)) + ": " + str(magic_num))

	start_x += 1

# df = pd.DataFrame(magic_num_list)

# print(df)
end_time = datetime.now() - start_time
print(end_time)

# b = "99919"
# print(b.count("9"))
# print(len(b))
