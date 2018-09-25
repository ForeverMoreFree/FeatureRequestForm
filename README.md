## Introduction
The activity suggests using creativity to complete this project. I have decided to do just that. I have slightly enlarged the scope of the project to include CRUD functionality and a server connect/disconnect button. It is also highly adaptable for new features. This has enabled me to use the current app as the project's own feature request form! :)

The program may be built into a Docker image if desired. An image is also on Dockerhub located at https://hub.docker.com/r/forevermorefree/featurerequest/

Here is what is used in the app: (Included with Docker image)
* KnockoutJS front end
* Flask backend
* HTTP RESTful API using JSON messages
* Mysqlite3 database
* SQLAlchemy
* nginx to serve static content
* Gunicorn WSGI to bridge nginx and Flask
* Supervisor to oversee Gunicorn on local unix


## Instructions to run app
```shell
Start Docker engine
$ docker run -d -p 5000:80 forevermorefree/featurerequest:1
Browse to http://192.168.99.100:5000
```



## App demonstration
Instructions to use are on the information page of the app.
Here are images of the working app.

![Alt text](/documentation/introduction.png?raw=true "Introduction")

![Alt text](/documentation/connected.png?raw=true "Shows 'DB connected'")

![Alt text](/documentation/disconnected.png?raw=true "Shows 'DB disconnected'")

![Alt text](/documentation/viewFeatures.png?raw=true "View Features")

![Alt text](/documentation/addFeature.png?raw=true "Add Features")

![Alt text](/documentation/updateFeature.png?raw=true "Update Feature")
