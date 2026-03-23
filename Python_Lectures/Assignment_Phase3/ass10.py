'''Q10. Ask the user for a string and print:
• All unique characters
• The count of unique characters'''

text = input("Enter a string: ")

unique_chars = []

for ch in set(text):
    if text.count(ch) == 1:
        unique_chars.append(ch)

print("Unique characters:", unique_chars)
print("Count:", len(unique_chars))