## Introduction
Per the directions of this activity, I have decided to make use of my creativity in completing this project. I have slightly enlarged the scope into a webapp that I will personally use. This means it will have full CRUD, GUI responsiveness, and adaptable to future features. This has enabled me to use the current app as the projects own feature request form! :)

Already completed is a full-stack Flask application. I have now created an independent single page application (SPA) using KnockoutJS (KO). I have prepared the SPA for an api that I have created. Next steps are to complete the api integrations, containerize using Docker, host on a service, and update the final documentation.

## The current application
The full-stack webapp remains unchanged in this commit. I have created an html/css/js SPA that focuses heavily on KO. KO bindings allow for real-time updates on the page. The navbar now uses these bindings, changing templates and section visibility as needed. I mocked some JSON response data. The webapp contains a full client-side CRUD working in-memory with real-time updates using the mocked response data. The forms also contain client-side validation. Server-side validation will also be implemented. Feature priority numbers can skip, this is intended as a feature.

Currently missing functionality for a full feature set:
* reordering priorities
* api connection

Updates to come are listed in the "View Features" picture below.

## Demonstration
Instructions to use are on the information page of the app.
Here are images of the working app.

![Alt text](/documentation/introduction.png?raw=true "Introduction")

![Alt text](/documentation/viewFeatures.png?raw=true "View Features")

![Alt text](/documentation/addFeature.png?raw=true "Add Features")

![Alt text](/documentation/updateFeature.png?raw=true "Update Feature")
