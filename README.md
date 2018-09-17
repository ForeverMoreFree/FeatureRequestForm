## Introduction

This form allows an already logged in employee to add a feature request.

I have created a full-stack Flask application first. As that was a quick setup for a full one stop shop. (Front-end, backend, database) I will continue on with Knockout to decouple the frontend/backend, then containerize using Docker, then host on a service.

## The current application
We have a webapp that is using a Flask backend. Our database uses sqlite3 and connects with python using SQLAlchemy. The webpages are served using blueprints with Flask and the form templates use wtforms. The webpages use jinja to show the forms and data.

The ability for viewing, deleting, and updating was not explicitly stated, I feel it was implied. Because the goal is to see how I fill ambiguities in my own creative way, I'd like to implement the full CRUD. While I am developing this program, I am using the program. I am using it as a my own feature request form. Because I am a user, I more easily  pinpoint pain points.

Currently missing functionality for a full feature set:
* update_page
* reordering priorities

Updates to come are listed in the "view_features" picture below.

## Demonstration
Instructions to use are on the index page of the app.
Here are images of the working app.

![Alt text](doumentation/index.png?raw=true "index.html")

![Alt text](doumentation/view_feature.png?raw=true "view_feature.html")

![Alt text](doumentation/add_feature.png?raw=true "add_feature.html")
