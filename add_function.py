def add_function(value1, value2):
    total_sum = value1 + value2
    return total_sum

answer = add_function(8, 9)
print(answer)

answer1 = add_function(2, 4)
answer2 = add_function(1, 7)
answer3 = add_function(2, 5)
answer4 = add_function(2, 1)

my_nums = 2, 4
# answer5 = add(*my nums)


# this is packing them into a tuple, using the * allows you to pass an unlimited number of arugments
def add(*numbers):
    answer = 0
    for num in numbers:
        answer+= num
    return answer

print(add(2, 4, 6, 8, 10))