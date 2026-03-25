#String Manipulator Program
text = input("enter a sentence: ")
print("\n Results:")
print("original:", text)
print("characters (with spaces):", len(text))
print("characters (without spaces):", len(text.replace(" ", "")))
words = text.split()
print("Total words:", len(words))
print("uppercase:", text.upper())
print("lowercase:", text.lower())
print("Title case:", text.title())
#checking for an edge cases
if len(words) > 0:
    print("First word:", words[0])
    print("Last word:", words[-1])
else:
    print("No words entered")
print("Reversed sentence:", text[::-1])