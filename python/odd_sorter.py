# Task
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
  odds = sorted((num for num in source_array if num % 2 != 0))
  final = [odds.pop(0) if num % 2 != 0 else num for num in source_array]
  return final

print(sort_array([9, 2, 7, 4, 5, 6, 3, 8, 1])) # expect [1, 2, 3, 4, 5, 6, 7, 8, 9]



# Original Attempt:
# def sort_array(source_array):
#   replacement_array = []
#   list_num = 0
#   for number in source_array:
#     if ((number % 2) != 0):
#       source_array.remove(number)
#       source_array.append('i')
#       # list_num += 1
#       # pdb.set_trace()

#       # replacement_array.append(number)
#       # replacement_array.sort()
#   return source_array
#   return replacement_array