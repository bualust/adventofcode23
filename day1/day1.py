import os

filename = "input"

with open(filename) as data:
    input_data = data.readlines()

first_answer = 0

for line in input_data:

    line = line.replace("\n","")
    chars = [int(x) for x in line if x.isdigit()]
    first_and_last = 10*chars[0]+chars[-1]
    first_answer = first_answer+first_and_last

print(f"First answer is {first_answer}")


second_answer = 0
numbers = ["one","1","two","2","three","3","four","4","five","5",
           "six","6","seven","7","eight","8","nine","9"]
numbers_dic = {"one":1,"two":2,"three":3,"four":4,"five":5,
               "six":6,"seven":7,"eight":8,"nine":9,
               "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

for line in input_data:

    line = line.replace("\n","")
    positions = {}
    rpositions = {}
    for num in numbers:
        found = line.find(num)
        rfound = line.rfind(num)
        if found!= -1: positions[found] = numbers_dic[num]
        if rfound!= -1: rpositions[rfound] = numbers_dic[num]

    values = sorted(positions)
    rvalues = sorted(rpositions)
    first_and_last = 10*positions[values[0]]+rpositions[rvalues[-1]]
    second_answer = second_answer+first_and_last


print(f"Second answer is {second_answer}")
