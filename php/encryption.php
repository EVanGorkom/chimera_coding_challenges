<!-- Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:
encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes. -->

<?php

function encrypt($text, $n)
{
  $array = str_split($text);
  
  for ($i = 0; $i < $n; $i++) {
    $odds = '';
    $evens = '';

    for ($j = 0; $j < count($array); $j++) {
      if ($j % 2 != 0) {
        $odds .= $array[$j];
      } else {
        $evens .= $array[$j];
      }
    }
    $text = $odds . $evens;
    $array = str_split($text);
  }

  return $text;
}

function decrypt($text, $n)
{
  if (empty($text) || $n <= 0) {
    return $text;
  }

  $array = str_split($text);
  $midpoint = (int)(count($array) / 2);

  for ($i = 0; $i < $n; $i++) {
    $decrypted = '';

    for ($j = 0; $j < $midpoint; $j++) {
      $decrypted .= $array[$j + $midpoint] . $array[$j];
    }

    if (count($array) % 2 != 0) {
      $decrypted .= $array[count($array) - 1];
    }

    $array = str_split($decrypted);
  }

  return $decrypted;
}

// Testing the decrypt function
echo decrypt("135024", 1);  // Output: "012345"
echo "\n";
echo decrypt("304152", 2);  // Output: "012345"
echo "\n";
echo decrypt("012345", 3);  // Output: "012345"
echo "\n";


echo encrypt('012345', 1); // '135024'
echo '<br>';
echo encrypt("012345", 2); // "135024"->"304152"
echo '<br>';
echo encrypt("012345", 3); // "135024"->"304152"->"012345"
