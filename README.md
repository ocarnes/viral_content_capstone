# README #

This repository contains work completed for the [Galvanize Data Science Immersive](https://www.galvanize.com/data-science) 
Capstone Project for the October 2017 Denver Cohort. The objective of this project is to determine similarities
between popular online content from a news and lifestyle site. Natural language processing is used to determine 
latent topics within the group of articles, which is then compared to page views to assess what topics generate 
the most interest. 

Sentiment analysis is also included in this project because news and lifestyle articles frequently contain a 
majority of positive or negative language...
This README documents the steps needed to reproduce the following data and results.

## Web Scraping ##
The [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) python package was used to parse text scrapped
from the client's website. Features taken from the soup included article content, date published, hyperlink counts, 
social media link counts, keyword tags, titles, urls, and thumbnail images. 

## Topic Modeling ##

Topic modeling was performed using sklearn's [TfidfVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
and [K-means clustering](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html).

![Clusters](/src/visualization/article_20cluster_5k_feat.png)
![Legend](/src/visualization/legend_20cluster_5k_feat.png)

## Sentiment Analysis ##

Sentiment analysis is ... A previosly tagged movie review dataset provided by Rotten Tomatoes is often used to 
classify sentiment in a body of text. [Sentiment analysis](https://www.clips.uantwerpen.be/pages/pattern-en#sentiment)
from the [pattern](https://www.clips.uantwerpen.be/pages/pattern) python package was used to classify sentiment 
on a scale from -1 to 1, where 0.1 is commonly used as the threshold between a positive or negative article.
![Sentiment](/src/visualization/violin_40k_views.png)
![Categories](/src/visualization/cats_violin.png)
#### Topic 3: Babies ####
>   Views  | Sentiment | Title
>  --------|-----------|--------
> 1028834 | 'Negative'| 'Beyonce Reportedly Shuts Down Hospital Floor, Moves Patients Out As She Prepares To Give Birth'
>   138046 | 'Positive'| 'Jinger Duggar Shares Instagram Photo Of Risky Wardrobe Moment After Jeremy Vuolo Praises Her Modesty'
>   122462 | 'Positive'| "Jill Duggar Dillard Update: Baby Samuel Scott Dillard's First Photo Emerges, Sparks Fans' Worry"
>   121940 | 'Positive'| "Jinger Duggar 'Baby Bump' Is A Bust, Jeremy Vuolo Complains About 'Pagan Religion Of Catholicism'"
>   113102 | 'Positive'| "Jinger Duggar Photo Has Fans Debating Whether She's Pregnant Or Too Skinny"
>   106535 | 'Negative'| "Springdale Officials Move Motion Against Duggar Girls' Lawsuit"
>    99492 | 'Positive'| 'Duggar Family Mistreated Grandchildren? New Photo Sparks Trouble'
>    98595 | 'Positive'| 'Jinger Duggar Wears Shorts With Jeremy Vuolo After Fans Complain About Her Dark Pants'
>    85713 | 'Positive'| 'Joseph Duggar And Kendra Caldwell Change Wedding Date, Want Guests To Pay For Their Clothes'
>    76365 | 'Positive'| 'Jinger Duggar Makes Another Big Life Change Because Of Husband Jeremy Vuolo'

#### Topic 18: Games & Unhappy Fans ####
>  Views | Sentiment | Title
>  ------|-----------|--------
> 633002 | 'Negative'|'SEGA Forever: Every SEGA Game Ever Made Is Coming To iOS And Android For Free'
> 147386 | 'Negative'|"'Game Of Thrones Was My Sex Education' Says Sophie Turner As She Drops Hints About Sansa's Future On The Show"
>  70152 | 'Negative'|"The Real Reason Ed Sheeran Showed Up In The 'Game Of Thrones' Season 7 Premiere"
>  15959 | 'Positive'|"'Pokemon GO': Free Pokecoins Now Limited To 50 Per Day"
>  11595 | 'Negative'|"The 'Game Of Thrones' Cast Sing 'I Will Survive,' But Can Jon Snow Sing?"
>  10367 | 'Negative'| "'Pokemon GO': Is Gen 3 Coming July 22?"
>   9992 | 'Negative'|"'Game Of Thrones' S8 Feature-Length Shows Considered, S7 Finale Over 80 Minutes, 'Ghosts Of Westeros' Gather"
>   8312 | 'Positive'|"Pokemon Fans Furious About The 'Inexcusable' Reveal Made This Week"
>   7475 | 'Negative'|"'Pokemon GO' Gyms Are All Shutting Down Tomorrow - Here's What We Know About The Update"
>   7373 | 'Positive'|"'GTA Online' Gunrunning Update Live, Here's How Much Cash Is Required To Buy A Bunker, Mobile Ops Center"


## What is this repository for? ##

* Quick summary: The purpose of this project is to determine what features of an article contribute 
	to its popularity. Data
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

## How do I get set up? ##

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact