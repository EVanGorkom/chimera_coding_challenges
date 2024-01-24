# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(input)
  array = input.split
  modified_words = array.map do |word|
    if word =~ /\w/
      word[1..-1] + word[0] + 'ay'
    else
      word
    end
  end
  modified_words.join(' ')
end

p pig_it("Pig latin is cool")
p pig_it("Hello world !")