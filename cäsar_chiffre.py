offset = int(input("Offset: "))
string = input("Text: ")

# ord() chr()
# char.isAplpha
# 97 - 122

result = ""
for a in string:
    result += chr(ord(a) + offset)
    
original = ""
for a in result:
    original += chr(ord(a) - offset)

print(result)
print(original)

