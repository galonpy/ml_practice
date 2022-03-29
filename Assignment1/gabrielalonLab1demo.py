"""
CS3C, Assignment #1, Movie Objects and Classes
Gabriel Alon
Driver File
"""

from Assignment1.gabrielalonLab1 import Movie

if __name__ == '__main__':
    movie_list = Movie()

    new_movie = Movie(str("Monty Python and the Holy Grail"), int(1975))
    movie_list.add(new_movie)
    new_movie = Movie(str("On the Waterfront"), int(1954))
    movie_list.add(new_movie)
    new_movie = Movie(str("Cat on a Hot Tin Roof"), int(1958))
    movie_list.add(new_movie)

    (Movie.selection_menu())
    print("\n")
    print("Command: list")
    result_list = (movie_list.list())
    print("\n")
    type_x = None
    while type_x != "satisfied":
        try:
            type_x = input("Command: ")
            if type_x == "add":
                name = input("Name: ")
                year = input("Year: ")
                new_movie = Movie(str(name), int(year))
                if movie_list.add(new_movie) is True:
                    print(f"{name} was added")

            elif type_x == "del":
                index = input("Number: ")
                # retrieve index of actual list
                delete_name = movie_list.list(index)
                if movie_list.delete(index) is True:
                    print(f"{delete_name} was deleted")  # if its valid i think
            elif type_x == "list":
                result_list = (movie_list.list())
            elif type_x == "exit":
                print("Bye!")
                exit()
            print("\n")
            print("Command: list")
            result_list = (movie_list.list())
            print("\n")
        except Exception as e:
            if isinstance(e, SystemExit(code)):
                #causes the program to not print gross error message
                #when user calls exit triggering exit()
                pass
            else:
                raise ValueError("Invalid input {type_x}")
"""
COMMAND MENU
list - List all movies
add - Add a movie
del - Delete a movie
exit - Exit program


Command: list
1. Monty Python and the Holy Grail 1975
2. On the Waterfront 1954
3. Cat on a Hot Tin Roof 1958


Command: del
Number: 0


Command: list
1. Monty Python and the Holy Grail 1975
2. On the Waterfront 1954
3. Cat on a Hot Tin Roof 1958


Command: del
Number: 5


Command: list
1. Monty Python and the Holy Grail 1975
2. On the Waterfront 1954
3. Cat on a Hot Tin Roof 1958


Command: del
Number: 2
On the Waterfront was deleted


Command: list
1. Monty Python and the Holy Grail 1975
2. Cat on a Hot Tin Roof 1958


Command: add
Name: kndkjsadnfkajksdnkndkjsadnfkajksdnfkasdjnfkasdfasdf
Year: 2021
kndkjsadnfkajksdnkndkjsadnfkajksdnfkasdjnfkasdfasdf was added


Command: list
1. Monty Python and the Holy Grail 1975
2. Cat on a Hot Tin Roof 1958
3.  2021


Command: add
Name: bad_year
Year: 0
bad_year was added


Command: list
1. Monty Python and the Holy Grail 1975
2. Cat on a Hot Tin Roof 1958
3.  2021
4. bad_year 2021


Command: add
Name: Point break
Year: 2005
Point break was added


Command: list
1. Monty Python and the Holy Grail 1975
2. Cat on a Hot Tin Roof 1958
3.  2021
4. bad_year 2021
5. Point break 2005


Command: list
1. Monty Python and the Holy Grail 1975
2. Cat on a Hot Tin Roof 1958
3.  2021
4. bad_year 2021
5. Point break 2005


Command: list
1. Monty Python and the Holy Grail 1975
2. Cat on a Hot Tin Roof 1958
3.  2021
4. bad_year 2021
5. Point break 2005


Command: exit
Bye!
"""
