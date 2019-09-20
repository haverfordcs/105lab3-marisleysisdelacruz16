Lab 3: Print Traingular Patterns
CS105, Haverford College
Due date: September 24, Midnight | submissions would be accepted through GitHub only unless stated otherwise. 

<replace with your name>

(1) Similar to the previous labs, you have to clone this repository into your local machine (PyCharm-> VCS-> Checkout from Git), 
if you are not sure how to do this, read the general instructions (https://bit.ly/2ZypGeY)

(2) Following are the list of tasks that you have to accomplish:

(a) Develop test cases of your own for all the 8 types of patterns with different number of rows, add your test cases into test_print_the_pattern.txt
Also add test cases that checks for checking pre-conditions as per the restrictions (mentioned below) on number of rows and raise appropriated exceptions

(b) Implement the given function viz. PrintThePattern(number_of_rows, pattern_type) inside the file PrintPatterns.py such that it passes
the test cases avaialable in 

(c) Make sure your implementation passes the test cases provided in test_print_the_pattern.txt

(d) Make sure your code is readable, is well commented, and contains identifiers (names of variables, functions, etc.) that are self explainatory

(e) Submit your code to GitHub (Commit and Push)

PS: You can add your own functions if needed. 

"""

The given function signatured PrintThePattern(number_of_rows, pattern_type), takes two arguments, number_of_rows, and pattern_type.
The "number_of_rows" should be positive integer and in some cases only odd positive integer
The "pattern_type" takes one of the following values
"lower-left", "lower-right", "upper-left", "upper-right",
"top-center", "bottom-center", "left-center", "right-center"

If the supplied pattern_type is other than the above eight options, 
raise an exception (Value Error:) with a message "Pattern not found!"

Examples are given below:

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
 ****
*****

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
