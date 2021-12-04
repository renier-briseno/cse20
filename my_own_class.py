""" 
Renier Briseno
CSE20 - Intro to Python
12/3/21

Assignment 10.1: Your Own Class


ACKNOWLEDGEMENTS:



"""


# Importing time module for dramatic effect
import time




# This class is about movies
class Movies:
# Here are some class variables
    director = "Renier T. Briseno"
    favorites_list = []
# Construcor function
    def __init__(self, name, genre, rating):
# Private variables
        self.__name = name
        self.__genre = genre
        self.__rating = rating
# get_name returns name
    def get_name(self):
        return (self.__name)
# get_genre returns genre
    def get_genre(self):
        return(f"This is a {self.__genre} movie.")
# get_rating returns rating
    def get_rating(self):
        return(f"The rating for this movie is {self.__rating}.")
# set_favorite adds movie to favorites list
    def set_favorite(self):
        self.favorites_list.append(self.__name)
        print(f"{self.__name} set to favorites. Favorites list: ")
        return self.favorites_list
# download "downloads" the movie (not really)
    def download(self):
        for num in range(0, 3):
            time.sleep(.5)
            print(".")
        return("Download complete.")
# watch, "watches the movie"
    def watch(self):
# ALL OF THIS CODE IS THE MOVIE "PLAYING"
# THIS IS ALL JUST FOR SHOW
# YOU CAN SKIP TO THE NEXT FUNCTION IF YOU'D LIKE
        time.sleep(1)
        print(f"Directed by: {self.director}...")
        time.sleep(2)
        print(f"Written/Produced by {self.director}...")
        time.sleep(3)
        print(f"Rated: {self.__rating}")
        time.sleep(2)
        print("Dun Dun Dun... Intro Music Intro Music etc.")
        time.sleep(3)
        print("Main character meets supporting character etc.")
        time.sleep(2)
        print("Perhaps,")
        time.sleep(1)
        print("Falls in love?")
        time.sleep(2)
        print("Dialog between characters blah blah plot thickens")
        time.sleep(2)
        print("The Action begins to Rise...")
        time.sleep(2)
        print("CLIMAX DUN DUN DUN DUN ACTION SCENE DUN DUN")
        time.sleep(2)
        for num in range(0, 3):
            time.sleep(.5)
            print(".")
        print("The hero...")
        time.sleep(1)
        print("Rises against all odds...")
        time.sleep(1)
        print("And overcomes whatever the challenge was.")
        time.sleep(2)
        return ("THE END.")





# This function will act like a streaming service
# You can navigate the service using text commands
# You can "click" on different things to get more
# information about the movies and interact with
# the service
def streaming_service(movie_dict, scary_list, funny_list, rom_com_list, scary_object_list, funny_object_list, rom_com_object_list):
# This num is to browse through the list of movies
    num = 1
# This flag is to break out of inner while Loop
    flag = True
# This while loop is the outer program of the service
# it just welcomes and exits the shell
    while True:
# Welcoming the user to the program
        print("\n")
        print("Hello, welcome to MoviePlus! Enter 'next' to go to next genre")
# This flag controlled loop is the main area of interaction
        while flag:
# The first num is the first page of movies (Scary ones)
            if num == 1:
        
                print("\t")
                print("Page 1")
                print("Scary Movies:")
                print("\n")
# Print out all the movies in this page
                for movie in movie_dict["Scary"]:
                    print("\t-",movie)
                print("\n")
                print("Type movie name to interact. next for next page, and exit to exit program.")
# Ask user what they would like to do
                next_move = input(">>> ")



# Parse through movies in the Scary dictionary key
                for movie in movie_dict["Scary"]:
# When the movie inputted matches the value in the list...
                    if next_move == movie:
