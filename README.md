# Sentimental-Review-Analysis
Sentiment Analysis of a review/post through Named Entity Identification.

Input datasets consisting of product reviews and rating for a group of products given by customers on Amazon.
After initial data-trimming to filter actual review content, we use libraries like nltk and TextBlob to classify the reviews as positive and negative based on their on sentimental-analysis score.

Following this, we plot a graph of sentimental analysis scores of product reviews vs. product ratings.
In this graph, customer points at extreme locations in clusters are customer reviews and ratings that should be looked into detail because these customers reviews are relatively contradictory with respect to their ratings when compared with other "normal" customer reviews and ratings having customer reviews that are equatable to their respective ratings.
