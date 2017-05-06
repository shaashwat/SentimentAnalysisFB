from textblob import TextBlob
import Analyzer

account = input("Enter page name to analyze here: ")
question = input("Would you like to adjust comment and page number settings? (y/n): ")
if question == "y":
    pagenum = input("How many posts would you like to look at (default is 50): ")
    commentnum = input("How many comments would you like to look at per page? (default is 50): ")
    print("Analyzing Tweets...")
    print(Analyzer.getSentimentAnalysisScore(account, number_of_posts_limit=pagenum, number_of_comments_limit=commentnum))
else:
    print("Analyzing Tweets...")
    print(Analyzer.getSentimentAnalysisScore(account))
