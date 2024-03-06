import random

number_list = []

for i in range(12):
    random_number = random.randint(0, 99)
    
    inserted = False
    for j in range(len(number_list)):
        if random_number < number_list[j]:
            number_list.insert(j, random_number)
            inserted = True
            break
    if not inserted:
        number_list.append(random_number)
    
    print(f'value3 = {number_list}')