<h1> Weather Dashboard </h1> 
 
<h2>Description</h2>

A weather dashboard built with Django and Bulma that fetches live updates from the OpenWeatherMap API. Users can easily add and delete different cities' weather info.


![image](https://github.com/claireweiz/weather_dashboard/blob/main/dashboard.png)

<h2>Skills & Tools</h2>

* Python
* Django
* Bulma (CSS framework)

<h2>Setup steps</h2>

You can follow the setup tips to complete Django environment settings, and run my app in your local server.

First,copy and paste the following command in the terminal to download my code:
```
git clone https://github.com/claireweiz/weather_dashboard.git
```

Run the following command to change to the 'the_weather_env' directory:
```
~$ cd weather_dashboard/the_weather_env
```

 Now that you are in 'the_weather_env' directory, run the following commands to download the two modules below and then activate the environment:
```
~$ pipenv install django
~$ pipenv install requests
~$ pipenv shell
```
When the virtual environment has been activated, run the following commands:
```
(the_weather_env) ~$ cd the_weather
(the_weather_env) ~$ python manage.py runserver
```
Then you will see the following description in the terminal:

*Starting development server at http://127.0.0.1:8000/*

Then, open your browser, type in the URL that appears in the terminal, and you'll be able to see and test my app!


<h2>Brief Notes</h2>

The purpose of this project was to familiarize myself with Django, Bulma (a CSS framework) and how to use an API to present live data. Compared to Flask and Tkinter, I found Django to be more customizable as well as scalable.

At the start of the project, I found the web framework and the set-up quite challenging. However, I performed my own research and did lots of problem-solving to complete the project. Upon completion, I found I had a lot more confidence to tackle coding exercises that I had not encountered before.