str=input()
str=str.lower()
alpha="abcdefghijklmnopqrstuvwxyz"
pangram=True
for char in alpha:
    if char not in str:
        pangram=False
        break
if pangram:
    print("Pangram")
else:
    print("Not Pangram")