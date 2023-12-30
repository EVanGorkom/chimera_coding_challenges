# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# vowels = {'a' => 0, 'e' => 0, 'i' => 0, 'o' => 0, 'u' => 0} #This is more complicated than the problem was asking for.

def get_count(input_str)
  str_array = input_str.downcase.split
  vowels = ['a', 'e', 'i', 'o', 'u']
  vowel_count = 0
  str_array.each do |word|
    vowels.each do |vowel|
      if word.include?(vowel)
        vowel_count += 1
      end
    end
  end
  p vowel_count
end

get_count("This is a sentence with a lot vowels for counting.")