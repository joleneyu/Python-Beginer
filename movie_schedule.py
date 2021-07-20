current_movies = {'A Quiet Place Part II': '5:30pm',
                  'Cruella': '7:20pm',
                  'Those who wish me dead': '6pm',
                  'Wrath of Man': '9:10pm'}
print("We're currently showing the following movies:")
for x in current_movies:
    print(x)

movie = input("What movie would you like the showtime for?\n")
showtime = current_movies.get(movie)
if showtime == None:
    print("The requested movie is not playing.")
else:
    print(movie, "is playing at", showtime)

