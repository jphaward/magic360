import time
from datetime import datetime
import pandas as pd

x1 = 1.0000001
x2 = 2

def Project360(input_num):
	# print(input_num)

	# Input number * by 60 and assigns to input_num_60
	input_num_60 = input_num * 60
	# print(input_num_60)

	# removes decimal point from magic_num
	clean_input_num_60 = str(input_num_60).replace('.', '')
	# print(clean_input_num_60)

	# For readability, assigns clean_input_num_60 to magic_num be iterated over.
	magic_num = clean_input_num_60

	# Keep adding the character ints of magic_num together until only one chracter is left 
	while len(str(magic_num)) != 1:
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
	start_x_list = []
	magic_num = Project360(start_x)
	start_x_list = [start_x/c, magic_num]
	magic_num_list.append(start_x_list)

	if magic_num != 3 and magic_num != 6 and magic_num != 9:
		print(magic_num)
		break
	else:
		print(str((start_x/c)) + ": " + str(magic_num))

	start_x += 1

# print(magic_num_list)

df = pd.DataFrame(magic_num_list)

print(df)
end_time = datetime.now() - start_time
print(end_time)
# def convert_number(input_num, iteration_len):
# 	if "." not in str(input_num) and iteration_len > 0:
# 		input_num = str(input_num) + "."

# 	if "." in str(input_num):
# 		num, decimal_places = str(input_num).split(".")
# 		nums_to_add = iteration_len - len(decimal_places)
# 		while nums_to_add > 0 :
# 			input_num = str(input_num) + "0"
# 			nums_to_add -= 1

# 	return int(str(input_num).replace('.', ''))

# def calc_iteration_num(iteration_len):
# 	if iteration_len == 0:
# 		return 1
# 	else:
# 		extra_zeros = ""
# 		while iteration_len-1 > 0:
# 			extra_zeros = extra_zeros + "0"
# 			iteration_len -= 1

# 		return float("0." + extra_zeros + "1")
# iteration_num = calc_iteration_num(iteration_len)
# print(convert_number(x1, iteration_len))
# print(convert_number(x2, iteration_len))
# print(calc_iteration_num(iteration_len))

# while x1 < x2:
# 	print(x1)
# 	x1 += iteration_num


# start_x = convert_number(x1, iteration_len)
# end_x = convert_number(x2, iteration_len)