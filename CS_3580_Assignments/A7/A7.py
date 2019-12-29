#!/usr/bin/env python3

from __future__ import division
import numpy as np
import json
from sklearn.feature_extraction import text

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.datasets import fetch_20newsgroups
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
import sys
import fileinput
from sklearn.multiclass import OneVsRestClassifier

#from stop_words import get_stop_words
#stop_words = get_stop_words('en')
#stopWordSet = set(stop_words) | set(' ')
#print(len(stopWordSet))
#



def svm(bookInput):        


    with open('Mansfield_Park.txt',encoding='utf-8') as f:
        austen1 = ""
        lines = f.readlines()
        for line in lines:
            austen1 = austen1 + line.rstrip()
            f.close()
    
    
    with open('Northanger_Abbey.txt',encoding='utf-8') as f:
        austen2 = ""
        lines = f.readlines()
        for line in lines:
            austen2 = austen2 + line.rstrip()
            f.close()
        
    with open('Persuasion.txt',encoding='utf-8') as f:
        austen3 = ""
        lines = f.readlines()
        for line in lines:
            austen3 = austen3 + line.rstrip()
            f.close()
    
    with open('Pride_and_Prejudice.txt',encoding='utf-8') as f:
        austen4 = ""
        lines = f.readlines()
        for line in lines:
            austen4 = austen4 + line.rstrip()
            f.close()
    
    with open('Dorothy_and_the_Wizard_in_Oz.txt',encoding='utf-8') as f:
        baum1 = ""
        lines = f.readlines()
        for line in lines:
            baum1 = baum1 + line.rstrip()
            f.close()
            
    with open('Ozma_of_Oz.txt',encoding='utf-8') as f:
        baum2 = ""
        lines = f.readlines()
        for line in lines:
            baum2 = baum2 + line.rstrip()
            f.close()
            
    with open('The_Emerald_City_of_Oz.txt',encoding='utf-8') as f:
        baum3 = ""
        lines = f.readlines()
        for line in lines:
            baum3 = baum3 + line.rstrip()
            f.close()
            
    with open('The_Wonderful_Wizard_of_Oz.txt',encoding='utf-8') as f:
        baum4 = ""
        lines = f.readlines()
        for line in lines:
            baum4 = baum4 + line.rstrip()
            f.close()
            
    
    with open('All_Around_the_Moon.txt',encoding='utf-8') as f:
        verne1 = ""
        lines = f.readlines()
        for line in lines:
            verne1 = verne1 + line.rstrip()
            f.close()
            
    with open('Around_the_World.txt',encoding='utf-8') as f:
        verne2 = ""
        lines = f.readlines()
        for line in lines:
            verne2 = verne2 + line.rstrip()
            f.close()
            
    with open('From_the_Earth_to_the_Moon.txt',encoding='utf-8') as f:
        verne3 = ""
        lines = f.readlines()
        for line in lines:
            verne3 = verne3 + line.rstrip()
            f.close()
            
    with open('Journey_to_the_Centre_of_the_Earth.txt',encoding='utf-8') as f:
        verne4 = ""
        lines = f.readlines()
        for line in lines:
            verne4 = verne4 + line.rstrip()
            f.close()
            
    #getting rid of the parts in the beginning and end of the book that was added by the guttenburg project
    austen1 = austen1[584:868538]
    austen2 = austen2[560:426131]
    austen3 = austen3[553:459081]
    austen4 = austen4[1729:679160]
    
    baum1 = baum1[556:225719]
    baum2 = baum2[558:210758]
    baum3 = baum3[561:291847]
    baum4 = baum4[421:204146]
    
    verne1 = verne1[607:575240]
    verne2 = verne2[558:363427]
    verne3 = verne3[1390:537919]
    verne4 = verne4[559:476580]
    
    #creating a book that has key/value pairs
    #authors = {'Austen':str, 'Baum':str, 'Verne':str}
    authors = {1:str, 2:str, 3:str}
    
    #putting each authers books into one str in the value portion of key/value pair
    authors[1] = austen1+austen2+austen3+austen4
    authors[2] = baum1+baum2+baum3+baum4
    authors[3] = verne1+verne2+verne3+verne4
    
    authorsList = [1,2,3]
    
#    print(authors.values())
####################################################################################################################################################    
#                                       
####################################################################################################################################################

    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(authors.values())
    
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
#    print("The shape of 'X_train_tfidf':")
#    print(X_train_tfidf.shape)
    
    
    #Now that we have our features, we can train a classifier to try to predict the category of a post. Let’s start with a naïve Bayes classifier, which provides a nice baseline for this task. scikit-learn includes several variants of this classifier; the one most suitable for word counts is the multinomial variant:
    clf = OneVsRestClassifier(MultinomialNB()).fit(X_train_tfidf, authorsList)
    
    #Predicted section
    
    X_new_counts = count_vect.transform(test)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    
    predicted = clf.predict(X_new_tfidf)
    
    if (predicted == 1):
        authorName = "Austen"
    elif (predicted == 2):
        authorName = "Baum"
    elif (predicted == 3):
        authorName = "Verne"
        
        
    
    
    return(authorName)
####################################################################################################################################################    
#                           Command Line Interface
####################################################################################################################################################
    
print("\nDaniel Salmond")
wantAnotherBook = True
print("Your book will be compared against the authors Jane Austen, L. Frank Baum, and Jules Verne.")
while wantAnotherBook:	
	
    #user input book
    test = []
    text_book = input("Please input the text file name of book to compare (ex. test_book.txt): ")
    with open(text_book,encoding='utf-8') as f:
        readBook = ""
        lines = f.readlines()
        for line in lines:
            readBook = readBook + line.rstrip()
            f.close()
            
    test = np.array([readBook])
#    bookInput = {1:str}
#    bookInput[1] = readBook
    
    #Print the results
    results = svm(test)
    print("The predicted author of the book you inputed is: ", results)
    more = input("Would you like to input another book?  Y for Yes and N for No:  ")
    if (more == 'N') or (more == 'n'):
        wantAnotherBook = False
    elif (more == 'Y') or (more == 'y'):
        pass
    else:
        print("You didn't enter a Y or N. Try Another book!")		
		
print("Thanks you.")




