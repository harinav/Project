import wikipedia

def releavent_search(word):
		#print(wikipedia.search(input))
	return  wikipedia.page(wikipedia.search(word)[0])
		#for i in range(len(wikipedia.search(input))):
       	 	#	return wikipedia.page(wikipedia.search(input)[i])
