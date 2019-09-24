"""The following function takes two arguments, number_of_rows, and pattern_type
"number_of_rows" should be positive integer and in some cases only odd positive integer
while "pattern_type" takes one of the following values
"lower-left", "lower-right", "upper-left", "upper-right",
"top-center", "bottom-center", "left-center", "right-center"
lower-left: example for number_of_rows = 6
*
**
***
****
*****
******

"lower-right": example for number_of_rows = 5
     *
    **
   ***
 *****
******

"upper-right": example for number_of_rows = 4
****
 ***
  **
   *

"upper-left": example for number_of_rows = 5
*****
****
***
**
*

"top-center": example for number_of_rows = 4
*******
 *****
  ***
   *

"bottom-center": example for number_of_rows = 4
   *
  ***
 *****
*******

"left-center": example for number_of_rows = 5  !! Do you think number_of_rows should always be odd?
Put a check on number_of_rows accordingly for this type of pattern
*
***
*****
***
*

"right-center": example for number_of_rows = 5  !! Do you think number_of_rows should always be odd?
Put a check on number_of_rows accordingly for this pattern
    *
  ***
*****
  ***
    *
"""

def PrintThePattern(number_of_rows, pattern_type):
    # This function will print a pattern as per the arguments i.e. number_of_rows
#lower-left pattern
    if pattern_type == "lower-left":
        for i in range(1, number_of_rows + 1):
            print("*" * i)
#lower-right pattern
    elif pattern_type == "lower-right":
        for i in range(1,number_of_rows+1):
            print (" " *(number_of_rows-i)+"*"*i)
#upper-left pattern
    elif pattern_type == "upper-left":
        for i in range(1, number_of_rows + 1):
            print("" * (i - 1), "*" * (number_of_rows - i + 1))
#upper-right pattern
    elif pattern_type == "upper-right":
        for i in range(1, number_of_rows + 1):
            print(" " * (i - 1), "*" * (number_of_rows - i + 1))
#top-center pattern
    elif pattern_type == "top-center":
        for i in range(1,number_of_rows+1):
            print(" " * (i - 1) + "*" * (number_of_rows - i + 1) + (number_of_rows - i) * "*")
#bottom-center pattern
    elif pattern_type == "bottom-center":
        for i in range(1, number_of_rows + 1):
            print(" " * (number_of_rows - i + 1) + "*" * (i - 1) + i * "*")
#right-center pattern
    elif pattern_type == "right-center":
        # to make the input for number_of_rows odd if it's even
        if number_of_rows % 2 == 0:
            number_of_rows += 1
        # using two different loops to separate the first half of the pattern from the second half of the pattern
        for i in range(1, int((number_of_rows / 2.0) + 1.5)):
            print(" " * (number_of_rows - (i * 2) + 1) + "*" * ((i * 2) - 1))
        for i in range(int((number_of_rows / 2.0) + 0.5), number_of_rows):
            print(" " * ((i * 2) - number_of_rows + 1) + "*" * ((number_of_rows - i) * 2 - 1))
#left-center pattern
    elif pattern_type == "left-center":
        # to make the input for number_of_rows odd if it's even
        if number_of_rows % 2 == 0:
            number_of_rows += 1
        # using two different loops to separate the first half of the pattern from the second half of the pattern
        for i in range(1, int((number_of_rows / 2.0) + 1.5)):
            print("*" * ((2 * i) - 1))
        for i in range(int((number_of_rows / 2.0) + 0.5), number_of_rows):
            print("*" * ((number_of_rows - i) * 2 - 1))
#Exception
    else:
        raise ValueError("Pattern not found!")



