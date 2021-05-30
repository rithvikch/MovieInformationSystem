import requests # python requests library
from colorama import Fore # style colors
from os import name, system 
from time import sleep
from PIL import Image
import sys
from Movie import Movie # from other movie class

# loading screen animation

def loadingScreen(length):
    if name == 'nt':
        key = 'cls'
    else:
        key = 'clear'

    _ = system(key)
    for i in range(5):
        print(Fore.GREEN + "Loading")
        sleep(length)
        _ = system(key)
        print(Fore.GREEN + "Loading.")
        sleep(length)
        _ = system(key)
        print(Fore.GREEN + "Loading..")
        sleep(length)
        _ = system(key)
    print(Fore.RESET)

# finds all movies based on given name
def findMovies(moviename):
    server = "http://www.omdbapi.com/?i=tt3896198&apikey=7be6a6a6" # server 
    #original brief overview parameters
    parameters = {
    
        's' : moviename
    }
    response = requests.get(server, params=parameters)

    movies = response.json()
    #redeclare empty parameters
    par = { 

    }
    #checks if api request works ok
    if movies['Response'] == 'False':
        print(Fore.LIGHTBLUE_EX + "Sorry. We were not able to find this particular movie.. Please rerun the program and correct the the name of the movie.")
        sys.exit()
   
    
    else:
        check = False
        print(Fore.LIGHTBLUE_EX + "\n\nCongrats. We were able to find " + movies['totalResults'] + " matches. Please hold while our system processes.")
        sleep(2)
        loadingScreen(0.25) #animation
        #adds specific movie objects with specific parameters which return large descriptions for each movie
        for movie in movies['Search']: 
            par = {
                't' : movie['Title']
            }
            
            if requests.get(server,params=par).json()['Response'] != 'False':
                all.append(Movie(requests.get(server,params=par).json()))
                
                quest = input(Fore.LIGHTMAGENTA_EX  +"Is " +  Fore.GREEN + movie['Title'] + ": " + movie['Year'] + ", directed by " + all[0].getDirector() + Fore.LIGHTMAGENTA_EX + " the movie you're looking for? (y/n)\n\t>").lower()

            while quest != 'y' and quest != 'n':
                print(Fore.RED + "No. Please enter y or n. ")
                quest = input("\t>")
                if quest == 'y' or quest == 'n':
                    break
            
            if quest == 'y':
                check = True

                break
                
            else:
                if len(all) > 0: all.pop()
                print(Fore.GREEN + "Ok then.\n\n")

        if check == False:
            print(Fore.LIGHTBLUE_EX + "Sorry. We weren't able to find your movie.. Please rerun the program and correct the the name of the movie or choose another real movie. ")
            sys.exit()
        loadingScreen(0.25)


ans = ""      
while ans != "n":
    all = []

    option = int(input(Fore.LIGHTMAGENTA_EX + "Welcome to the world's most advanced ~ ~ Movie/Series Information System ~ ~\n\n What would you like to do today?\n(1: Get information about a movie  2: Compare a movie with another)\n\n\t>"))

    while option != 1 and option != 2:
        print(Fore.RED + "No. Please enter 1 or 2. ")
        option = int(input("\t>"))
        if option == 1 or option == 2:
            break

    loadingScreen(0.25)
    if (option == 1):
        moviename = input(Fore.LIGHTMAGENTA_EX + "Ok. Please enter the movie/series that you would like to learn more about\n\t>")
        findMovies(moviename)
        loadingScreen(0.25)
        print(all[0].print())
        all[len(all)-1].display()

    
    else:
        movie1name = input(Fore.LIGHTMAGENTA_EX + "Ok. Please enter the first movie/series that you would like to compare\n\t>")
        findMovies(movie1name)
        movie1 = all.pop()
        movie2name = input(Fore.LIGHTMAGENTA_EX + "Ok. Please enter the second movie/series that you would like to learn more about\n\t>")
        findMovies(movie2name)
        movie2 = all.pop()
        print(movie1, movie2)

        print("Ok. We have successfully collected the data for both. The comparision will start now. ")




        sleep(3)
        movie1.compareTo(movie2)

        input(Fore.LIGHTBLUE_EX + "\n\n\nPress enter to see the info of both movies\n\t>")
        movie1.display()
        movie2.display()



    
    ans = input(Fore.LIGHTMAGENTA_EX + "Would you like to learn or compare another movie/series?(y/n)\n\t> ")

    while ans != "y" and ans != "n":
        print(Fore.RED + "No. Please enter y or n. ")
        ans = input("\t>")
        if ans == "y" or ans == "n":
            break

if name == 'nt':
    key = 'cls'
else:
    key = 'clear'
__ = system(key)
print(Fore.RESET + "Oh well. Thanks for playing!\n\n")
