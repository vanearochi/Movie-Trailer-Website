# Import files needed to create instances
# and to run the page
import fresh_tomatoes
import media

# Modules to obtain movies information
from imdb import IMDb
from wikiapi import WikiApi

#Variables to create Movie instances
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

#Store Movie variables in a list.
movie_instances_name = [cowspiracy, toy_story, birdman,
                        the_grand_budapest_hotel, monsters_inc,
                        finding_nemo, wreck_it_ralph, beginners,
                        django_unchained, pulp_fiction,
                        the_lord_of_the_rings_1, the_lord_of_the_rings_2,
                        the_lord_of_the_rings_3]

# Movies information: name and youtube id.
movies_info= [ {"name":
                    "Cowspiracy",
                 "id": "nV04zyfLyN4"},
               {"name":
                    'Toy Story',
                 "id": "KYz2wyBy3kc"},
                {"name":
                    "Birdman or (The Unexpected Virtue of Ignorance)",
                 "id": "uJfLoE6hanc"},
                {"name":
                     "The Grand Budapest Hotel",
                 "id":"1Fg5iWmQjwk"},
                {"name":
                     "Monsters Inc",
                 "id":"8IBNZ6O2kMk"},
                {"name":
                     "Finding Nemo",
                 "id":"2zLkasScy7A"},
                {"name":
                     "Wreck-it Ralph",
                 "id":"87E6N7ToCxs"},
                {"name":
                     "Beginners",
                 "id":"rXUFUp6vsxg"},
                {"name":
                     "Django Unchained",
                "id":"C3VjVMitTbA"},
                {"name":
                     "Pulp Fiction",
                 "id":"s7EdQ4FqbhY"},
                {"name":
                     "The Lord of the Rings: The Fellowship of the Ring",
                 "id": "V75dMMIW2B4"},
                {"name":
                     "The Lord of the Rings: The Two Towers",
                 "id": "LbfMDwc4azU"},
                {"name":
                     "The Lord of the Rings: The Return of the King",
                 "id": "r5X-hFf6Bwo"}
                ]


# Create Movie instances
def get_Movie_instance(movie_object):

    movie_title = movie_object["name"]

    # Concatenate youtube root with youtube id
    youtube_id = movie_object["id"]
    youtube_root = "https://www.youtube.com/watch?v="
    youtube_link = youtube_root + youtube_id

    # Search in IMDB for movie data
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

    # Search Wikipedia for movie image and link
    wikipedia_api= WikiApi()
    wikipedia_results = wikipedia_api.find(movie_title)
    wikipedia_first_match = wikipedia_api.get_article(wikipedia_results[0])
    wikipedia_image = wikipedia_first_match.image
    wikipedia_link = wikipedia_first_match.url

    return media.Movie(movie_title, movie_plot, wikipedia_image,
                       youtube_link, movie_director, wikipedia_link,
                       movie_writer, movie_cast, movie_genres, movie_rating)

#Get data from a list
def get_info_from_list(movie_data_list, key):
    #Restring list to 5 items if list have more than 5
    movie_data_list_length = len(movie_data_list)
    if movie_data_list_length > 5:
        movie_data_list = movie_data_list[:5]
    movie_info=""

    # Iterate over list or a list of objects
    for movie_data in movie_data_list:
        # Concatenate taken value
        if key == "no_key":
            movie_info = movie_info + ", " + movie_data
        else:
            movie_info = movie_info + ", " + movie_data[key]

    movie_info = movie_info[2:] + "."
    movie_info = movie_info.encode('utf-8')
    return movie_info

i=0
# Iterate over movie_info and movie_instances_name
for movie_information in movies_info:
    # Assign Movie instance to his corresponding variable
    movie_instances_name[i]=get_Movie_instance(movie_information)
    # Append Movie instance to movie list
    movies.append(movie_instances_name[i])
    i = i + 1

#Calls functions that creates and open web page
fresh_tomatoes.open_movies_page(movies)