// Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

// Examples:
// 'abc' =>  ['ab', 'c_']
// 'abcdef' => ['ab', 'cd', 'ef']

function solution(str) {
  if (str.length % 2 != 0) {
    str += '_';
  }
  let final = []
  for (i = 0; i < str.length; i += 2) {
    final.push(str.slice(i, i + 2));
  }
  return final
}

console.log(solution("abc"));
console.log(solution("abcdef"));