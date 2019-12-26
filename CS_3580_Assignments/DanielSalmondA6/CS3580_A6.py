#!/usr/bin/env python3
import pandas

allMovies = pandas.read_csv("movies.with.ratings.csv.gz", compression="gzip", index_col=0)

userSelections = set() # set of movieId index values from allMovies or any other dataframe
initialRecommendations = [] # initial random recommendations

def makeGenreDictionary(nestedListOfGenres):
	c = {'_total': 0}
	for movie in nestedListOfGenres:
		for genre in movie:
			if genre in c: c[genre] += 1
			else: c[genre] = 1
			c['_total'] += 1
	return c

def weightedSimilarity(singleMovie, genreDictionary):
	numerator = 0
	for genre in singleMovie:
		if genre in genreDictionary:
			numerator += genreDictionary[genre]
	return numerator / genreDictionary['_total']


def search(searchString):
	searchResults = allMovies.loc[allMovies['title'].str.contains(searchString, case=False, regex=False)]
	return searchResults

def displayMovies(moviesDF):
	moviesDF = moviesDF.sort_values(by="title")
	for index, row in moviesDF.iterrows():
		print("MovieID: ", index, ", Title: ", row['title'], ", Rating: ", row['rating'], sep="")

def getRecommendations():
	"""Returns a dataframe with the movie recommendations based on userSelections.  If userSelections is empty, 10 random movies"""
	global userSelections, allMovies
	if len(userSelections) == 0:
		recommendations = allMovies.sample(10)
	else:    
		selectedMovies = allMovies.loc[allMovies.index.isin(userSelections)]
		genresFromSelected = selectedMovies['genres']
		genreList = [ g.split("|") for g in genresFromSelected.tolist()]
		
		genreDictionary = makeGenreDictionary(genreList)
		allMovies['distance'] = allMovies['genres'].map(lambda g: weightedSimilarity(g.split("|"), genreDictionary))
		nearest = allMovies.sort_values(by=['distance', 'title'], ascending=[False, True])
		
		recommendations = nearest.head(10)
	
	return recommendations

		
# Main menu
def mainMenu():
	print("\nMain Menu. Please choose an option:")
	print("\t1. Search Movies")
	print("\t2. Add MovieID to Selections")
	print("\t3. Show Current Selections")
	print("\t4. Show Recommendations")
	print("\n\t0. Quit")
	choice = input(" >>  ")
	try:
		choice = int(choice)
	except:
		choice = -1
	return choice

# Recommendations  
def showRecommendations():
	global userSelections, initialRecommendations
	if len(userSelections) == 0:
		recommendations = initialRecommendations
	else:
	  	recommendations = getRecommendations()
	print("Your movie recommendations:")
	displayMovies(recommendations)


# Start of the actual "logic" outside of function definitions:

initialRecommendations = getRecommendations()

choice = -1

print("Welcome to Daniel's movie recommender!\n")
while True:
	choice = mainMenu()
	if choice not in (1,2,3,4,0):
		print("Invalid choice: ", choice)
		continue # ask again
	elif choice == 0:
		break
	elif choice == 1:
		searchString = input("Search for movie: ")
		results = search(searchString)
		print(len(results.index), "movie results:")
		displayMovies(results)
	elif choice == 2:
		movieID = input("Enter MovieID to add to selection: ")
		try:
			movieID = int(movieID)
		except:
			print("Invalid MovieID")
			continue
		if movieID in allMovies.index:
			userSelections.add(movieID)
			print("You have added MovieID ", movieID, " to selections.  Title=", str(allMovies.loc[allMovies.index == movieID].iloc[0]['title']), sep="")
		else:
			print("That MovieID does not exist")
	elif choice == 3: # Show selections:
		if len(userSelections) != 0:
			selections = allMovies.loc[allMovies.index.isin(userSelections)]
			print("Your selected movies:")
			displayMovies(selections)
		else:
			print("You do not have any selected movies.")
	elif choice == 4: # Show recommendations
		showRecommendations()












