#   count_vowels("programming")  # Should return 3
def count_vowels(string):
    return [(i.lower() in ['a', 'e', 'i', 'o', 'u']) for i in list(string)].count(True)

print(count_vowels("programming")) # prints 3