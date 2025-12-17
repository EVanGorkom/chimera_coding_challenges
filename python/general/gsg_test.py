# This is a demo task.

# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
  positives = []
  for i in A:
    if i > 0:
      positives.append(i)

  lowest_num = 1
  while lowest_num in positives:
    lowest_num += 1

  return lowest_num

array = [1, 2, 3, 5, 6, 7] #Should return 4
array1 = [-1, -2, -3, -5, -6, -7] #Should return 4
print(solution(array))
print(solution(array1))