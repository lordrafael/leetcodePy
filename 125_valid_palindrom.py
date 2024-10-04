"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()     # a man, a plan, a canal: panama

        s_without_space = ""    # amanaplanacanalpanama

        for i in range(len(s_lower)):
            if s_lower[i].isalnum():
                s_without_space += s_lower[i]

        i = len(s_without_space) - 1

        reveresed_string = ""

        while i >= 0:
            reveresed_string += s_without_space[i]
            i -= 1

        if s_without_space == reveresed_string:
            return True
        else:
            return False