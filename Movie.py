from PIL import Image
import numpy as np
import urllib.request
from colorama import Fore
from time import sleep
class Movie:

    def __init__(self, mov):
        self.mov = mov
    
    def getTitle(self):
        return self.mov['Title']

    def print(self):
     return self.mov

    def getYear(self):
        return self.mov['Year']

    def getActors(self):
        return self.mov['Actors']

    def getDirector(self):
        return self.mov['Director']
    
    def getPlot(self):
        return self.mov['Plot']

    def getLanguage(self):
        return self.mov['Language']

    def getBoxOffice(self):
        return self.mov['BoxOffice']
    def display(self):                                                                    
        print(Fore.RESET + "Title: " +Fore.GREEN +  self.getTitle(), end = "     ")
        print(Fore.RESET + "Directed by " + Fore.GREEN + self.getDirector())
        print(Fore.RESET + "\nMade in " + Fore.GREEN + self.getYear())
        print(Fore.RESET + "\tCast: " + Fore.GREEN + self.getActors())
        print(Fore.RESET + "\tLanguage: " + Fore.GREEN + self.getLanguage())
        
        if self.mov['Type'] != 'series':
            print(Fore.RESET + "\tBox Office: " + Fore.GREEN +  self.getBoxOffice())
        
        
        print(Fore.RESET + "\tCountry: " + Fore.GREEN + self.mov['Country'])
        print(Fore.RESET + "\n\tAwards: " + Fore.GREEN + self.mov['Awards'])
        if self.mov['Type'] == 'series':
            print(Fore.RESET + "\n\n\tSeasons: " + Fore.GREEN + self.mov['totalSeasons'])
        print(Fore.RESET + "\n\n\tRatings: ")
        for i in range(len(self.mov['Ratings'])):
            print(Fore.RESET + "\t\t" +  Fore.GREEN + self.mov['Ratings'][i]['Source'] + ": " + self.mov['Ratings'][i]['Value'])
        print(Fore.RESET + "\n\t\t\tPlot: " +  Fore.LIGHTCYAN_EX + self.getPlot() + "\n\n")
        

        
        input( Fore.RESET + "Click enter to see the poster : )\n\t>")
        urllib.request.urlretrieve(self.mov['Poster'], "img.jpg")

        im = Image.open("img.jpg")
        im.show()

    def compareTo(self, other):
        if self.mov['imdbRating'] == 'N/A'or other.print()['imdbRating'] == 'N/A':
            print("SHTOP IT! GIK DOCHUNT WOHK!!!! Unfortunately, some ratings are missing. We apologize for this inconvenience")
            return False
        if self.mov['Metascore'] != 'N/A' and other.print()['Metascore'] != 'N/A':
            movie1total = ((float(self.mov['Metascore']) + float(self.mov['imdbRating']))/110.0)*100
            movie2total = ((float(other.print()['Metascore']) + float(other.print()['imdbRating']))/110.0)*100
        else:
            movie1total =  self.mov['imdbRating']
            movie2total = other.print()['imdbRating']
        print(Fore.RESET + "\n\n\t" + self.getTitle() + " Ratings: ")
        for i in range(len(self.mov['Ratings'])):
            print(Fore.RESET + "\t\t" +  Fore.GREEN + self.mov['Ratings'][i]['Source'] + ": " + self.mov['Ratings'][i]['Value'])        


        print(Fore.RESET + "\n\n\t" + other.print()['Title'] + " Ratings: ")
        for i in range(len(other.print()['Ratings'])):
            print(Fore.RESET + "\t\t" +  Fore.GREEN + other.print()['Ratings'][i]['Source'] + ": " + other.print()['Ratings'][i]['Value'])   
        
        if (movie1total > movie2total):
            print(Fore.RESET + "\n\t\t\t" + "The better movie/series is " + Fore.GREEN + self.getTitle() + Fore.RESET  +  " because it had an average overall rating of " + str(movie1total) + " while " + Fore.GREEN +  other.print()['Title'] + Fore.RESET + " had an average overall rating of " + str(movie2total))

        elif (movie2total > movie1total):
            print(Fore.RESET + "\n\t\t\t" + "The better movie/series is " + Fore.GREEN + other.print()['Title'] + Fore.RESET  +  " because it had an average overall rating of " + str(movie2total) + " while " + Fore.GREEN +  self.getTitle() + Fore.RESET + " had an average overall rating of " + str(movie1total))

        else:
            print(Fore.RESET + "\n\t\t\t" + "Both movies have the same overall rating: " + Fore.GREEN + self.getTitle() + Fore.RESET  +  " has an average overall rating of " + str(movie1total) + " and " + Fore.GREEN +  other.print()['Title'] + Fore.RESET + " has an average overall rating of " + str(movie2total))
