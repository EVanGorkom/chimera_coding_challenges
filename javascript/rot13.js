// ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

// Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

function rot13(message){
  let final = '';

  for (i = 0; i < message.length; i++) {
    let charCode = message.charCodeAt(i);
    if (charCode >= 65 && charCode <= 90) {
      charCode += 13
      if (charCode > 90) {
        charCode = (65 + (charCode - 91))
      };
    }
    else if (charCode >= 97 && charCode <= 122) {
      charCode += 13
      if (charCode > 122) {
        charCode = (97 + (charCode - 123))
      };
    };
    final += String.fromCharCode(charCode);
  };
  return final;
}

console.log(rot13("NARTUO")) // 65 - 90
console.log(rot13("naruto")) // 97 - 122