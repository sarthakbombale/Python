def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

def get_factorial(number):
    if number == 1:
        return 1
        
    return number * get_factorial(number - 1)
print(get_factorial(5))

def get_fibonacci(position):

    if position == 0:
        return 0
    if position == 1:
        return 1
    
    return get_fibonacci(position - 1) + get_fibonacci(position - 2)

print(get_fibonacci(6))

def sum_list(number):
    if len(number) == 0:
        return 0
    else:
        return number[0] + sum_list(number[1:])
my_list=[1,2,3,4,5]
print(sum_list(my_list))

def multiply_list(number):
    if len(number) == 0:
        return 1
    else:
        return number[0] * multiply_list(number[1:])
my_multiply_list = [1,2,3,4,5]
print(multiply_list(my_multiply_list))

def count_items(items):
    if len(items) == 0:
        return 0
    else:
        return 1 + count_items(items[1:])
my_list_items = ["banana","nana","na"]
print(count_items(my_list_items))

def get_power(base, exponent):
    if exponent == 0:
        return 1
    return base * get_power(base, exponent - 1)

print(get_power(2, 3))

def reverse_string(text):
    if len(text) == 0:
        return text
    return text[-1] + reverse_string(text[:-1])

print(reverse_string("hello"))

def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(1234))

def count_vowels(text):
    if not text:
        return 0
    is_vowel = 1 if text[0].lower() in "aeiou" else 0
    return is_vowel + count_vowels(text[1:])

print(count_vowels("python"))

def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    sub_max = find_max(numbers[1:])
    return numbers[0] if numbers[0] > sub_max else sub_max

print(find_max([3, 8, 1, 9, 2]))
def multiply_list(numbers):
    if len(numbers) == 0:
        return 1
    return numbers[0] * multiply_list(numbers[1:])

print(multiply_list([1, 2, 3, 4]))

def get_factorial(n):
    if n <= 1:
        return 1
    return n * get_factorial(n - 1)

print(get_factorial(5))

def reverse_list(items):
    if len(items) == 0:
        return items
    return [items[-1]] + reverse_list(items[:-1])

print(reverse_list(["a", "b", "c"]))

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(54321))

def remove_vowels(text):
    if not text:
        return ""
    char = "" if text[0].lower() in "aeiou" else text[0]
    return char + remove_vowels(text[1:])

print(remove_vowels("javascript"))

def find_min(numbers):
    if len(numbers) == 1:
        return numbers[0]
    sub_min = find_min(numbers[1:])
    return numbers[0] if numbers[0] < sub_min else sub_min

print(find_min([5, 2, 9, 1, 7]))
