def reverse_sentence(sentence):
    words=sentence.split()
    words.reverse()
    return" ".join(words)
sentence="hello python is fun"
reversed_largest=reverse_sentence(sentence)
print("reversed_largest:",reversed_largest)