# Set variable specific_movie to be the 

                        """
                ****** IMPORTANT COMMENT ******
This is the bulk of the code, really. By setting the movie inputted by
the user to the variable 'specific_movie', we are able to access all of that
movies' Class variables and methods.

The options given after choosing which movie they want will reflect those
Class variables and objects. 
                        """


                        if scary_list.index(movie) == 0:
                            specific_movie = scary_object_list[0]
                        elif scary_list.index(movie) == 1:
                            specific_movie = scary_object_list[1]
                        elif scary_list.index(movie) == 2:
                            specific_movie = scary_object_list[2]
# Ask what the user would like to do with the movie
                        while True:
                            command = input(f"Available commands for {movie} are: name, genre, rating, favorite, download, watch, exit: ")
# If they want the name of the movie...
                            if command == "name":
# Call the get_name() method for the specific movie
                                print(specific_movie.get_name())
# Same goes for the other commands, using the respective class methods
                            elif command == "genre":
                                print(specific_movie.get_genre())
                            elif command == "rating":
                                print(specific_movie.get_rating())
                            elif command == "favorite":
                                print(specific_movie.set_favorite())
                            elif command == "download":
                                print(specific_movie.download())
                            elif command == "watch":
                                print(specific_movie.watch())
# If they choose exit, exit to movie menu
                            elif command == "exit":
                                break

                if next_move == "next":
                    num += 1
                elif next_move == "exit":
                    flag = False
                    break





# Second page movie options (Comedy ones)
            elif num == 2:
                print("\t")
                print("Page 2")
                print("Comedy Movies:")
                print("\n")
# Print comedy movie titles
                for movie in movie_dict["Comedy"]:
                    print("\t-",movie)
                print("\n")
                print("Type movie name to interact. next for next page, and exit to exit program.")
                next_move = input(">>> ")

# Parse through movies in the Comedy dictionary key
                for movie in movie_dict["Comedy"]:
# When the movie inputted matches the value in the list...
                    if next_move == movie:
# Set variable specific_movie to be the 
                        if funny_list.index(movie) == 0:
                            specific_movie = funny_object_list[0]
                        elif funny_list.index(movie) == 1:
                            specific_movie = funny_object_list[1]
                        elif funny_list.index(movie) == 2:
                            specific_movie = funny_object_list[2]
# Ask what the user would like to do with the movie
                        while True:
                            command = input(f"Available commands for {movie} are: name, genre, rating, favorite, download, watch, and exit: ")
# If they want the name of the movie...
                            if command == "name":
                                print(specific_movie.get_name())
# Same goes for the other commands, using the respective class methods
                            elif command == "genre":
                                print(specific_movie.get_genre())
                            elif command == "rating":
                                print(specific_movie.get_rating())
                            elif command == "favorite":
                                print(specific_movie.set_favorite())
                            elif command == "download":
                                print(specific_movie.download())
                            elif command == "watch":
                                print(specific_movie.watch())
# If they choose exit, exit to movie menu
                            elif command == "exit":
                                break

# If next, next pageg
                if next_move == "next":
                    num += 1
                elif next_move == "exit":
                    flag = False
                    break





# Third page movies (Romance ones)
            elif num == 3:
                print("\t")
                print("Page 3")
                print("Romance Movies:")
                print("\n")
# Print movie options
                for movie in movie_dict["Romance"]:
                    print("\t-",movie)
                print("\n")
                print("Type movie name to interact. next for next page, and exit to exit program.")
                next_move = input(">>> ")

# Parse through movies in the Scary dictionary key
                for movie in movie_dict["Romance"]:
# When the movie inputted matches the value in the list...
                    if next_move == movie:
# Set variable specific_movie to be the respective Movies object

                        
                        if rom_com_list.index(movie) == 0:
                            specific_movie = rom_com_object_list[0]
                        elif rom_com_list.index(movie) == 1:
                            specific_movie = rom_com_object_list[1]
                        elif rom_com_list.index(movie) == 2:
                            specific_movie = rom_com_object_list[2]

