from pre_processing import PreProcessing


class Quantifying(PreProcessing):
    tf = []

    def __init__(self, text):
        super(Quantifying, self).__init__(text)
        self.sentences = self.preProcess()  

    def calcFrequency(self):
        docFreq = []
        for sentence in self.sentences:
            words = {word : sentence.count(word) for word in list(sentence)} 
            docFreq.append(words)

        return(docFreq)

    def termFreq(self, len_of_sen):
        sentences = []
        for sentence in self.tf:
            tf = dict()
            for word in sentence:
                tf[word] = round(sentence[word] / len_of_sen, 3)
            sentences.append(sentence)
            print(sentence)
        return(sentences)

    # def createSentenceDict(self):
    #     for words in self.sentences:
    #         sentence = self.calcfrequency(words)
    #         self.sentence_dict.append(sentence)
    #         self.updateIn(sentence)

    #         self.termFreq(sentence, len(words))

        # self.docFreq()

        
    # def updateIn(self, sentence):
    #     for key in sentence:
    #         if key in self.corpus:
    #             self.corpus[key] = self.corpus[key] + sentence[key]
    #         else:
    #             self.corpus[key] = sentence[key]


    


    # def docFreq(self):
    #     df = dict()
    #     for word in self.corpus:
    #         for sentence in self.sentence_dict:
    #             if word in sentence:
    #                 df[word] = df[word] + 1
                
    #             else:
    #                 df[word] = sentence[word]

    #     self.df_dict = df

    def quantify(self):
        self.df = self.calcFrequency()
        for sentence in self.sentences:
            self.tf.append(self.termFreq(len(sentence)))


    def display(self):
        self.quantify()
        print(self.df)
    #     self.createSentenceDict()
    #     print("TERM", " FREQUENCY")
    #     for _ in self.tf_dict:
    #         print(_)

    #     # for _ in self.sentence_dict:
    #     #     print(_)  
    #     print("In CORPUS")        
    #     print(self.corpus)
    #     # print(self.df_dict)


text = "In late-2000, a young boy in called Ahmedabad called Govind dreamt of having a business. To accomodate his friends Ish and Omi’s passion, they open a cricket shop. Govind wants to make money and thinks big.  Ish is all about nurturing Ali, the batsman with a rare gift. their goals, they will have to face it all – religious politics, earthquakes, riots, unacceptable love  and above all, their own mistakes. Will they make it? Can an individual’s dreams overcome the nightmares offered by real life? Can we succeed despite a few mistakes? Based on real events, from the bestselling author of “Five Point Someone” and “One Night @ the call centre”, comes another dark, witty tale about modern India."

clean = Quantifying(text)
clean.display()
    