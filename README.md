# Tumblr Python Tag Topic Analysis
========================================

This is the topic analysis of Tumblr posts, that were posted with the Python tag. Some of the results were presented at the Ljubljana Python Meeetup in May 2019. 

The project has the following components:

    * Script to download the data
    * Analysis
    * Presentation
    * Topic Models Visualizations

The requirements for either project, sans standard Python libraries, are also in the requirments.txt file.

## Script to Download the Data
--------------------------------

This includes the files arguments.py and DownloadTumblrData.py. This one also requires the Tumblr keys and secrets in the file secrets.py. For the personal keys and secrets, the application needs to be registered. This can be done on Tumblr API page [https://www.tumblr.com/docs/en/api/v2](https://www.tumblr.com/docs/en/api/v2). 

The script uses the [pytumblr libary](https://github.com/tumblr/pytumblr). It is available on pip with:

    pip install pytumblr

The rest of the libraries are standard Python libraries.

The script can be started with:

    python DownloadTumblrData.py

If more than one run is requires, either do it manually, or have a cron job do it for you. 

When I downloaded the data (Finished on 12th of May 2019), there were between 40.000 and 41.000 posts with this tag. Because of the API call limit, it requires more than one run. But the scripts creates the file timestamp.txt, so it knows from which point to download when it restarts. 

Because I don't know, how to effectively anonymize the data, I have decided that I am not going to share the data I collected. 
 
## Analysis
------------------

The analysis part can be found in the file Tumblr-Python-Tag-Data-Analysis.ipynb. 

Beside the standard Python libraries, the following libraries are used:

* matplotlib ([pip](https://pypi.org/project/matplotlib/))
* beautifulsoup4 ([pip](https://pypi.org/project/beautifulsoup4/))
* pyLDAvis ([pip](https://pypi.org/project/pyLDAvis/))
* networkx ([pip](https://pypi.org/project/networkx/))
* gensim ([pip](https://pypi.org/project/gensim/))
* pandas ([pip](https://pypi.org/project/pandas/))
* nltk ([pip](https://pypi.org/project/nltk/))

These libraries are needed to replicate the analysis. To just look at the analysis, it should be possible to do it without (considering it is in Jupyter notebook). 

## Presentation
------------------------

The presentation can be found in the folder Presentation. It was created with [reveal.js](https://github.com/hakimel/reveal.js) framework. It can be started by opening the index.html file in the browser. 

The presentation can also be found on [https://sarajaksa.eu/content/presentations/2019/ljubljana-python-meetup-may-2019/index.html](https://sarajaksa.eu/content/presentations/2019/ljubljana-python-meetup-may-2019/index.html)

## Topic Models Visualization
-----------------------------------

Unlike the data, where I think the privacy could be problematic, I see nothing wrong with sharing the visualization of the topic models. The topic models are in the three folders, that start with TopicModels.

In the TopicModels-All, there are the results of topic analysis of all of the posts. In the TopicModels-Python, there are the topic analysis of all the posts, sans nature ones. In the TopicModels-PythonCoding, both the nature posts and startup posts were removed. 

The names are always the same: LDA\_X\_Y.html. The X was a help to me, to help me remember, which posts were included (1=all, 2=python, 3=coding only). The Y indicates, how many topics were in that solution. 

The files are html+javascript files and can be opened in browser.

