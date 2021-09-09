# DistanceToMKAD
The following project is a Flask based app to find the distance from Moscow Ring Road to an specified address. If the address is located inside the Moscow Ring Road or if it is not found by our geolocator it is not calculated, else the application returns the address found on the geolocator along with its latitude, longitude and distance to it. 

## Code style
During the realization of the project we utilize [PEP8](https://pep8.org) code compliance and use of type annotations. 
## Tech/framework used
- [Atom](https://atom.io) - A hackable text editor
- [Python](https://www.python.org) - awesome programming language to work quickly and integrate systems effectively
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - micro web framework written in Python
- [Geopy](https://geopy.readthedocs.io/en/stable/) - Python client for several geocoding web services
- [Pandas](https://pandas.pydata.org) - is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool
- [Shapely](https://shapely.readthedocs.io/en/stable/) - Shapely is a BSD-licensed Python package for manipulation and analysis of 

## Installation
In order to run the application you must have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) in your computer. Once they are installed let's install all the other needed libraries by running the following commands on our terminal:

```sh
$ pip install Flask
```
```sh
$ pip install geopy
```
```sh
pip install pandas
```
```sh
pip install shapely
```
Lets now import the folder project into our workspace by cloning the repository from either 
Github:
```sh
$ git clone https://github.com/tapiatellez/distance_to_MKAD
```
Gitlab:
```sh
$ git clone https://gitlab.com/tapiatellez/distance_to_MKAD
```
or Bitbucket:
```sh
$ git clone https://bitbucket.org/tapiatellez/distance_to_mkad
```
We can now run the application on developer mode with the following command:
```sh
$ python3 app.py
```
We will see the following output:
```sh
* Serving Flask app 'app' (lazy loading)

* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: on
```
Now we can go into [our localhost port 5000](http://localhost:5000) and utilize the app.

## Test

In order to test our blueprint, we can use the test.py file as follows:
```sh
$ python3 test.py -v
```
The output will be the following:
```sh
test_address_correct (__main__.FlaskTestCase)
Testing page with a retrievable address ... ok
test_address_empty (__main__.FlaskTestCase)

Test for a null address. ... ok
test_address_incorrect (__main__.FlaskTestCase)
Testing page for an unretrievable address. ... ok
test_address_inside_mkad (__main__.FlaskTestCase)
Test for an address inside of MKAD location. ... ok
test_address_page (__main__.FlaskTestCase)
Ensure index page loads the correct html. ... ok
test_index (__main__.FlaskTestCase)
Ensure that flask was set up correctly. ... ok

----------------------------------------------------------------------
Ran 6 tests in 1.521s

OK
```

## Docker

DistanceToMKAD is very easy to install and deploy in a Docker container. 
In the terminal and with [Docker](https://docs.docker.com/get-docker/) installed in your computer type the following
to pulled down the image and eventually start it up. 

```sh
docker run -dp 5000:5000 tapiatellez/distance-app-simple
```

This will create the DistanceToMKAD image and pull in the necessary dependencies.
Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply use the port 5000 but you can change this in the 
app.py file. 

## Screenshots and How to use?
The application is straight forward: Our index page contains an "Enter the Address" box where you will send and HTTP request into our distance_bp blueprint, you can enter any address you wish and press the submit button as show in the image bellow:
![Screen Shot 2021-09-09 at 16.03.18.png](https://www.dropbox.com/s/rzs9uk2zt3exday/Screen%20Shot%202021-09-09%20at%2016.03.18.png?dl=0&raw=1)
Once the submit button is pressed the app will present its results as show in the image:
![Screen Shot 2021-09-09 at 16.03.31.png](https://www.dropbox.com/s/m0p30eky3f15ltw/Screen%20Shot%202021-09-09%20at%2016.03.31.png?dl=0&raw=1)

## Contact

José Medardo Tapia Téllez
tapiatellez@gmail.com

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
