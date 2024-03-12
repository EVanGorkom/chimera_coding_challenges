# Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

# Examples
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"

def to_underscore(string):
    final = ''
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if not isinstance(string, str):
        return f"{string}"
    
    upcase_count = 1
    for char in string:
        if upcase_count == 1:
            upcase_count += 1
            final += char.lower()
        elif char == char.upper() and char not in nums:
            final += '_' + char.lower()
            upcase_count += 1
        else:
            final += char

    return final


print(to_underscore('HelloWorld'))
print(to_underscore('TestController'))
print(to_underscore('MoviesAndBooks'))
print(to_underscore('App7Test'))
print(to_underscore(7))