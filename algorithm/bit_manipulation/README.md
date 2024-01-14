## Bit Manipulation
### Bit Operators
- Bitwise AND (&)
- Bitwise OR (|)
- Bitwise XOR (^)
- Bitwise NOT (!)

### Two's Complement and Negative Numbers
Computers typically store integers in two's complement representation.
- A positive number is represented as itself while a negative number is represented as the two's complement of its absolute value.
- Inverse Every bit and plus 1

### Arithmetic and Logical Right Shift
#### Logical Right Shift (>>>)
- shift the bits and put a 0 in the most significant bit

#### Arithmetic Right Shift (>>)
- shift the bits to the right but fill in the new bits with the value of the sign bit.
- this has the effect of (roughly) dividing by two

### Bit Tasks: Getting and Setting
#### Get Bits
- to find the bit at a particular position (denoted by i) of the given number N.
- to find the Bitwise AND of the given number and 2^i, i.e., (1 << i).
- if the value return is 1, then the bit at the ith position is set (1), otherwise it is unset

#### Set Bits
- to set the bit at a particular position (denoted by i) of the given number N.
- to update the value of given number N to the Bitwise OR of the given number N and 2^i that can be represeneted as (1 << i)
- if the value return is 1 then the bit at the ith position is set. Otherwise, it is unset.

#### Clear Bits
- to clear the bit at a particular position (denoted by i) of the given number N.
- to update the value of the given number N to the Bitwise AND of the given number and the compliment of 2^i, i.e., ~(i << i)