movies = [
{
    #0
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
    #1
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
    #2
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
    #3
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
    #4
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
    #5
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
    #6
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
    #7
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
    #8
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
    #9
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
    #10
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
    #11
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
    #12
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
    #13
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
    #14
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# Средний балл категории(жанра)
def avg_category_mov(mov,cat):
    cnt = 0
    y = 0
    for i in range(0,len(mov)):
        if mov[i]["category"] == cat:
            cnt+=mov[i]["imdb"]
            y+=1
    return (cnt/y)

print(avg_category_mov(movies,input()))