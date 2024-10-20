numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
x = len(numbers)
filter=[num for num in numbers if num is not None]
a=sum(filter)
numbers[4] = a / x
print("Измененный список:", numbers)
