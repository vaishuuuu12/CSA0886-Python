def convert_to_numeric(input_str):
    try:
        num = int(input_str)
        return num
    except ValueError:
        return "an error has occurred"
input_str_1 = "S"
output_1 = convert_to_numeric(input_str_1)
print(output_1)
input_str_2 = "a"
output_2 = convert_to_numeric(input_str_2)
print(output_2)