# Ask what the user would like to do with the movie
                        while True:
                            command = input(f"Available commands for {movie} are: name, genre, rating, favorite, download, watch, and exit: ")

# If they want the name of the movie...
                            if command == "name":
# We call the get_name() method for the specific movie
                                print(specific_movie.get_name())
# Same goes for the other commands, using the respective class methods
                            elif command == "genre":
                                print(specific_movie.get_genre())
                            elif command == "rating":
                                print(specific_movie.get_rating())
                            elif command == "favorite":
                                print(specific_movie.set_favorite())
                            elif command == "download":
                                print(specific_movie.download())
                            elif command == "watch":
                                print(specific_movie.watch())
# If they choose exit, exit to movie menu
                            elif command == "exit":
                                break


                if next_move == "next":
                    num += 1
# Break out of loop if they exit
                elif next_move == "exit":
                    flag = False
                    break

# Loop around to page one if you reach the last page and increase counter
            elif num == 4:
                num = 1

            
            
        break















        
def create_movies():

# To 'analyze' our movie data, we will need a few lists
# This master dictionary will contain all the info about the movie
    movie_dict = {}
# The movie lists contains the name of the movies
    scary_list = []
# The movie object like contains the actual Movie object
    scary_object_list = []
# This goes for the funny movies and the romantic movies as well
    funny_list = []
    funny_object_list = []
    rom_com_list = []
    rom_com_object_list = []

# Here we append the name and Movie object to the respective list
    scary_movie1 = Movies("Creepy House", "gritty/dark", "R")
    scary_object_list.append(scary_movie1)
    scary_list.append(scary_movie1.get_name())

# Same goes for every other movie in the repository...
    scary_movie2 = Movies("The Underground Asylum", "psychological thriller", "PG")
    scary_object_list.append(scary_movie2)
    scary_list.append(scary_movie2.get_name())

    scary_movie3 = Movies("I'm Not Scared of That", "comedy/horror", "PG-13")
    scary_object_list.append(scary_movie3)
    scary_list.append(scary_movie3.get_name())

    funny_movie1 = Movies("What's Up With That??", "comedy", "PG-13")
    funny_object_list.append(funny_movie1)
    funny_list.append(funny_movie1.get_name())

    funny_movie2 = Movies("Brothers. In. Law.", "comedy", "PG")
    funny_object_list.append(funny_movie2)
    funny_list.append(funny_movie2.get_name())

    funny_movie3 = Movies("School Daze: The Last Toke", "comedy", "R")
    funny_object_list.append(funny_movie3)
    funny_list.append(funny_movie3.get_name())

    rom_com1 = Movies("Boy Meets Girl", "romance", "PG")
    rom_com_object_list.append(rom_com1)
    rom_com_list.append(rom_com1.get_name())

    rom_com2 = Movies("She", "romance", "PG-13")
    rom_com_object_list.append(rom_com2)
    rom_com_list.append(rom_com2.get_name())

    rom_com3 = Movies("Divorce, Reimagined", "romantic comedy", "G")
    rom_com_object_list.append(rom_com3)
    rom_com_list.append(rom_com3.get_name())


    movie_dict["Scary"] = scary_list
    movie_dict["Comedy"] = funny_list
    movie_dict["Romance"] = rom_com_list

# Returning all of the lists and dictionary used to analyze data
    return movie_dict, scary_list, funny_list, rom_com_list, scary_object_list , funny_object_list, rom_com_object_list






def main():

# First we return all of the lists so we can use 
# all the data in the shell program
    movie_dict, scary_list, funny_list, rom_com_list, scary_object_list, funny_object_list, rom_com_object_list  = create_movies()

# This next function is a shell for a pseudo- 
# movie streaming service
    streaming_service(movie_dict, scary_list, funny_list, rom_com_list, scary_object_list, funny_object_list, rom_com_object_list)







# Calling main function
if __name__ == "__main__":
    main()