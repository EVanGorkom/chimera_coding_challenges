

# def funcRotate(inputMat):
#     transposed_mat = []
#     rows = len(inputMat)
#     cols = len(inputMat[0])
#     for i in range(cols):
#         new_row = []
#         for j in range(rows):
#             new_row.append(inputMat[j][i])
#         transposed_mat.append(new_row)
    
#     reversed = []
#     for row in transposed_mat:
#         reversed.append(row[::-1])

#     # string = ""
#     # for row in reversed:
#     #     for num in row:
#     #         string += f"{num} "
#     #     string = string.strip() + '\n'

#     # return string
#     rotated_lines = []
#     for row in reversed:
#         rotated_lines.append(" ".join(map(str, row)))
    
#     rotated_string = "\n".join(rotated_lines)
    
#     return rotated_string


# print(funcRotate([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     ]))


# def funcSubstring(inputStr):
#     length = len(inputStr)
#     smallest_palindrome = ""
#     max_length = 0

#     for i in range(length):
#         for j in range(i + 2, length + 1):
#             substr = inputStr[i:j]
#             if substr == substr[::-1] and len(substr) > max_length:
#                 smallest_palindrome = substr
#                 max_length = len(substr)
#             elif len(substr) == max_length and substr < smallest_palindrome:
#                 smallest_palindrome = substr

#     return smallest_palindrome if max_length > 1 else "None"

import pdb

# def funcHopSkipJump(matrix):
#     n = matrix[0][0]  # Number of rows
#     m = matrix[0][1]  # Number of columns
#     visited = [[False] * m for _ in range(n)]  # Initialize visited matrix
#     row, col = 0, 0  # Start from top-left corner
#     direction = "down"  # Initial movement direction

#     while True:
#         visited[row][col] = True  # Mark current cell as visited

#         if direction == "right":
#             if col + 1 < m and not visited[row][col + 1]:
#                 col += 1
#             else:
#                 direction = "down"
#         elif direction == "down":
#             if row + 1 < n and not visited[row + 1][col]:
#                 row += 1
#             else:
#                 direction = "left"
#         elif direction == "left":
#             if col - 1 >= 0 and not visited[row][col - 1]:
#                 col -= 1
#             else:
#                 direction = "up"
#         elif direction == "up":
#             if row - 1 >= 0 and not visited[row - 1][col]:
#                 row -= 1
#             else:
#                 direction = "right"
        
#         # Check if all cells are visited
#         if all(all(row_visited for row_visited in row) for row in visited):
#             break

#     return matrix[row][col]

# # Example usage:
# matrix = [
#     [3, 3],
#     [29, 8, 37],
#     [15, 41, 3],
#     [1, 10, 14]
# ]
# result = funcHopSkipJump(matrix)
# print(result)  # Output: 41



# funcHopSkipJump([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     ])