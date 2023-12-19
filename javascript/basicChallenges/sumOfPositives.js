// You get an array of numbers, return the sum of all of the positives ones.

// Example [1,-4,7,12] => 1 + 7 + 12 = 20

// Note: if there is nothing to sum, the sum is default to 0.

function positiveSum(arr) {
  var sum = 0
  for (i = 0; i < arr.length; i++) {
    arr[i] >= 1 ? (sum += arr[i]) : 0
  };
  return sum
};

console.log(positiveSum([1, 2, 3, 4, 5,]));
console.log(positiveSum([1, -2, -3, -4, 5,]));
console.log(positiveSum([1]));
console.log(positiveSum([]));