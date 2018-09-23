## Introduction
Per the directions of this activity, I have decided to make use of my creativity in completing this project. I have slightly enlarged the scope into a webapp that I will personally use. This means it will have full CRUD, GUI responsiveness, and adaptable to future features. This has enabled me to use the current app as the projects own feature request form! :)

The api has now decoupled the frontend and backend. The database has its own api which the server calls to preform database actions. Beyond the api, I have included a button to connect and disconnect with the server database. One can disconnect and have near full functionality testing the site without modifying the database.

Next steps are to containerize using Docker, host on a service, and update the final documentation.

## The current application
We have restructured the backend. We are no longer using Flask blueprints. The Single Page Application (SPA) is fully connected to the server, which routes actions to the database api. Validation checks are preformed on the client side. If successful, the action is the validated on the server side before touching the database api. This reduces server calls if data is incomplete, and rejects malformed data that is intentionally sent to corrupt the database. Error messages for each type of error from the server are logged in the console.
Also, all routes direct to the index page.

Currently missing functionality for a full feature set:
* None! Project requirements satisfied.

## Demonstration
Instructions to use are on the information page of the app.
Here are images of the working app.

![Alt text](/documentation/introduction.png?raw=true "Introduction")

![Alt text](/documentation/connected.png?raw=true "Shows 'DB connected'")

![Alt text](/documentation/disconnected.png?raw=true "Shows 'DB disconnected'")

![Alt text](/documentation/viewFeatures.png?raw=true "View Features")

![Alt text](/documentation/addFeature.png?raw=true "Add Features")

![Alt text](/documentation/updateFeature.png?raw=true "Update Feature")
