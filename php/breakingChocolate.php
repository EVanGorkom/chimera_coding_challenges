<!-- Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.

For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, but for size 3 x 1 you must do two breaks.

If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer. -->

<?php

function breakChocolate ($n, $m) {
  return $n * $m - 1;
};

echo breakChocolate(3, 4); // 11
echo '<br>';
echo breakChocolate(5, 5); // 24

/*
3x5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
15 area
14 starting with rows
14 starting with cols

5x5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
25 units
24 minimum breaks
*/