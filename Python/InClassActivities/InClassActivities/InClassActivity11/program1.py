'''
Programmer: Antony Melendez

Description: Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.

Date:11-3-20
'''


def is_palindrome(word):
    string = ""
    for i in range(len(word) - 1, -1, - 1):
        string += word[i]
    if word == string:
        return True
    else:
        return False


def main():
    option = "YES"
    while(option == "YES"):
        word = input(
            "Enter a word and I will tell you if it is palidrome or not: ")

        if (is_palindrome(word) == True):
            print("Word is palidrome")
        else:
            print("Word is not palidrome")
        option = input("Do you wish to try another word? ").upper()


main()
