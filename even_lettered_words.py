sentence = "My name is Kumar Appu"
def even_length(sentence):
   i = sentence.split()
   for j in i:
    if len(j)%2 ==0:
        print(j);
print("even number of letters in the sentence: ");
even_length(sentence)