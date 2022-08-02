# this file will convert data to a plot
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


class data_visualisation():

    def __init__(self, file = 'Tweets.txt', height = [], emotions = []):
        #init function
        self.emotions = emotions
        self.file = file
        self.height = height

    
    def import_data_file(self, file):
        #import data from file and put it in list
        data_file = open(file, 'r', encoding="utf8")
        data_list = []
        for line in data_file:
            data_list.append(line)
        return data_list
    
    def add_emotions(self, emotion_to_add):
        #add emotions you want to analyze
        self.emotions.append(emotion_to_add)
        self.height.append(0)

    def data_processing(self, file):
        # in this function the data is processed and put into a list of heights which can be plotted
        for emotion in self.emotions:
            for item in self.import_data_file(file):
                if emotion in item:
                    self.height[self.emotions.index(emotion)] += 1
                #else:
                    #self.height[0] += 1
        
    """    
    def process_dict(self):
        
        dict_ = {'happy': 32, 'sad': 15, 'stressed': 0, 'angry': 19}
        for key in dict_:
            self.emotions.append(key)
            self.height.append(dict_[key])
    """

    def plot_data_bar(self):
        # This functions plots the graph
        
        y_pos = np.arange(len(self.emotions))
        # Create bars
        plt.bar(y_pos, self.height)
 
        # Create names on the x-axis
        plt.xticks(y_pos, self.emotions)
        plt.ylabel("amount of mentions")
 
        # Show graphic
        return plt.show()

    def word_cloud(self, file):
    # Create a list of word
        #text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")
        
        
            
        
        
        with open(str(file), 'r', encoding = 'utf-8') as myfile:
            text = myfile.read()
            text.replace('twitter', '')
            text.replace('https', '')
            text.replace('Twitter', '')
            
        stopwords = set(STOPWORDS)
        stopwords.update(['twitter', 'https', 'RT', 'pic'])
            
    #Create the wordcloud object
        wordcloud = WordCloud(stopwords = stopwords, background_color = 'grey', width=800, height=800, margin=0).generate(text)
 
    # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.margins(x=0, y=0)
        plt.show()
        #wordcloud could show that not that many people tweet about emotions etc
        



def run_data_visualization():
    #testing the visualisation
    #TODO: fix capitalization problems
    
    test_vis = data_visualisation()
    
    test_vis.import_data_file('Tweets.txt')
    test_vis.add_emotions('car')
    test_vis.add_emotions('tired')
    test_vis.add_emotions('angry')
    test_vis.add_emotions('stressed')
    test_vis.add_emotions('scared')
    test_vis.add_emotions('sad')
    test_vis.add_emotions(":(")
    test_vis.add_emotions(":)")
    print(test_vis.emotions)
    test_vis.data_processing('Tweets.txt')
    test_vis.plot_data_bar()

    
    
    print('word cloud of the 10 past tweets of someone who tweeted about a car accident')
    test_vis.word_cloud('Tweets.txt')
    print('word cloud of the tweets about a car accident')
    test_vis.word_cloud('output.csv')
    
    #test_vis.network_vis('Tweets.txt')
    

run_data_visualization()

