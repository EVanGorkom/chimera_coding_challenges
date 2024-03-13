// Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

// Numerical Score	Letter Grade
// 90 <= score <= 100	'A'
// 80 <= score < 90	'B'
// 70 <= score < 80	'C'
// 60 <= score < 70	'D'
// 0 <= score < 60	'F'
// Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

function getGrade (s1, s2, s3) {
  var avg = ((s1 + s2 + s3) / 3);
  console.log(avg)
  if (avg >= 90 && avg <= 100) {
    return 'A';
  }
  else if (avg >= 80 && avg <= 90) {
    return 'B';
  }
  else if (avg >= 70 && avg <= 80) {
    return 'C';
  }
  else if (avg >= 60 && avg <= 70) {
    return 'D';
  }
  else {
    return 'F';
  };
};

// // Alternative solutions:
// function getGrade (s1, s2, s3) {
//   avg = (s1+s2+s3)/3;
//   if (avg < 60)  return "F";
//     else if (avg < 70) return "D";
//     else if (avg < 80) return "C";
//     else if (avg < 90) return "B";
//     else return "A";
// }

// function getGrade(...scores) {
//   let average = scores.reduce((a, b) => a + b) / scores.length
  
//   if (average >= 90) return 'A'
//   else if (average >= 80) return 'B'
//   else if (average >= 70) return 'C'
//   else if (average >= 60) return 'D'
//   else return 'F'
// }

// function getGrade (s1, s2, s3) {
//   var s = (s1 + s2 + s3) / 3
//   return s >= 90 ? "A" : s >= 80 ? "B" : s >= 70 ? "C" : s >= 60 ? "D" : "F"
// }

console.log(getGrade(95, 90, 93));
console.log(getGrade(85, 80, 88));
console.log(getGrade(80, 70, 70));
console.log(getGrade(25, 85, 96));
console.log(getGrade(20, 30, 40));