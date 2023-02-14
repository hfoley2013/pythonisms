class WordCollection:
    def __init__(self):
        self.words = ['apple', 'banana', 'cherry', 'date']
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return word
        else:
            raise StopIteration

if __name__ == '__main__':
    # Using the WordCollection in a for loop
    wc = WordCollection()
    for word in wc:
        print(word)

    # Using the WordCollection in a list comprehension
    wc = WordCollection()
    words_starting_with_c = [word for word in wc if word.startswith('c')]
    print(words_starting_with_c)
