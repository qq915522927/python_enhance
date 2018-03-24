import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence(object):

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    # def __getitem__(self, index):
    #   return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)

   #def __iter__(self):
   #    for word in self.words:
   #        yield word
   #    return

class SentenceIterator(object):

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self

class LazySentence(object):

    def __init__(self, text)
        self.text = text
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return  (match.group() 
                for match in RE_WORD.finditer(self.text))
