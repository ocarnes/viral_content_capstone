# README #
This repository contains work completed for the [Galvanize Data Science Immersive](https://www.galvanize.com/data-science)
Capstone Project for the October 2017 Denver Cohort.

## Background ##

In the world of online publishing, understanding what makes content popular can be hugely beneficial for both consumers and content creators alike. When a publisher knows what’s being shared and talked about, a more personalized experience can be tailored to the user based on current trends and user demographics.

From a publishing perspective, increased page views directly link an article’s popularity with the ad revenue generated from a user clicking on that page. Publishing buzzworthy content is therefore acutely relevant to a publisher’s bottom line.

## Objectives ##

The objective of this project are as follows:
1. Explore connections between popular articles published on a news and lifestyle site over the course of a few months during the summer of 2017
2. Predict content popularity using page views as a target value and attributes such as article topic, sentiment analysis, imagery, and interactivity as features
3. Compare article performance over time to trending topics on the same subject
4. Create easily adapted prediction models for partner company Surge for use in online publishing analytics

## Methods ##

1. Scrape relevant content from all articles published within a certain timeframe on a news and lifestyle website.
2. Clean text by removing uninformative words and stemming the remaining words to create a vocabulary list
3. Rate importance of each word in vocab list to a given document based on term frequency and inverse-document frequency
4. Determine latent topics and topic similarities using term frequency and Latent Dirichlet Allocation
5. Add sentiment analysis to determine whether articles have an overall negative or positive sentiment, in addition to comparing whether an article employs extreme vs. neutral language, and subjective vs. objective language
6. Evaluate importance of latent topics and sentiment to page views

### Web Scraping ###

The [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) python package was used to parse text scrapped
from the client's website. Features taken from the soup included article content, date published, hyperlink counts,
social media link counts, keyword tags, titles, urls, and thumbnail images.

### Topic Modeling ###

Topic modeling was performed using sklearn's [TfidfVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
and [Latent Dirichlet Allocation](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html). The below image is notable because of the uniqueness of each topic. Typically a corpus of articles will have overlapping topic clusters but here we can see that each cluster is very distinct. This creates an opportunity to build a very specialized recommendation system for readers wanting content similar to what they've already consumed.

![Clusters](/img/LDA.png)

### Sentiment Analysis ###

[Sentiment analysis](https://www.clips.uantwerpen.be/pages/pattern-en#sentiment)
from the [pattern](https://www.clips.uantwerpen.be/pages/pattern) python package was used to classify sentiment
on a scale from -1 to 1, where 0.1 is commonly used as the threshold between a positive or negative article. The below graph indicates that the majority of highly viewed articles are neither very polarizing nor very extreme in their use of either positive or negative language.

![Sentiment](/img/Polarity_x_subjectivity.png)

## Analysis ##

![Categories](/img/violin.png){:height="50%" width="50%"}

When analyzing the sentiments of highly viewed
![Under20](/img/violin5.png){:height="50%" width="50%"}![Over80](/img/violin8.png){:height="50%" width="50%"}
