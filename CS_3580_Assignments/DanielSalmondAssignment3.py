#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns; sns.set(color_codes=True)



file = "flavors_of_cacao.csv"


# Creates a DataFrame from the csv file
all_data = pd.read_csv(file)


####################################################################################
#                                Basic Information
#####################################################################################


print("Number of Chocolates for each rating:")
rating  = all_data['Rating']        # Taking Ratings column and return a Series
ratings = rating.value_counts()     # Counts the number of series
ratings = ratings.sort_index()      # Sorts the "index" which is the rating values

print(ratings)                      # Print out the counts.
print()

country_means = all_data[['Company\nLocation', 'Rating']]                    # Reads two columns and returns a datafram
country_means.columns = ['Country', 'Mean Rating']                           # Rename from Company Location to Country, Rating -> Mean Rating
country_means = country_means.groupby('Country')                             # Group by Country
country_means = country_means.mean()                                         # Get the mean
country_means = country_means.sort_values(by="Mean Rating", ascending=False) # Sort descending by Mean Rating

print(country_means.head(5))                                                 # Print top 5

ratings.plot.bar()                                                           # Bar Graph of the ratings:

plot.ylabel("Count of Ratings")
plot.show()



print("Find the mea for the company location: ", all_data['Company\nLocation'].mode()[0])
print("Find the mode for the origin of the broad bean: ", all_data['Broad Bean\nOrigin'].mode()[0])
print("Find the mode for the percent of Bean Origin: ", all_data['Cocoa\nPercent'].mode()[0])
print("Find the country for mode of specific bean origin: ", all_data['Specific Bean Origin\nor Bar Name'].mode()[0])
print("Find the median for the Review Date: ", all_data['Review\nDate'].median())
print()


####################################################################################
#                               First Correlation
#####################################################################################


#    Print out the correlation,
cocoaPercent = all_data['Cocoa\nPercent']
cocoaPercent = all_data['Cocoa\nPercent'].str.rstrip('%').astype('float') / 100.0
correlation1 = cocoaPercent.corr(rating)
print("Correlation between cocoa and rating:", correlation1)

#    show the scatterplot and linear regression line in a graph,
fit = np.polyfit(cocoaPercent,rating,1)
fit_fn = np.poly1d(fit)
plot.plot(cocoaPercent,rating, 'yo', cocoaPercent, fit_fn(cocoaPercent), '--k')
plot.show()

#    What is the correlation between percent of cocoa and rating? (write in text to print to console)
print('\nFrom the correlation number we calculated, and the graph, we see that there is little correlation between the amount of Cocoa and Rating.\n')


####################################################################################
#                               Second Correlation
#####################################################################################

other_data = pd.read_csv(file, header=0, names=['Company', 'Specific Bean Origin', 'REF', 'Review Date', 'Cocoa Percent', 'Company Location', 'Rating', 'Bean Type', 'Broad Bean Origin'],
            converters={'Cocoa':lambda c: float(c.strip("%"))/100})

companyRating = other_data[['Company', 'Rating']]
companyRating.columns = ['Company', 'Rating']
companyRating = companyRating.loc[companyRating['Company'].isin(('Soma', 'Domori', 'Caribeans', 'Pralus', 'A. Morin'))]
dummies = pd.get_dummies(companyRating['Company'])
companyRating = pd.concat([companyRating, dummies], axis=1)
companyRating = companyRating.drop(['Company'], axis=1)
print(companyRating.corr())


x = np.array(companyRating['Soma'])
y = np.array(companyRating['Rating'])
fitme = np.polyfit(x,y,1)
fitme_fn = np.poly1d(fitme)
# fit_fn is now a function which takes in x and returns an estimate for y

plot.plot(x,y, 'yo', x, fitme_fn(x), '--k')
plot.title("Correlation between the company Soma and Rating")
plot.xlabel("Soma")
plot.ylabel("Rating")
print("")
plot.show()



print("What are the correlations between company (Soma) and rating? The correlation matrix shows that soma's ratings is correlated to the other companies ratings. In the table, the 1's that go diagnol are those that are compared to itself which would always be 1. Soma's correlation with rating is" +
      " at 0.232726. When we compare Soma against A. Morin, we see that it has a correlation of -0.381562, which doesn't correlate that well compared to some of the others"+
      " When we compare the correlations data of Soma against the Caribeans, we see that it correlates the best out of the other companies with a -0.163648. Domori correlates to Soma with -0.401886. Soma correlates with Pralus at -0.401886.\n")


####################################################################################
#                               Independent Thought
#####################################################################################

print("\nWhat is the correlation between Specific Bean Origin and Rating for 5 bean origins?")
bean = other_data[['Specific Bean Origin', 'Rating']]
bean = bean.loc[bean['Specific Bean Origin'].isin(('Vanua Levu', 'Chuao', 'Ecuador', 'San Juan', 'Madagascar'))]
dummies = pd.get_dummies(bean['Specific Bean Origin'])
bean = pd.concat([bean, dummies], axis=1)
bean = bean.drop(['Specific Bean Origin'], axis=1)
print(bean.corr())


x = np.array(bean['San Juan'])
y = np.array(bean['Rating'])
fitme = np.polyfit(x,y,1)
fitme_fn = np.poly1d(fitme)

plot.plot(x,y, 'yo', x, fitme_fn(x), '--k')
plot.title("Correlation between the San Juan and Rating")
plot.xlabel("San Juan")
plot.ylabel("Rating")
print("")
plot.show()

print("\nI chose my question based off of what I thought was interesting. I analysed the question on how I would approach it, what made sense but also what would be applicable. I answered it by finding the correlation and then graphing it which doesn't really correlate very well.")










