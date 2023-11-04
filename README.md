<h1> Weather Dashboard </h1> 
 
<h2>Description</h2>

A weather dashboard using Django as the GUI that fetches live updates from the OpenWeatherMap API. Users can easily add and delete different cities' weather info.


![image](https://github.com/claireweiz/weather_dashboard/blob/main/dashboard.png)

<h2>Skills & Tools</h2>

* Python
* Django

<h2>Set-up steps</h2>

Write the following command lines in the terminal:
```
git clong https://github.com/claireweiz/weather_dashboard.git
```

Under 'the_weather_env' repository, run:
```
pipenv install django
pipenv install requests
pipenv shell
```
When the virtual environment is activated, run:
```
(the_weather_env) cd the_weather
(the_weather_env) python manage.py runserver
```
Then you will see this:

*Starting development server at http://127.0.0.1:8000/*

Open the browser and visit the URL.


<h2>Brief Notes</h2>

The purpose of this project was to familiarize myself with Django, Bulma (a CSS framework) and how to use an API to present live data. Compared to Flask and Tkinter, I found Django to be more customizable as well as scalable.

At the start of the project, I found the web framework and the set-up quite challenging. However, I performed my own research and did lots of problem-solving to complete the project. Upon completion, I found I had a lot more confidence to tackle coding exercises that I had not encountered before.