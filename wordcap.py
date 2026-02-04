s = input("Enter a string: ").strip()

if len(s) == 0:
    print("Empty string")
else:
    result = s[0].upper() + s[1:]
    print(result)
