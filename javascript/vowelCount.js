// Return the number (count) of vowels in the given string.
// We will consider a, e, i, o, u as vowels for this Kata (but not y).
// The input string will only consist of lower case letters and/or spaces.

function getCount(str) {
  let count = 0;
  const vowels = ['a', 'e', 'i', 'o', 'u'];

  for (i = 0; i < str.length; i++) {
    for (v = 0; v < vowels.length; v++) {
      if (str[i].toLowerCase() == vowels[v]) {
        count += 1;
      }
    }
  }

  return count;
}

//// Alternative Solution:
// function getCount(str) {  
//   return (str.match(/[aeiou]/ig) || []).length;
// }

console.log(getCount("This is a long sentence with lots of vowels for counting."))