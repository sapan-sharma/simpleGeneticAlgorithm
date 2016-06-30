import nltk
import random
import pickle
from nltk.corpus import movie_reviews


def movie_classifier():
    
    featureSets=createFeatureSet(3000)

##    # set that we'll train our classifier with
    training_set = featureSets[:2500]
##
##    # set that we'll test against.
    testing_set = featureSets[2500:]
##
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

   


def find_features(document, word_features):
    words = set(document)    
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features






def createFeatureSet(numOfExamples):    
    
    documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)[:numOfExamples]]
    with open('documents.txt', 'wb') as f:        
        pickle.dump(documents, f)

##    #read from file
##    with open('documents.txt', 'rb') as f:
##        documents = pickle.load(f)

    random.shuffle(documents)
    
    all_words = []
##    for w in movie_reviews.words():
##        all_words.append(w.lower())
    #write to file
##    with open('allwords.txt', 'wb') as f:
##        pickle.dump(all_words, f)

    #read from file
    with open('allwords.txt', 'rb') as f:
        all_words = pickle.load(f)

    freqDist = nltk.FreqDist(all_words)
    #print('freq dist')
    #print(freqDist.most_common(50))

    word_features = freqDist.most_common(3000)

    featuresets = [(find_features(rev, word_features), category) for (rev, category) in documents]
    return featuresets



movie_classifier()

