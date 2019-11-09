from pre_processing import LoadBook, LoadText, PreProcessing
import pandas as pd, numpy as np, matplotlib.pyplot as plt

class Analyzing(PreProcessing):
    df = []
    sentence_score = dict()

    def __init__(self, load_text, load_book):
        super(Analyzing, self).__init__(load_text)
        self.sentences_of_text = self.preProcess()          # List of words in a list of sentences  - in case of the trained data set
        self.text_sentences = self.sentenceList             # List of sentences

        super(Analyzing, self).__init__(load_book)
        self.sentences_of_book = self.preProcess()          # List of words in a list of sentences  - in case of the untrained data set
        self.book_sentences = self.sentenceList             # List of sentences


    def createDf(self, df):
        df = df.drop(columns = ['Positive', 'Negative'])
        
        # Giving score to the different emotions
        df['Anger'] = df['Anger'].replace(to_replace = 1, value = -4)
        df['Disgust'] = df['Disgust'].replace(to_replace = 1, value = -3)
        df['Fear'] = df['Fear'].replace(to_replace = 1, value = -2)
        df['Sadness'] = df['Sadness'].replace(to_replace = 1, value = -1)
        df['Surprise'] = df['Surprise'].replace(to_replace = 1, value = 2)
        df['Trust'] = df['Trust'].replace(to_replace = 1, value = 3)

        # Giving a score to each word - based upon different values for emotions
        df['Score'] = df['Anger'] + df['Disgust'] + df['Fear'] + df['Sadness'] + df['Surprise'] + df['Trust'] + df['Joy']
        
        return df

    def findSentenceScore(self, df):
        # Finding the score of sentence with thier emotion 

        for i in range(len(self.sentences_of_text)):                       # Used indices to traverse both -> 'sentences in text_file' and 'The actual sentence'
            # DataFrame of sentence in the trained data set using the emotions excel file
            df1 = df.loc[df['Words'].isin(self.sentences_of_text[i])]
            val = []                                                       # value to the key (actual sentences) in dict ->'sentence_score'
            score = df1['Score'].sum()                                     # Taking the score
            emotion = self.sentences_of_text[i][0]                         # Taking the emotions
            
            val.append(emotion)
            val.append(score)
            self.sentence_score[self.text_sentences[i]] = val              # Providing the value
            
            # Printing out the stuffs 
            print(self.text_sentences[i], end = ' = ')
            print(self.sentence_score[self.text_sentences[i]])
            # self.df = self.df.append(df1, ignore_index = True)
            print(df1)            




    def analyze(self):
        # Bundling up the entire thing
        df = pd.read_excel('sentiments.xlsx')               # Reading the excel file
        df = self.createDf(df)                              # Creating the dataframe of emotion wala file
        self.df = pd.DataFrame()                            # Empty data Frame ---> for now USE-LESS
        self.findSentenceScore(df)                          # Finding score to each sentence with their emotions

        return df


# Handling the text file -> a.k.a. The trained data set
text_file = LoadText('ISEAR.txt')
text_of_file = text_file.getText()

# Handling the book file -> a.k.a. The untrained data set
# # book = LoadBook("Dracula.pdf")
# # text_of_book = book.createSentence()
text_of_book = ''

# Driver Code
excel_file = 'sentiments.xlsx'
clean = Analyzing(text_of_file, text_of_book)
df = clean.analyze()
# print(df)
    
 