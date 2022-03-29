class Movie:
    DEFAULT_NAME = ""
    DEFAULT_YEAR = 1999


    def __init__(self,name=DEFAULT_NAME,year=DEFAULT_YEAR):
    #
        if self.strOK(name) is True: #or is it strOk
            self._name = name
            print("11")
        elif self.strOK(name) is False:
            self._name = '' #?
            print("17")
        if self.yearOK(year) is True:
            self._year = year
            print("14")
        elif self.yearOK(year) is False:
            self._year = 1999 #?
            print("20")
        self.__movieList = []


      #  self._name = name
       # self._year = year
        #if valid , else:
        #if mutator validation returns false set to default

    def list(self):
        print("Command: list")
        if len(self.__movieList) == 0:
            print("Out of movies...order more!")
        else:
            for i in range(0,len(self.__movieList)):
                print(f"{i+1}. {self.__movieList[i].getName()} ({self.__movieList[i].getYear()})")
        #print current movie list

    def add(self, movie):
        #is a mutator
        print("38")
        #if self.strOK(movie._name) is True and self.yeaOK(movie._year) is True:
         #   print("40")
        self.__movieList.append(movie)
        print("42")
        print(self.__movieList, "42+")
        return True
        #When the add / delete methods detect invalid parameter data no change of state to the movie list occurs.
        #self.__movieList.append(movie)

    def delete(self, index):
        #is a mutator

        #if self.strOK(self.__movieList[index]) is True and self.yearOK(self.__movieList[index]) is True:
        del self.__movieList[(int(index)-1)]
        return True

        #When the add / delete methods detect invalid parameter data no change of state to the movie list occurs.
    def selection_menu():
        print("COMMAND MENU")
        print("list - List all movies")
        print("add - Add a movie")
        print("del - Delete a movie")
        print("exit - Exit program")
        #display a selection menu

    def getStr(self):
        #string representation of a movie entry (e.g. a movie name and year).
        return(f"{self._name},{self._year}")

    def strOK(self, the_str): ###??? or strOk
        #validates str parameters and yearOK() that validates year parameters.
        """
        All legal strings should be of length  <= 50 consisting of printable characters.
        :return:
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

    def yearOK(self,the_year):
        """
       All legal ints should be > 1000 and < 2022.
        """
        if (the_year)>1000 or (the_year) < 2022:
            return True
        else:
            return False

    def setName(self,name):
        if strOk(name) is False:
            self._name = DEFAULT_NAME #default
            return False
        else:
            self._name = name

        #is a mutator
        #When the set methods detect invalid parameter data, the mutator returns False and a new default value is stored in that member.

        pass
    def setYear(self,year):
        if yearOK(year) is False:
            self._year = DEFAULT_YEAR #default arbitrary
            return False
        else:
            self._year = year

        #is a mutator

        #When the set methods detect invalid parameter data, the mutator returns False and a new default value is stored in that member.

    def getName(self):
        return self._name

    def getYear(self):
        return self._year
    #test driver?
if __name__ != '__main__':
    movie_list = Movie()
    print("passed 115")
    (Movie.selection_menu())
    type_x = None
    while type_x != "satisfied":
       # try:
        type_x = input("Command:")
        #do we force the input to be a value intrinsically or do we pseduo prompt command?
        if type_x == "add":
            name = input("Name:")
            year = input("Year:")
            print(name,year, "recieved")
            new_movie = Movie(str(name),int(year))
            print("128 reached")
            if movie_list.add(new_movie) is True:
                #movie_list.add(new_movie) #?
                print(f"{name} was added")  # if its valid i think
           # new_name = new_movie.list
           # print(new_name, "here is  138")
          #  new_name[-1].getName()
           # print("138")
           # result = new_movie.list
           # print(result, "here is result")
          #  print(Movie.__movieList, "here is Movie data")
        elif type_x == "del":
            index = input("Number:")
            #retrieve index of actual list
            delete_name = move_list.getName
            if movie_list.delete(index) is True:
                #either not deleting or deleting multiple times
                print(f"{delete_name} was deleted")  # if its valid i think
        elif type_x == "list":
            (movie_list.list())
            #or save list to var here and run whole print for loop that way i can retrieve for delete
        elif type_x == "exit":
            print("Bye!")
            exit()



        # if (type_x
       # except:
       #     print("erroe handle")
            
