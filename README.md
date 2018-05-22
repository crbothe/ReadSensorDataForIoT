# ReadSensorDataForIoT
This repo demonstrates implementation of Django server for reading data from the sensor continuously (with Python support) and pushing them to the webpage

# How to use this repo

Django provides a great framework and its own project creation and app generation.

Saying that, means you can not use these files and just run this code.

Basically, you have to create your project with [Django](https://www.djangoproject.com/). 

You can follow simple guidelines given here: [Start your first project and app with Django](https://docs.djangoproject.com/en/1.9/intro/tutorial01/)

I have provided the Django version 1.9 link here, because this project was tested with the same. However, you can try using recent version as well.

The main project starts under "DAWebServer" folder.

## Step one
Create project using:
```sh
django-admin startproject DAWebServer
```
Start your app using:
```
python manage.py daweb
```
and add the link in "DAWebServer/setting.py", here "daweb" is the app
```py
INSTALLED_APPS = [
    'daweb',
    'django.contrib.admin',
    'django.contrib.auth',
    .
    ]
```

Edit other files according to following steps.

## Step two
Create the "index" as general step in Django to host the "home.html".
Also, create the functions for reading your sensor data in "daweb/views.py"
```py
def get_sense1(request):
    results =  round(random.random(), 3) # Your Python function for reading sensor 1 values
    print(results)
    return HttpResponse(results)
```

## Step three
Refer the created functions in "DAWebServer/urls.py"
```py
 url(r'^get_sense1/$', 'daweb.views.get_sense1', name='get_sense1'),
```

## Step four
Read and push the data to the webpage through "daweb/templates/home.html"
```html
	<!-- READING SENSOR "1" VALUES -->
		<div  style="width:100%" align="middle">
			<div><b>The sensor 1 value:</b></div>
			<div id="sensor1"></div>
			<script>
			$(document).ready(function() {
			  $.ajaxSetup({ cache: false });
			  var my_refresh = setInterval(function() {
				$('#sensor1').load('/get_sense1/');
			  }, 1000); // "1000ms"
			});
			</script>
	</div>
```
This code is quite self-explainatory. It uses ajax js funciton from jquery which loaded through:	
```html
<script src="http://code.jquery.com/jquery-latest.min.js"></script>
```
keeps updating only the field of interest every one second (1000ms), here it is "sensor1".

## Step five
Run the server using:
```sh
python manage.py runserver 0:8080
```

This allows you to access the webpage within the network at:
```sh
http://0.0.0.0:8080/
```
Enjoy streaming your sensor data on webpage.
