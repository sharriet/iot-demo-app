# IoT Demo App

## Overview

This application allows you to control an LED through a Flask app using a Raspberry Pi. It was developed to introduce sixth-form students to IoT. It is therefore simple enough for any student to operate, without prior knowledge of Python.

The repository includes a workbook in pdf format which teaches students how to build the LED circuit and run the application. The tasks in the workbook take around an hour to complete. For best results a minimal amount of HTML/CSS is desirable, but not essential.

## Running the app

To run this app,

		source bin/activate
		pip install -r requirements.txt
		cd app
		export FLASK_APP=routes.py
		flask run

