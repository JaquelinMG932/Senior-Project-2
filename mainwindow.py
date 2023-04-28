import numpy as np
from wordcloud import WordCloud
import re
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from nltk.tokenize import TweetTokenizer, RegexpTokenizer
from nltk.corpus import stopwords
from stop_words import get_stop_words
import nltk
from collections import Counter
from os import path
from fpdf import FPDF
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from twit import *
from interface_ui import Ui_MainWindow
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt, QSize, QPropertyAnimation, QIODevice, QUrl, QFile, QTextStream
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebEngineWidgets import QWebEngineView
import sys
import tweepy
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Qt5Agg')


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Initializes the user interface calling setupUi method from interface_ui.py
    """

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        """
        Connect the event methods to the buttons
        """
        self.homeBtn.clicked.connect(self.clickedHomeBtn)
        self.dataBtn.clicked.connect(self.clickedDataBtn)
        self.reportBtn.clicked.connect(self.clickedReportBtn)
        self.menuBtn.clicked.connect(self.menuClicked)
        self.infoBtn.clicked.connect(self.clickedInfoBtn)
        self.helpBtn.clicked.connect(self.clickedHelpBtn)
        self.minimizeWinBtn.clicked.connect(self.minimize)
        self.restoreWinBtn.clicked.connect(self.maximize)
        self.pushButton.clicked.connect(self.closeCenterMenu)
        self.closeWinBtn.clicked.connect(self.closeApp)
        self.searchBtn.clicked.connect(self.clickedSearchBtn)

        """
        Create Canvas for Graphs
        """
        self.canvas = FigureCanvas(Figure())
        self.ax = self.canvas.figure.add_subplot(111)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.container1 = QWidget()
        self.lay = QVBoxLayout(self.container1)
        self.lay.addWidget(self.canvas)
        self.lay.addWidget(self.toolbar)

        # Add widget to scroll layout
        self.scroll_layout.addWidget(self.container1)
        self.container1.setMinimumWidth(400)
        self.container1.setMinimumHeight(400)

        """
        self.canvas2 = FigureCanvas(Figure())
        self.ax2 = self.canvas2.figure.add_subplot(111)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
         """

        self.container2 = QWidget()
        self.lay = QVBoxLayout(self.container2)
        self.l1 = QLabel(self.container2)
        self.l1.setMinimumWidth(1000)
        self.l1.setMinimumHeight(800)

        # Add second widget to scroll layout
        self.scroll_layout.addWidget(self.container2)
        self.container2.setMinimumWidth(1000)
        self.container2.setMinimumHeight(800)

        """
        self.lay.addWidget(self.canvas2)
        self.lay.addWidget(self.toolbar2)
        """
        self.container3 = QWidget()
        self.lay = QVBoxLayout(self.container3)
        self.label = QLabel(self.container3)
        self.label.setMinimumWidth(800)
        self.label.setMinimumHeight(400)

        # Add third widget to scroll layout
        self.scroll_layout.addWidget(self.container3)
        self.container3.setMinimumWidth(800)
        self.container3.setMinimumHeight(400)

        self.container4 = QWidget()
        self.lay = QVBoxLayout(self.container4)
        self.l2 = QLabel(self.container4)
        self.l2.setMinimumWidth(1000)
        self.l2.setMinimumHeight(800)

        self.scroll_layout.addWidget(self.container4)
        self.container4.setMinimumWidth(1000)
        self.container4.setMinimumHeight(800)

        self.container5 = QWidget()
        self.lay = QVBoxLayout(self.container5)
        self.l3 = QLabel(self.container5)
        self.l3.setMinimumWidth(1000)
        self.l3.setMinimumHeight(600)

        # Add widget to scroll layout
        self.scroll_layout.addWidget(self.container5)
        self.container5.setMinimumWidth(1000)
        self.container5.setMinimumHeight(800)

        """
        self.canvas3 = FigureCanvas(Figure())
        self.ax3 = self.canvas3.figure.add_subplot(111)
        self.toolbar3 = NavigationToolbar(self.canvas3, self)
        self.container4 = QWidget()
        self.lay4 = QVBoxLayout(self.container4)
        self.lay4.addWidget(self.canvas3)
        self.lay4.addWidget(self.toolbar3)
         """
        """
        self.scroll_layout.addWidget(self.container4)
        self.container4.setMinimumWidth(400)
        self.container4.setMinimumHeight(400)
        """
        """ self.container.setMinimumWidth(800)
        self.container3.setMinimumHeight(400) """

        """
        Creates WebView for PDF
        """
        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(
            QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(
            QWebEngineSettings.WebAttribute.PdfViewerEnabled, True)
        self.verticalLayout_13.addWidget(self.webView)
        self.webView.setMinimumHeight(600)

    # Button action logic

    # Changes the StackWidget to page 4 for home page

    def clickedHomeBtn(self):
        self.stackedWidget_2.setCurrentWidget(self.page_4)
        self.leftMenuContainer.setMaximumWidth(50)

    # Changes Stacked Widget to page 3 where user can enter search topic

    def clickedDataBtn(self):
        self.stackedWidget_2.setCurrentWidget(self.page_3)
        self.leftMenuContainer.setMaximumWidth(50)

    # Changes Stacked Widget to page  5 which is where WebView is already there for pdf view
    def clickedReportBtn(self):
        self.stackedWidget_2.setCurrentWidget(self.page_5)
        self.leftMenuContainer.setMaximumWidth(50)
        topic = self.lineEdit.text()

        # --------------------- Creates pdf file ---------------------------
        file = open("text.txt", "r")
        text = file.read()
        file.close()

        pdf = FPDF('P', 'mm', 'Letter')

        # Add a page
        pdf.add_page()

        pdf.set_margins(10, 10, 10)

        # specify font
        # fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
        # 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))

        pdf.set_font('helvetica', 'BU', size=16)

        pdf.cell(w=0, h=0, txt='Sentimental Anaylsis Report', align='C')

        pdf.ln(h=10)
        # Line Breaks are required inbetween new cells, multicells and images!

        pdf.set_font('helvetica', size=12)

        pdf.multi_cell(0, 10, text, align='J')

        # Add an new page
        pdf.add_page()

        pdf.set_font('helvetica', 'B', size=10)

        pdf.cell(w=0, h=0, txt='Figure 1:', align='L')

        # Add an image to the PDF
        # pdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
        # For standard 8.5 x 11 paper 10x10 x/y will center it on page
        # w=195, h=149

        pdf.image('first.png', x=20, y=25, w=175, h=129)

        pdf.ln(h=160)

        pdf.set_font('helvetica', 'I', size=10)

        pdf.multi_cell(0, 10, 'Description: Figure 1 represents a bar graph containing the overall score for ' + str(topic) +
                       '. The red bar is the total score weighted while the blue and orange represent the polarity and subjectivity score. The higher the total score is the more positive the sentiment for the selected topic', align='J')
        # Add an new page
        pdf.add_page()

        pdf.set_font('helvetica', 'B', size=10)

        pdf.cell(w=0, h=0, txt='Figure 2:', align='L')

        # Add an image to the PDF
        # pdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
        # For standard 8.5 x 11 paper 10x10 x/y will center it on page
        # w=195, h=149

        pdf.image('bar.png', x=20, y=25, w=175, h=129)

        pdf.ln(h=160)

        pdf.set_font('helvetica', 'I', size=10)

        pdf.multi_cell(0, 10, 'Description: This is a graph that shows the top 10 most frequently reoccuring words found in the tweets.'
                       + "Tokenization was used to count the number of times each word appeared and the result for the top 10 were aggregated into this chart.", align='J')
        # Add an new page
        pdf.add_page()

        pdf.set_font('helvetica', 'B', size=10)

        pdf.cell(w=0, h=0, txt='Figure 3:', align='L')

        # Add an image to the PDF
        # pdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
        # For standard 8.5 x 11 paper 10x10 x/y will center it on page
        # w=195, h=149

        pdf.image('scatter.png', x=20, y=25, w=175, h=129)

        pdf.ln(h=160)

        pdf.set_font('helvetica', 'I', size=10)

        pdf.multi_cell(0, 10, 'Description: This graph is a scatter plot of all the tweets obtained via the Twitter API for a given topic. This graph you can see the relationship between polarity and subjectivity. If the point is darker that mean there are more than one tweet that generated the same score. .', align='J')

        # Add an new page
        pdf.add_page()

        pdf.set_font('helvetica', 'B', size=10)

        pdf.cell(w=0, h=0, txt='Figure 4:', align='L')

        # Add an image to the PDF
        # pdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
        # For standard 8.5 x 11 paper 10x10 x/y will center it on page
        # w=195, h=149

        pdf.image('wordcloud.png', x=20, y=25, w=175, h=129)

        pdf.ln(h=160)

        pdf.set_font('helvetica', 'I', size=10)

        pdf.multi_cell(0, 10, 'Description: This graph shows wordcloud for the selected topic. The more a specific word appear in the data, the bigger and bolder it will appear in the word cloud and the more important it is. This word cloud was generated using a maximum of 5000 words. ', align='J')
        # Add an new page
        pdf.add_page()

        pdf.set_font('helvetica', 'B', size=10)

        pdf.cell(w=0, h=0, txt='Figure 5:', align='L')

        # Add an image to the PDF
        # pdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
        # For standard 8.5 x 11 paper 10x10 x/y will center it on page
        # w=195, h=149

        pdf.image('adjectives.png', x=20, y=25, w=175, h=129)

        pdf.ln(h=160)

        pdf.set_font('helvetica', 'I', size=10)

        pdf.multi_cell(0, 10, 'Description: This graph shows the most frequent adjectives used in the tweets. Since these are descriptive words, they can really affect the overall score of the topic. Having more positive adjectives can really change the overall test results produced in the graphs.  ', align='J')

        pdf.output("pdftest.pdf")

        # Sets webview to url leading to desktop directory where pdf was saved
        if len(sys.argv) > 1:
            self.webView.setUrl(QUrl(f"{sys.argv[1]}"))
        else:
            wd = wd = path.dirname(path.abspath(sys.argv[0]))
            test_pdf = "pdftest.pdf"
            self.webView.setUrl(QUrl(f"file://{wd}/{test_pdf}"))

    # Displays Menu
    def menuClicked(self):
        w = self.leftMenuContainer.width()
        maxExtend = 16777215
        standard = 50
        if w == 50:
            self.leftMenuContainer.setMaximumWidth(maxExtend)
        else:
            self.leftMenuContainer.setMaximumWidth(standard)

    # Displayes Info Tab
    def clickedInfoBtn(self):
        self.stackedWidget.setCurrentWidget(self.page)
        self.centerMenuSubContainer.setMinimumWidth(200)
        self.centerMenuContainer.setMinimumWidth(0)
        self.centerMenuContainer.setMaximumWidth(200)
        self.leftMenuContainer.setMaximumWidth(50)
        self.label_2.setText("To begin:\nEnter a topic you would like\nto explore in the search\nbar. After clicking the \nbutton the program will \nget tweets from Twitter\nThat contains the\nSubject you have entered\nBased on those results\nThe program will generate\nThe graphs that will tell\nYou the sentiment of the\nTopic you have entered. \nThe higher the total score the\nMore positive the tweets are\nThe graphs will also present\nFrequently used words that\nGive users more information \nAbout the topic.")

    # Displayes Help Tab

    def clickedHelpBtn(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.centerMenuSubContainer.setMinimumWidth(200)
        self.centerMenuContainer.setMinimumWidth(0)
        self.centerMenuContainer.setMaximumWidth(200)
        self.leftMenuContainer.setMaximumWidth(50)
        self.label_3.setText("For more help:\nFAQ:\nWhere can I find documentation?\nVisit QT Documentation\nHow does the app work?\nSee Information\n\n What is Polarity?\nPolarity ranges from -1 to 1.\nIt refers to negative and\nPositive sentiment\n\nWhat is Subjectivity?\nSubjectivity ranges from 0 to 1.\nIt refers to personal opinions\nand judgments.\n")

    def minimize(self):
        self.showMinimized()

    def maximize(self):
        self.showMaximized()

    def closeApp(self):
        sys.exit()

    def closeCenterMenu(self):
        self.centerMenuSubContainer.setMinimumWidth(0)
        self.centerMenuContainer.setMinimumWidth(0)
        self.centerMenuContainer.setMaximumWidth(0)

    # Logic to run API call to Twitter and get Tweet scores
    def clickedSearchBtn(self):
        tweets = self.getTweets()
        t = []
        tweetObj = []
        for tweet in tweets:
            t.append([tweet.full_text])

        for text in t:
            tweetObj.append(TweetObject(str(text)))

        topic = TopicObject(tweetObj)
        polarity = topic.getPolarity(tweetObj)
        subjectivity = topic.getSubjectivity(tweetObj)
        total = topic.getScore(polarity, subjectivity)
        self.label_9.setText("The Polarity score is: " + str(polarity))
        self.label_10.setText(
            "The Subjectivity score is: " + str(subjectivity))

        data = {
            "total": total,
            "polarity": polarity,
            "subjectivity": subjectivity
        }

        self.getFirstGraph(data)

        tokenizer = TweetTokenizer()
        tweet_tokens = [tokenizer.tokenize(str(tweet)) for tweet in t]

        stop_words = ['RT', 'contact', '\"\"', 've',
                      's', 't', '*', '\'', '...', '\"', ' ']
        # extract the adjectives
        adjectives = []
        adjectives.clear()
        for tokens in tweet_tokens:
            pos_tags = nltk.pos_tag(tokens)
            for word, pos in pos_tags:
                if pos == 'JJ' and word not in stop_words:
                    adjectives.append(word)
        # print(adjectives)

        # create a list of unique adjectives and their frequency
        unique_adj = list(set(adjectives))
        adj_count = [adjectives.count(adj) for adj in unique_adj]

        current = []
        # sort the adjectives by frequency in descending order and select the top 10
        sorted_adj = [adj for adj, count in Counter(
            adjectives).most_common(15)]
        sorted_count = [count for adj, count in Counter(
            adjectives).most_common(15)]

        result = self.filter(t)
        self.wc(result, 'black', 'Frequent Words')

        self.getThirdGraph(result)

        x = topic.listPolarity(tweetObj)
        y = topic.listSubjectivity(tweetObj)
        self.getFourthGraph(x, y)
        self.getSecondGraph(sorted_adj, sorted_count)

    # Calls the Twitter API

    def getTweets(self):
        searchQuery = self.lineEdit.text()
        api = tweepy.API(auth)
        tweets = api.search_tweets(
            q=searchQuery, lang='en', result_type='recent', count=100, tweet_mode='extended')
        return (tweets)

    # Generates bar graph of total, subjectivity, and polarity
    # You pass in data dictionary as scores
    def getFirstGraph(self, scores):
        titles = list(scores.keys())
        values = list(scores.values())

        bar_labels = ['red', 'blue', 'orange']
        bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

        self.ax.bar(titles, values, width=0.4,
                    label=bar_labels, color=bar_colors)
        self.ax.set_ylabel("Scoress")
        self.canvas.draw()
        self.canvas.print_figure("first.png")

    # Generates word frequency graph

    def getSecondGraph(self, adj, count):
        fig, ax = plt.subplots(figsize=(7, 5.5))
        fig.set_size_inches(10, 5)
        plt.bar(adj, count, width=0.7, align='edge')
        plt.xlabel('Adjectives')
        plt.ylabel('Frequency')
        plt.title('Frequency of Adjectives in Tweets')
        plt.xticks(rotation=20)
        plt.savefig("adjectives.png")
        self.l3.setPixmap(QPixmap(QImage("adjectives.png")))
        self.l3.setScaledContents(True)

    # Generates the wordcloud

    def wc(self, data, bgcolor, title):
        wc = WordCloud(background_color=bgcolor,
                       max_words=5000,  max_font_size=50)
        gwc = wc.generate(' '.join(data))
        image = gwc.to_image()
        image.save("wordcloud.png")
        self.label.setPixmap(QPixmap(QImage("wordcloud.png")))
        self.label.setScaledContents(True)

    # Filters and cleans text

    def filter(self, t):
        # convert list into text
        list_to_text = ''.join(str(t))

        # removes punctuation,numbers and returns list of words
        desc_remove_pun = re.sub('[^A-Za-z]+', ' ', list_to_text)

        # remove all the stopwords from the text
        stop_words = list(get_stop_words('en'))
        nltk_words = list(stopwords.words('english'))
        stop_words.extend(nltk_words)

        word_tokens = nltk.tokenize.word_tokenize(desc_remove_pun)
        filtered_sentence_desc = [
            w_desc for w_desc in word_tokens if not w_desc in stop_words]
        filtered_sentence_desc = []
        for w_desc in word_tokens:
            if w_desc not in stop_words:
                filtered_sentence_desc.append(w_desc)

        # Remove characters which have length less than 2
        without_single_chr_desc = [
            word_desc for word_desc in filtered_sentence_desc if len(word_desc) > 2]

        # Remove numbers
        cleaned_data_desc = [
            word_desc for word_desc in without_single_chr_desc if not word_desc.isnumeric()]
        return (cleaned_data_desc)

    def getThirdGraph(self, data):
        top_N = 100
        word_dist_desc = nltk.FreqDist(data)
        rslt_desc = pd.DataFrame(word_dist_desc.most_common(top_N),
                                 columns=['Word', 'Frequency'])

        fig, ax = plt.subplots(figsize=(7, 5.5))
        fig.set_size_inches(10, 5)
        plt.figure(figsize=(10, 10))
        sns.set_style("whitegrid")
        ax = sns.barplot(x="Word", y="Frequency", data=rslt_desc.head(10))
        plt.savefig("bar.png")
        self.l1.setPixmap(QPixmap(QImage("bar.png")))
        self.l1.setScaledContents(True)

    def getFourthGraph(self, list1, list2):
        N = len(list1)
        colors = np.random.rand(N)
        plt.figure(figsize=(10, 10))
        plt.scatter(list1, list2, c=colors, alpha=.2)
        plt.xlabel("Polarity")
        plt.ylabel("Subjectivity")
        plt.title("Polarity vs Subjectivity For Each Tweet")
        plt.savefig("scatter.png")
        self.l2.setPixmap(QPixmap(QImage("scatter.png")))
        self.l2.setScaledContents(True)
