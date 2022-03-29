"""
CS3C, Assignment #1, Movie Objects and Classes
Gabriel Alon
Main File
"""


class Movie:
    DEFAULT_NAME = ""
    DEFAULT_YEAR = 2021

    def __init__(self, name=DEFAULT_NAME, year=DEFAULT_YEAR):
        """
        self.__movieList is a list of movies of class Movie
        :param name: name of movie
        :param year: year of movie
        """
        #
        self.setName(name)
        self.setYear(year)
        self.__movieList = []

    def list(self, *args):
        """
        Prints out Movies
        :param args: index
        :return: optional deleted value
        """
        try:
            if args:
                #     print(args,type(args), "here is args")
                return (self.__movieList[int(args[0]) - 1].getName())
            if len(self.__movieList) == 0:
                print("Out of movies...order more!")
            else:
                for i in range(0, len(self.__movieList)):
                    #  print(f"{i + 1}. {self.__movieList[i].getName()} ({self.__movieList[i].getYear()})") #worked
                    print(f"{i + 1}. {self.__movieList[i].getStr()}")
        except:
            pass

    def add(self, movie):
        """
        Adds valid movie to list
        :param movie: has a name and year
        :return: True if valid
        """
        self.__movieList.append(movie)

        return True

    def delete(self, index):
        """
        Deletes valid movie from list
        The delete method will want to ensure that the list is not empty
        and that the index is within valid range for the number of elements in the list
        :param movie: has a name and year
        :return: True if valid
        """
        # is a mutator
        if len(self.__movieList) > 0 and (int(index)-1 <= len(self.__movieList)) and int(index)>=1:
            del self.__movieList[(int(index) - 1)]
            return True

    def selection_menu():
        """
        Prints out Selection Menu for app
        :return: N/A
        """
        print("COMMAND MENU")
        print("list - List all movies")
        print("add - Add a movie")
        print("del - Delete a movie")
        print("exit - Exit program")

    def getStr(self):
        """
        :return name and year of movie
        """
        # string representation of a movie entry (e.g. a movie name and year).
        return (f"{self._name} {self._year}")

    def strOK(self, the_str):  ###??? or strOk
        # validates str parameters and yearOK() that validates year parameters.
        """
        :param name
        All legal strings should be of length  <= 50 consisting of printable characters.
        :return: True if Valid Else False
        """
        if len(the_str) <= 50:
            for achar in the_str:
                if (achar.isprintable()):
                    pass
                else:
                    return False
            return True
        else:
            return False

    def yearOK(self, the_year):
        """
       :param year
       All legal ints should be > 1000 and < 2022.
       :return True if Valid Else False
        """
        if (the_year) > 1000 and (the_year) < 2022:
            return True
        else:
            return False

    def setName(self, name):
        """
        :param name
        :return Set Name value Else False
        """
        if self.strOK(name) is False:
            self._name = self.DEFAULT_NAME  # default
            return False
        else:
            self._name = name

    def setYear(self, year):
        """
        param: year
        :return Year value Else False
        """
        if self.yearOK(year) is False:
            self._year = self.DEFAULT_YEAR  # default arbitrary
            return False
        else:
            self._year = year

    def getName(self):
        """
        :return: name
        """
        return self._name

    def getYear(self):
        """
        :return: year
        """
        return self._year
