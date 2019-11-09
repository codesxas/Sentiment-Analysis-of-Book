from nltk.corpus import stopwords
from string import digits
from nltk.tokenize import RegexpTokenizer as re
from nltk.stem import WordNetLemmatizer 
import PyPDF2, numpy as np


# To extract text from a pdf file (untrained data set)
class LoadBook:
    def __init__(self, book_name):                  # Passing the book name with(out) address
        obj = open(book_name, 'rb')                 # Opening it
        self.reader = PyPDF2.PdfFileReader(obj)     # Reading it
        self.num = self.reader.numPages             # Getting its numbers to read it
        
        print("Total No. of Pages are:-")
        print(self.num)

    def getText(self):
        self.text = ''
        for i in range(self.num):                                       # Extracting text - page-by-page -
            self.text += self.reader.getPage(i).extractText()
            self.text +='\n'
        
        return self.text


    def createSentence(self):
        self.text = self.getText()                                      # Extract Text
        
        self.text = self.text.replace("\n","")                          # Removing new lines ---- just in case ---.
        sentenceList = self.text.split('.')                             # Creating lists based of '.'
        newSentenceList = []                                            # In case of Question Mark ...
        for sentence in sentenceList:
            sentence = sentence.split("?")
            newSentenceList.extend(sentence)

        sentenceList.pop()

        return sentenceList
 
# To extract text from a txt file (trained data set)
class LoadText:

    def __init__(self, text_file):
        obj = open(text_file, 'r')                      # Opening it
        self.text = obj.read()                          # Reading it

    def getText(self):
        self.text = self.text.replace("\n","")          # Removing new lines ---- just in case ---.      
        sentenceList = self.text.split('.#%"')          # Splitting itno sentences
        
        sentenceList.pop()                              # Popping up the last one cause its residual

        return sentenceList
        
        
class PreProcessing:
    def __init__(self, text):
        self.text = text

    def removeNumAndSplChar(self, sentence):
        # Remove Numbers
        remove_digits = str.maketrans('', '', digits)
        sentence = sentence.translate(remove_digits)

        # Remove Special Character
        sentence = sentence.replace("’s", "")
        sentence = sentence.replace("'s", "")
        sentence = sentence.replace("#", " ")


        symbols = "™ˆ˜˚˝˙ˆˇ!\"“”ˆˇ$%&()*+-/:;<=>@[\]^_`~–{|}~\n"
        for i in symbols:
            sentence = sentence.replace(i, '')

        return sentence

    def removeStopword(self, sentence):
        # Remove Stop - Words
        cachedStopWords = stopwords.words("english")                                                # Collecting all the stopwords
        sentences = ' '.join([word for word in sentence.split() if word not in cachedStopWords])    # Removing it from the sentences(list)

        return sentences 

    def tokenize(self):
        # Creating the tokenizer
        tokenizer = re('\w+')
        tokens = []

        # Looping across the list of sentences to convert it into 'list of list'
        for sentence in self.sentences:
            tokens.append(tokenizer.tokenize(sentence))

        return tokens

    def lemmatize(self):
        # Extracting the root words
        lemmatizer = WordNetLemmatizer() 
        words = []

        for sentence in self.sentences:
            word = []
            for _ in sentence:
                word.append(lemmatizer.lemmatize(_))
            words.append(word)

        return words

    def removeMixedWords(self):
        # Removing mixed cases words from list of sentence
        sentences = []
        for sentence in self.sentences:
            words = [word for word in sentence if word.islower()]
            # sentence = [word for word in sentence if word not in words]
            sentences.append(words)
        return sentences
        
    def removeSingleCharacter(self):
        #  Remove single characters
        sentences = []
        for sentence in self.sentences:
            if len(sentence) != 0:
                words = [word for word in sentence if len(word) > 1]
                sentences.append(words)
        return sentences

    def preProcess(self):
        # Compiling it all and giving out the processed food
        self.sentenceList = self.text
        self.sentences = [self.removeNumAndSplChar(sentence) for sentence in self.sentenceList]
        self.sentences = [self.removeStopword(sentence) for sentence in self.sentences]
        self.sentences = self.tokenize()
        self.sentences = self.lemmatize()
        self.sentences = self.removeMixedWords()
        self.sentences = self.removeSingleCharacter()

        return self.sentences

    def display(self):
        self.words = self.preProcess()
        print("The List of Words in the list of sentences:-")
        print(self.words)
        # for sentence in self.sentenceList:
        #     print(sentence)


# textfile = LoadText("C:\\Users\\shrey\\Desktop\\tabs\\Syllabus\\IR\\Project\\ISEAR.txt")
# text_isear = textfile.getText()
# clean = PreProcessing(text_isear)
# clean.display()
