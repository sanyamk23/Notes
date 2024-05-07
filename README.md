 # Notes App

 This is a Notes Project in which the frontend is of React.Js and for backend we are using Django Framework.
 The React app is within the Django project.

 Firstly, we start the project by simply creating a Django project named 'mynotes' with an app named 'api' in it.
 The 'mynotes' base project contains the base installations in it.
 We neend to install djangorestframework and django-cors-headers as DRF provides the functionality to create RESTful APIs and cors header is used to let the react app fetch the data from the django project as React is working on the port 3000 and Django is working on port 8000.
 So this is cross origin resource, so to integrate both together we need corsheaders.

 In settings.py of base project of Django, in installed apps we add 'api', 'djangorestframework' and 'corsheaders'. We also need to includes corsheaders middleware named 'corsheaders.middleware.CorsMiddleware' that acts as a middleware between Django and React.
 We allow CORS to fetch data from all the Django origins by writing 'CORS_ALLOW_ALL_ORIGINS = True'

 In 'api' app, we define the basic routes and functionalites of the API and how the GET POST and PUT method would work.
 We define the notes model in models.py file.
 Urls are configured in the urls.py file.
 Note model is serialized in serializers.py file.
 All the functions of the notes like create note, delete note and update note are defined in utils.py file.
 Function based views are used to defining the views in views.py file.

 The react app is created by command 'npx create-react-app frontend' and a react app is created in the root directory of the project.
 In 'src' directory of React app, we create a frontend for our project.

 For integrating React app in Django project, we run the command 'npm run build' in the frontend directory of the project.
 This creates and build of the react app, which contains the index.html file of the react app and this file ill help us to directly access the react app.

 Now our build is created, so we will import these files to our Django project.
 In settings.py of base project, we would create a custom template of the index.html file of the React build by including the path of the build directory in the 'DIRS' key of the TEMPLATES.
 We would also include the  static files of the build in our settings.py by writing 'STATICFILES_DIRS = [
    BASE_DIR / 'frontend/build/static'
]' so that the static files are included in our Django project.
In urls.py file of the base project, we would include the base path of our project to index.html file of the React build by writing "path('', TemplateView.as_view(template_name='index.html')),".We use TemplateView as index.html is in the template of our Django project.


NoteList page - 
![Screenshot (122)](https://github.com/sanyamk23/Notes/assets/124618873/9b56dfae-27af-45e8-8926-8699d37531e2)

Note page by id - 
![Screenshot (123)](https://github.com/sanyamk23/Notes/assets/124618873/48aa1aea-e70e-4b7b-8229-4c6f92343711)
