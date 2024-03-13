// Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

function evenOrOdd(num) {
  return ((num % 2 == 0) ? "Even" : "Odd");
};

console.log(evenOrOdd(2));
console.log(evenOrOdd(3));
console.log(evenOrOdd(4));
console.log(evenOrOdd(5));