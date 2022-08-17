def isPalindrome(s: str) -> bool:
    '''
    Checks if a string is a palindrome.

    Returns: True if the string is a palindrome, False otherwise.

    '''
    return s == s[::-1]

def longestPalindrome1(s: str) -> str:
    '''
    Finds the longest palindrome in a string.

    Returns: The longest palindrome in the string.
    '''
    longest = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            if isPalindrome(s[i:j+1]):
                if len(s[i:j+1]) > len(longest):
                    longest = s[i:j+1]
    return longest



# different algorithm, it searches strings and decreases string length each time
# when there are no palindromes it will return the first letter of the word

def longestPalindrome2(s: str) -> str:
    testLen = len(s)
    for l in range(testLen, 0, -1):
        c=0
        while c+l<=testLen:
            if isPalindrome(s[c:c+l]): return s[c:c+l]
            c+=1



# same function but if the palindrome length < 2 it returns 'none'

def longestPalindrome3(s: str) -> str:
    testLen = len(s)
    for l in range(testLen, 0, -1):
        c=0
        while c+l<=testLen:
            test = s[c:c+l]
            #print(test)
            if (isPalindrome(test) and len(test)>2): return test
            c+=1

    return "none"



print(longestPalindrome3("abcracecarabs"))

palStr = "hello"

