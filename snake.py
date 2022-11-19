# Current Code is for Snake Game 1D version
# Telerik exam - exercise 2

number_of_snake_jumps = input().split(" ")

size_of_the_snake = int(number_of_snake_jumps[0])
jumps_left_of_the_snake = int(number_of_snake_jumps[1])

fruits_to_be_eaten = input().split(" ")
fruits_counter = []
path_counter = []
for numbers in fruits_to_be_eaten:
    fruits_counter.append(int(numbers))

for current_fruit in fruits_counter:
    if current_fruit == 0:
        continue
    elif current_fruit == 1:
        if size_of_the_snake > 0:
            size_of_the_snake += 1
        elif size_of_the_snake <= 0:
            path_counter.append(current_fruit)
    elif current_fruit == -1:
        if jumps_left_of_the_snake > 0:
            jumps_left_of_the_snake += -1
            path_counter.append(current_fruit)
        elif jumps_left_of_the_snake <= 0:
            size_of_the_snake += -1

print(f"{size_of_the_snake} {sum(path_counter)}")




