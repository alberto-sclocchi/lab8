#Problem 1

def print_backwards(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + print_backwards(string[:-1])

# print(print_backwards("Hello, world!"))

#Problem 2

def format_names(list_names):
    if len(list_names) == 0:
        return []
    else:
        if "," not in list_names[-1]:
            name = list_names[-1].split(" ")
            formatted_name = name[1] + ", " + name[0]
        else:
            formatted_name = list_names[-1]


        return  format_names(list_names[:-1]) + [formatted_name]


#print(format_names(["Allen Anderson", "Bruce Baker", "Cook, Claire", "Dunn, David"]))

#Problem 3

def sum_a(data):
    sum_values = 0
    for item in data:
        for key, value in item.items():
            if key == "a":
                sum_values += value

    return sum_values

#example_data = [
#     {"a": 2, "b": 3, "c": 1},
#     {"b": 2, "c": 3},
#     {"a": 1, "b": 2, "c": 3},
#     {"a": 3, "b": 2, "c": 1},
#     {"c": 1, "a": 4},
#]
#
#print(sum_a(example_data))

#Problem 4

def process_list(nums_list):
    even_list = []
    odd_list = []

    for index, num in enumerate(nums_list):
        if index % 2 == 0:
            even_list.append(str(num))
        else:
            odd_list.append(num * 10)

    return even_list + odd_list

#print(process_list([0, 1, 2, 3, 4, 5, 6, 7]))
#print(process_list([9,8,7,6,5,4,3,2,1]))





