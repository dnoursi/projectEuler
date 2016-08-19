## Sum of Squares, Square of Sums
### Problem
The sum of the squares of the first ten natural numbers is,

1<sup>2</sup> + 2<sup>2</sup> + ... + 10<sup>2</sup> = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)<sup>2</sup> = 55<sup>2</sup> = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

### Solution

We should establish basic sum identities:

1 + 2 + ... + n = n(n+1)/2

1<sup>2</sup> + 2<sup>2</sup> + ... + n<sup>2</sup> = n(n+1)(2n+1)/6

Upon inspection, we see that the square of sums is the square of n(n+1)/2 = n<sup>2</sup>(n-1)<sup>2</sup>/4, and the sum of squares is n(n+1)(2n+1)/6.

Taking the difference, we compute (n - 1)n(n + 1)(3n - 2)/12

For n = 100 we have 25164150
