# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

def duplicate_encode(word)
  as_array = word.downcase.split("")
  final = ""
  as_array.each do |letter|
    count_value = as_array.count(letter)
    if count_value >= 2
      final << ")"
    else
      final << "("
    end
  end

  return final
end

p duplicate_encode("Vendetta")
p duplicate_encode("Hello")
p duplicate_encode("Nissa")
p duplicate_encode("Chandra")