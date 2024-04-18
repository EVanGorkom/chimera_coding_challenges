# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:

def canConstruct(ransomNote, magazine):
    # hash solution
    mag_dic = {}
    for letter in magazine:
        if letter in mag_dic:
            mag_dic[letter] += 1
        else:
            mag_dic[letter] = 1

    for letter in ransomNote:
        if letter not in mag_dic or mag_dic[letter] == 0:
            return False
        else:
            mag_dic[letter] -= 1
    return True


# Testcase
def test_canConstruct():
    assert(canConstruct("a", "b") == False)
    assert(canConstruct("aa", "ab") == False)
    assert(canConstruct("aa", "aab") == True)


### Big O
# We get the info instantly == O(1)
# If the length of the new object is the same as the value given == O(n)
# One `for` loop == O(n)
# Nested `for` loops == O(n^(per nested for loop))

## Time complexity
# O(n)

## Space complexity
# O(n)