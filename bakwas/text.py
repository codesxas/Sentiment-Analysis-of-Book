import pandas as pd, numpy as np, matplotlib.pyplot as plt

df = pd.read_excel('C:\\Users\\shrey\\Desktop\\tabs\\Syllabus\\IR\\Project\\sentiments.xlsx')
print(df)
    
from pre_processing import LoadBook, PreProcessing
# from quantifying import Quantifying

import pandas as pd, numpy as np, matplotlib.pyplot as plt
 
 
class Analyzing(PreProcessing):
    
    def __init__(self, text):
        super(Analyzing, self).__init__(text)
        self.sentences = self.preProcess()

    def emotionClassifiers(self, emotion):
        var = self.df.loc[df[emotion] == 1, 'Words'].copy().reset_index(drop = True)
        var = pd.concat([pd.DataFrame(var)], 1)
        return var

    def createDF(self, df):
        print(self.sentences)
        for word in self.sentences:
            df1 = df.loc[df['Words'].isin(word)]
            self.df = self.df.append(df1, ignore_index = True)
        print(self.df)
        # print(len(self.df))

    def analyze(self):
        df = pd.read_excel('sentiments.xlsx')
        self.df = pd.DataFrame()
        self.createDF(df)

        






# book = LoadBook('dracula.pdf')
# text = book.getText()
# print(text)
# text = """Jonathan Harker’s Journal 3 May. Bistritz.—Left Munich at 8:35 P.M., on 1st May, arriving at Vienna early next morning; should have arrived at 6:46, but train was an hour late. Buda-Pesth seems a wonderful place, from the glimpse which I got of it from the train and the little I could walk through the streets. I feared to go very far from the station, as we had arrived late and would start as near the correct time as possible. The impression I had was that we were leaving the West and entering the East; the most western of splendid bridges over the Danube, which is here of noble width and depth, took us among the traditions of Turkish rule. We left in pretty good time, and came after nightfall to Klausenburgh. Here I stopped for the night at the Hotel Royale. I had for dinner, or rather supper, a chicken done up some way with red pepper, which was very good but thirsty. (Mem. get recipe for Mina.) I asked the waiter, and he said it was called ‘paprika hendl,’ and that, as it was a national dish, I should be able to get it anywhere along the Carpathians. I found my smattering of German very useful here, indeed, I don’t know how I should be able to get on without it. Having had some time at my disposal when in London, I had visited the British Museum, and made search among 
# Free eBooks at Planet eBook.com
# the books and maps in the library regarding Transylvania; it had struck me that some foreknowledge of the country could hardly fail to have some importance in dealing with a nobleman of that country."""
# clean = PreProcessing(text)
# clean.display()

# clean = Analyzing(text)
# clean.analyze()
# clean.display()

df = pd.read_excel('sentiments.xlsx')
print(df)
    
