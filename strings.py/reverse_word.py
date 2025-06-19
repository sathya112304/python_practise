#reverse the word
def reverse(sentence):
    sentence=sentence.split(".")
    return ' '.join(sentence[::-1])
    
sentence=input()
print(reverse(sentence))