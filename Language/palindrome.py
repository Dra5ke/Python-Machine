def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) == 1:
        return True
    if not first(word) == last(word):
        return False
    return is_palindrome(middle(word))

word = str(input('Write a palindrome:\n'))

print(first(word))
print(middle(word))
print(last(word))

print(len(word))

print(is_palindrome(word))