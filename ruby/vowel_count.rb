# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str)
  string = input_str.downcase
  vowels = ['a', 'e', 'i', 'o', 'u']
  vowel_count = []
  string.each_char do |char|
    vowel_count << char if vowels.include?(char)
  end
  p vowel_count.length
end

# Alternative / Simplified Solution
def get_count(inputStr)
  p inputStr.downcase.count("aeiou")
end

get_count("This is a sentence with a lot vowels for counting.")