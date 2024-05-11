'''
Time Complexity - O(1), we are only checking the first 7 characters if we go beyond that we are breaching the limits of int
Space Complexity - O(1)

Works on Leetcode
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        s= s.strip() #remove the spaces
        if s== None or len(s) == 0: #blank string or Null
            return 0
        sign = True #assume positive
        if s[0] == '-':#if first char - make sign false it denotes -ve
            sign = False 
        if not s[0].isnumeric() and (s[0] != '+' and s[0] != '-'): #if first character not numeric and not a sign return 0
            return 0
        result = 0 
        limit = int((2**31-1)/10) #set limit to max of int / 10
        print(f"Lmit: {limit}")
        for i in range(len(s)):
            ch = s[i]
            if ch.isnumeric(): #if character is numeric
                if sign:
                    if result > limit: #check we are within int limit
                        return 2**31 - 1
                    elif result == limit and ord(ch) - ord('0') >= 7: #if we are at limit and the next digit is greater than 7 return maxInt
                        return 2**31 - 1
                else:
                    if result > limit: #check we are within int limit
                        return (2**31)*(-1)
                    elif result == limit and ord(ch) - ord ('0') >=8: #if we are at limit and the next digit is greater than 8 return minInt for -ve
                        return (2**31)*(-1)
                result = result*10 + ord(ch)-ord('0') #convert the character to an integer
            elif  i != 0: #break if we encounter any other character other than number when we are not at first character
                break
        return result if sign else result*-1 #return +ve if sign is True else return -ve

        
        