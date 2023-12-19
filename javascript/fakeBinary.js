// Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

// Note: input will never be an empty string

function fakeBinary(x) {
  var bin = ''
  for (i = 0; i < x.length; i++) {
    if (x[i] < 5) {
      bin += '0';
    } else {
      bin += '1';
    };
  };
  return bin
};

// // Alternative Solution:
// function fakeBin(x) {
//   return x.split('').map(n => n < 5 ? 0 : 1).join('');
// }

console.log(fakeBinary('123456789'));