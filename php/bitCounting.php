<!-- Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case -->

<?php

function countBits($n) {
  $count = 0;
  $asBinaryString = (string)decbin($n);
  foreach (str_split($asBinaryString) as $digit) {
    if ($digit == 1) {
      $count += 1;
    }
  }
  return $count;
}

echo countBits(10);


//// Simplified Solution:
  // function countBits($n) {
  //   return substr_count(decbin($n), 1);
  // }


//// Chat's definition of the substr_count() function:
// The substr_count() function in PHP is used to count the number of occurrences of a substring within a string. It takes three parameters:

// haystack (string): The string in which you want to search for the substring.
// needle (string): The substring you want to search for within the haystack string.
// offset (int, optional): An optional parameter that specifies the position within the haystack string to start the search. If not provided, the search starts from the beginning of the haystack string.
?>