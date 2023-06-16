def palindrome(string):
    return True if string == string[::-1] else False


print(palindrome("helloworld"))
