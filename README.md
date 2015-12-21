Movie Trailer Website

Description:

This application will generate an HTML file, producing a website that displays movies.  To view a trailer for a movie,
click its poster image.

The files in this project are the following (stored in the same root directory, movies):

media.py
entertainment_center.py
fresh_tomatoes.py

media.py defines the class Movie().  The class Movie() contains a constructor that takes four arguments used to create
an instance of the class. This class also contains the function show_trailer() that takes one argument (self) and can
be called to display the trailer of a movie in a web browser.

entertainment_center.py defines six Movie() objects.  It then defines the array [movies] with the six Movie() objects.
Then the function open_movies_page() is called.  This function is defined in fresh_tomatoes.py.  It accepts an array
of movies and generates an html web page that displays the posters for each movie object and runs the associated trailer
when the poster is clicked by the user.

To run this application place the three files in the same folder and run entertainment_center.py with python 3.5.
