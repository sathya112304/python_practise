s=input()
s=s.lower()
alphabet="abcdefghijklmnopqrstuvwxyz"
if all(ch in s for ch in alphabet):
    print("pangram")
else:
    print("Not a pangram")