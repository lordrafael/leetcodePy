"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
                                # ["flower","flow","flight"]
        lcp = strs[0]            # flower
        lcp_length = len(lcp)   # 6

        for str in strs[1:]:    # loop starts from flow
                                # if lcp <> the second string 
            while lcp != str[0:lcp_length]:
                                # decrease the size of lcp
                lcp_length -= 1
                if lcp_length == 0:
                    return ""
                
                lcp = lcp[0:lcp_length]
            
        return lcp



                

        