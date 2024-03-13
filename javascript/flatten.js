// # The flatten method on Array squishes any nested arrays into the outer array like this:

// # > [[1,2],[3,[4,5]]].flatten
// # => [1, 2, 3, 4, 5]
// # JavaScript does not have a 'flatten' method. In ES6, you could deconstruct the array (...) and use concat to do something similar.

// # > [].concat.apply(...[[1,2],[3,[4,5]]])
// # => [1, 2, 3, 4, 5]
// # The object of this exercise is to recreate the functionality of the flatten method that we have in Ruby's Array class.

// # Implement a CustomArray class that works like this:

// # Ruby

// # > c = CustomArray.new([[1,2],[3,[4,5]]])
// # > c.flatten
// # => [1, 2, 3, 4, 5]
// # JavaScript

// # > let c = new CustomArray([[1,2],[3,[4,5]]])
// # > c.flatten
// # => [1, 2, 3, 4, 5]
// # But the CustomArray class may not use the built-in .flatten method or .to_s in Ruby or concat or deconstructing in JavaScript

function customArray(arr) {
  // let result = [];
  // arr.forEach (i => {
  //   if (Array.isArray(i)) {
  //     for (let j = 0; j < i.length; j++) {
  //       result.push(i[j]);
  //     }
  //   }
  //   else {
  //     console.log("error")
  //   }
  // });
  // return result;

  // return arr.reduce((result, element) => {
  //   if (Array.isArray(element)) {
  //     result = result.concat(element)
  //   }
  //   return result
  // }, []);

//   let result = [];
//   arr.forEach((element) => {
//     if (Array.isArray(element)) {
//       result = result.concat(customArray(element));
//     } else {
//       result.push(element);
//     }
//   });
//   return result;

  let result = [];
  let stack = [arr];

  while (stack.length) {
    let current = stack.pop();

    for (let i = 0; i < current.length; i++) {
      if (Array.isArray(current[i])) {
          stack.push(current[i]);
      } else {
          result.push(current[i]);
      }
    }
  }
  return result;
}



console.log(customArray([[1, 2, 3], [4, 5, 6], [7, 8]]))
console.log(customArray([[1, 2, 3], [[4, 5, 6], [7, 8]]]))