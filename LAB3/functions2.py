# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
# ex1 
def above_5_5(movie):
    return movie["imdb"] > 5.5
print(above_5_5(movies))

# ex 2
def filter_above_5_5(mlist):
    return [movie for movie in mlist if above_5_5(movie)]
print(filter_above_5_5(movies))

# ex 3
def filtercat(mlist, category):
    return [movie for movie in mlist if movie["category"] == category]
print(filtercat(movies, "Romance"))

# ex 4
def averagescore(mlist):
    if not mlist:
        return 0.0

    totscore = sum(movie["imdb"] for movie in mlist)
    return totscore / len(mlist)
print(averagescore(movies))

# ex 5
def averimbdcat(mlist, category):
    category_movies = filtercat( mlist, category)
    return averimbdcat (category_movies)
print(averimbdcat(movies, "Romance"))




