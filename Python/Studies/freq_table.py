import math
import statistics

def solve(*numbers):
     R = max(numbers) - min(numbers)
     c = 1 + (round((3.322 * math.log(len(numbers), 10)), 2))
     i = math.ceil(R / c)

     list_numbers = list(numbers)
     list_numbers.sort()
     print(list_numbers)

     print("R = " + str(R))
     print("c = " + str(c))
     print("i = " + str(i))

     mean = statistics.mean(numbers)
     median = statistics.median(numbers)
     mode = statistics.mode(numbers)
     sd = round(statistics.stdev(numbers), 2)
     variance = round(statistics.variance(numbers), 2)

     min_number = min(numbers)
     max_number = max(numbers)

     print(f'Min = {min_number}, Max = {max_number}')

     print(f'mean = {mean}, median = {median}, mode = {mode}, sd = {sd}, variance = {variance}')

     count1 = 0
     count2 = 0
     count3 = 0
     count4 = 0
     count5 = 0
     count6 = 0


     for i in numbers:
        if(i >= 4 and i <= 13):
            count1 += 1
        elif(i >= 14 and i <= 23):
            count2 += 1
        elif (i >= 24 and i <= 33):
            count3 += 1
        elif (i >= 34 and i <= 43):
            count4 += 1
        elif (i >= 44 and i <= 53):
            count5 += 1
        elif (i >= 54 and i <= 63):
            count6 += 1
        else:
            print("none")

     print(f'4 - 13: {count1}')
     print(f'14 - 23: {count2}')
     print(f'24 - 33: {count3}')
     print(f'34 - 43: {count4}')
     print(f'44 - 53: {count5}')
     print(f'54 - 63: {count6}')





solve(8, 12, 63, 16, 47, 17, 13, 14,
      13, 37, 12, 22, 14, 24, 24, 43,
      23, 4, 11, 7, 46, 41, 35, 38,
      28, 22, 13, 15, 11, 48, 12, 43)





