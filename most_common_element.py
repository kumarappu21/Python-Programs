from collections import Counter
def most_common_elements(text):
    characters = list(text)
    counter = Counter(characters)
    most_common=counter.most_common()
    return most_common;
text='hello world';
print("most common elements and their counts: ", most_common_elements(text));
