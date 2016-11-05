#We need this files
import fresh_tomatoes
import media
from urllib2 import Request, urlopen, URLError
import wikipedia
# We need this modules to obtain movies information
from imdb import IMDb
from wikiapi import WikiApi

#Defining variables to create Movie instances
cowspiracy=""
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

#We store the variables above in a list.
movie_instances_name = [cowspiracy, toy_story, birdman, the_grand_budapest_hotel,
                        monsters_inc, finding_nemo, wreck_it_ralph, beginners,
                        django_unchained, pulp_fiction, the_lord_of_the_rings_1,
                        the_lord_of_the_rings_2, the_lord_of_the_rings_3]

#This list contains the information of movies
# that we need to begin the search in the modules imported
movies_info= [ {"name": "Cowspiracy",
                 "id": "nV04zyfLyN4"},
               {"name":'Toy Story',
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

#This function creates search movie information on modules,
#creates Movie instances with it and return them
def get_Movie_instance(movie_object):

    movie_title = movie_object["name"]
    youtube_id = movie_object["id"]
    youtube_root = "https://www.youtube.com/watch?v="
    youtube_link = youtube_root + youtube_id
    imdb = IMDb()
    movie_search = imdb.search_movie(movie_title)
    first_match =  movie_search[0]
    imdb.update(first_match)
    movie_data = first_match.data
    movie_director = get_info_from_list(movie_data['director'], "name")
    movie_writer = get_info_from_list(movie_data['writer'], "name")
    movie_cast = get_info_from_list(movie_data['cast'], "name")
    movie_rating = str(movie_data['rating'])
    movie_rating = movie_rating.encode('utf-8')
    movie_genres = get_info_from_list(movie_data['genres'], "no_key")
    movie_plot = get_info_from_list(movie_data['plot'], "no_key")
    wikipedia_api= WikiApi()
    wikipedia_results = wikipedia_api.find(movie_title)
    wikipedia_first_match = wikipedia_api.get_article(wikipedia_results[0])
    wikipedia_image = wikipedia_first_match.image
    wikipedia_link = wikipedia_first_match.url

    return media.Movie(movie_title, movie_plot, wikipedia_image,
                       youtube_link, movie_director, wikipedia_link,
                       movie_writer, movie_cast, movie_genres, movie_rating)

#Gets information from a list
#iterating over it
def get_info_from_list(movie_data_list, key):
    movie_data_list_length = len(movie_data_list)
    if movie_data_list_length > 5:
        movie_data_list = movie_data_list[:5]
    movie_info=""

    for movie_data in movie_data_list:
        if key == "no_key":
            movie_info = movie_info + ", " + movie_data
        else:
            movie_info = movie_info + ", " + movie_data[key]

    movie_info = movie_info[2:] + "."
    movie_info = movie_info.encode('utf-8')
    return movie_info

i=0
#Iterates over movie_info and movie_instances_name
#Assigns instance to variable
for movie_information in movies_info:
    movie_instances_name[i]=get_Movie_instance(movie_information)
    movies.append(movie_instances_name[i])
    i = i + 1

#Calls functions that creates and open web page
fresh_tomatoes.open_movies_page(movies)