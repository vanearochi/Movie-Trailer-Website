#
import fresh_tomatoes
import media
from urllib2 import Request, urlopen, URLError
import wikipedia
from imdb import IMDb
from wikiapi import WikiApi

toy_story=""
birdman=""
the_grand_budapest_hotel=""
monsters_inc =""
finding_nemo=""
wreck_it_ralph=""
beginners=""
django_unchained=""
pulp_fiction=""
the_lord_of_the_rings_1=""
the_lord_of_the_rings_2=""
the_lord_of_the_rings_3=""
movies = []

movies_var = [toy_story, birdman, the_grand_budapest_hotel, monsters_inc, finding_nemo, wreck_it_ralph, beginners, django_unchained, pulp_fiction, the_lord_of_the_rings_1, the_lord_of_the_rings_2, the_lord_of_the_rings_3]

movie_titles = [{"name":'Toy Story',
                 "id": "KYz2wyBy3kc"},
                {"name":"Birdman or (The Unexpected Virtue of Ignorance)",
                 "id": "uJfLoE6hanc"},
                {"name":"The Grand Budapest Hotel",
                 "id":"1Fg5iWmQjwk"},
                {"name":"Monsters Inc",
                 "id":"8IBNZ6O2kMk"},
                {"name":"Finding Nemo",
                 "id":"2zLkasScy7A"},
                {"name":"Wreck-it Ralph",
                 "id":"87E6N7ToCxs"},
                {"name":"Beginners",
                 "id":"rXUFUp6vsxg"},
                {"name":"Django Unchained",
                "id":"C3VjVMitTbA"},
                {"name":"Pulp Fiction",
                 "id":"s7EdQ4FqbhY"},
                {"name": "The Lord of the Rings: The Fellowship of the Ring",
                 "id": "V75dMMIW2B4"},
                {"name": "The Lord of the Rings: The Two Towers",
                 "id": "LbfMDwc4azU"},
                {"name": "The Lord of the Rings: The Return of the King",
                 "id": "r5X-hFf6Bwo"}
                ]



#ass = ia.update(peli)



#b = ia.get_movie(a[0].id)
#for item in a:
     #print item['long imdb canonical title']
    #movie_id =item.movieID
    #b = ia.get_movie_plot(movie_id)
    #print b



def create_Movie_instance(movie_object):
    # type: (object) -> object

    movie_title = movie_object["name"]
    youtube_id = movie_object["id"]
    #print  youtube_id
    youtube_root = "https://www.youtube.com/watch?v="
    youtube_link = youtube_root + youtube_id
    #print youtube_link
    imdb = IMDb()

    movie_search = imdb.search_movie(movie_title)
    movie_id = movie_search[0].getID()
    #print movie_search[0].smartCanonicalTitle()
    name_long= movie_search[0]
    print name_long
    plot = imdb.get_movie_plot(movie_id)
    plot_object = plot.__getitem__("data")
    plot_text = plot_object['plot'][0]
    #print plot_text

    #wikipage = wikipedia.page(page)

    #print plot_object.__getitem__("plot")
    review = imdb.get_movie_critic_reviews(movie_id)
    #print review
    #print imdb.get_movie_episodes_cast





        #$print long_title




        #imdb_init = IMDb()
        #print imdb_init.g
    wiki= WikiApi()
    results = wiki.find(movie_title)
    print results
    #print name_long
    #print results
    article = wiki.get_article(results[0])
    print article
    wiki_image = article.image
    print article.heading

    #print wiki_image

    return media.Movie(name_long, plot_text, wiki_image, youtube_link)
        #print wiki_plot.summary
        #return wiki_plot

    #wiki_search_id = WikipediaPage(title= movie_title, pageid = wiki_plot.pageid)
    #print wiki_search_id.images

#wiki_search("toy story")
#wikipage= wikipedia.page(page)
#print wiki.title
#print wiki.url
#print wiki.image
#print wiki

#create_Movie_instance("monsters inc")
i = 0
for movie_obj in movie_titles:
    movies_var[i]=create_Movie_instance(movie_obj)
    movies.append(movies_var[i])
    i = i + 1
    print movies
    #print movies_var[i]

#movies=[toy_story]



#Movie instances
#toy_story = create_Movie_instance(movie_titles[0])
#print toy_story.title
#birdman = create_Movie_instance(movie_titles[1])
#the_grand_budapest_hotel = create_Movie_instance(movie_titles[2])
#the_lord_of_the_rings_1 = create_Movie_instance(movie_titles[3])
#the_lord_of_the_rings_2 = create_Movie_instance(movie_titles[4])
#the_lord_of_the_rings_3 = create_Movie_instance(movie_titles[5])

#monsters_inc = create_Movie_instance(movie_titles[6])
#ratatouille = create_Movie_instance(movie_titles[7])
#moulin_rouge = create_Movie_instance(movie_titles[8])
#a = create_Movie_instance(movie_titles[9])
#b = create_Movie_instance(movie_titles[10])
#c = create_Movie_instance(movie_titles[11])


#Array of movie instances pass to
#movies = [toy_story, birdman, the_grand_budapest_hotel, monsters_inc, ratatouille, moulin_rouge, beginners, sin_city, the_lord_of_the_rings_1, the_lord_of_the_rings_2, the_lord_of_the_rings_3, a, b, c]
#movies=[toy_story]
fresh_tomatoes.open_movies_page(movies)