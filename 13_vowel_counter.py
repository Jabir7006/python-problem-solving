vowels = ['a','e','i','o','u']

def count_vowels(word):
    word = word.strip().lower()
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

print(count_vowels('Hello'))