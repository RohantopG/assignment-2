# sentence take the input.
sentence = input("Enter a sentence: ")

print("\nOriginal:", sentence)


print("Characters (with spaces):", len(sentence))


print("Characters (without spaces):", len(sentence.replace(" ", "")))


words = sentence.split()
print("words:", len(words))


print("Uppercase:", sentence.upper())


print("Lowercase:", sentence.lower())


print("Title Case:", sentence.title())


if len(words) > 0:
    print("First word:", words[0])
else:
    print("First word: None")


if len(words) > 0:
    print("Last word:", words[-1])
else:
    print("Last word: None")


print("Reversed:", sentence[::-1])
