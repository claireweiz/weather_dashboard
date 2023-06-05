<h1> Weather Dashboard </h1> 
 
<h2>Description</h2>

A weather dashboard, fetching live updates from API (OpenWeatherMap), and using Django as GUI. The platform and add and delete different cities' weather info freely.


![image](https://github.com/claireweiz/weather_dashboard/blob/main/dashboard.png)

<h2>Skills & Tools</h2>

* python
* Django

<h2>Set-up steps</h2>

Write command lines in ternimal:
```
git clong https://github.com/claireweiz/weather_dashboard.git
```

Under 'weather_dashboard' respository, run:
```
pipenv install django
pipenv install requests
pipenv shell
```
While virtual environment is activated, run:
```
(weather_dashboard) cd the_weather
(weather_dashboard) python manage.py runserver
```
Then you will see this:
*Starting development server at http://127.0.0.1:8000/*
Open the browser and visit the URL.


<h2>Thoughts</h2>

First time I try Django as interface to run python and present live data from API, and CSS framework Bulma. Compare to Flask and Tkinter, Django is more helpful in terms of customization and quite esay to learn as well.