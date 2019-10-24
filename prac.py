# code to print pairs of numbers in the list whose product is even and whose sum is odd
input_list = input("Enter a list of integers(add spaces between different numbers): ")
input_list = input_list.split()
input_list = [int(item) for item in input_list]

final_list = list()

for i in range(len(input_list)):
    for j in range(len(input_list)):
        if i != j:
            product = input_list[i] * input_list[j]
            sum_of_items = input_list[i] + input_list[j]

            if product % 2 == 0 and sum_of_items % 2 != 0:
                final_list.append([input_list[i], input_list[j]])

print(final_list)
