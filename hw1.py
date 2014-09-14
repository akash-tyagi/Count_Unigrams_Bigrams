import json #or cjson
import re
from stemming.porter2 import stem
import sys 
class Hw1(object):
    #def __init__():
     #   pass
        
    @staticmethod
    def read_line(a_json_string_from_document):
        #sample answer:
        return json.loads(a_json_string_from_document)
        
    
    @staticmethod
    def tokenize(string):
        #----your code----
        string = string.lower().encode("ascii")
        regEx = re.compile('\w*')
        words = regEx.findall(string)
        words = filter(None, words)


        #return a list of words
        return words
    
    
    @staticmethod
    def stopword(a_list_of_words):
        #----your code----
        infile_name='./stop_word'
        file = open(infile_name,'r')
        string = ""
        for line in file:
            string = string + line
        stop_words = Hw1.tokenize(string)
       
        #return a list of words and the words ordering is not preserved
        return [word for word in a_list_of_words if word not in stop_words]
    
    
    @staticmethod
    def stemming(a_list_of_words):
        #----your code----
        
        #return a list of words
        return map(stem,a_list_of_words)
    
    
    def unigram_count(self, a_document_name):
        #TO NOTE, for this function, it's an default instance method, 
        #in contrast to static method. When calling the function, you need to declare a class instance first.
        #----your code-----
        f = open(a_document_name, 'r')
        words = []
        
        for line in f:
            line = Hw1.read_line(line)['text']
            words.extend(Hw1.stopword(Hw1.tokenize(line)))
        
        freq = {}
        for word in words:
           freq[word] = freq.get(word, 0) +1
        
        freq = sorted(freq, key=freq.get, reverse=True)

        #return top 20 unigrams e.g. {[hot,99],[dog,66],...}
        return freq[:20]
    
    
    def bigram_count(self,a_document_name):
        #-----your code-----



        #return top 20 bigrams and frequency pairs, e.g. {[hot dog,88],[apple pie,54],...}
        pass


if __name__ == '__main__':
    pass
    #hw=Hw1()
    #your
