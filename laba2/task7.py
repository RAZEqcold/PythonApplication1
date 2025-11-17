def coconuts(text):
    text = text.lower()
    ccs = "qwrtypsdfghjklzxcvbnm"
    count = 0
    for char in text:
        if char in ccs:
            count += 1
    return count
text = input()
numb = coconuts(text)
print (numb)