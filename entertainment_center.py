import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
birdman = media.Movie("Birdman",
                      "Illustrated upon the progress of his latest Broadway play, a former popular actor's struggle to cope with his current life as a wasted actor is shown.",
                      "https://upload.wikimedia.org/wikipedia/en/6/63/Birdman_poster.png",
                      "https://www.youtube.com/watch?v=uJfLoE6hanc")
the_grand_budapest_hotel = media.Movie("The Grand Budapest Hotel",
                                       "The adventures of Gustave H, a legendary concierge at a famous hotel from the fictional Republic of Zubrowka between the first and second World Wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend.",
                                       "https://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
                                       "https://www.youtube.com/watch?v=1Fg5iWmQjwk")
the_lord_of_the_rings_1 = media.Movie("The Lord of the Rings:<br>The Fellowship of the Ring",
                                      "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle Earth from the Dark Lord Sauron.",
                                      "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                                      "https://www.youtube.com/watch?v=V75dMMIW2B4")
the_lord_of_the_rings_2 = media.Movie("The Lord of the Rings:<br> The Two Towers",
                                      "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard.",
                                      "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                                      "https://www.youtube.com/watch?v=LbfMDwc4azU")
the_lord_of_the_rings_3 = media.Movie("The Lord of the Rings:<br>The Return of the King",
                                      "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
                                      "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                                      "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

monsters_inc = media.Movie("Monsters Inc.",
                           "In order to power the city, monsters have to scare children so that they scream. However, the children are toxic to the monsters, and after a child gets through, two monsters realize things may not be what they think.",
                           "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
                           "https://www.youtube.com/watch?v=8IBNZ6O2kMk")
ratatouille = media.Movie("Ratatouille",
                          "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=87q0RD5R4Us")
moulin_rouge = media.Movie("Moulin Rouge",
                           "A poet falls for a beautiful courtesan whom a jealous duke covets in this stylish musical, with music drawn from familiar 20th century sources.",
                           "https://upload.wikimedia.org/wikipedia/en/9/9f/Moulin_rouge_poster.jpg",
                           "https://www.youtube.com/watch?v=2PpgPxjzbkA")


movies = [toy_story, birdman, the_grand_budapest_hotel, monsters_inc, ratatouille, moulin_rouge, the_lord_of_the_rings_1, the_lord_of_the_rings_2, the_lord_of_the_rings_3]
fresh_tomatoes.open_movies_page(movies)