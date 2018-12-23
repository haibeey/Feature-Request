Flask web project that implement the feature request web app for BriteCore.

deployment
    The url to the site is http://abjoe.pythonanywhere.com/

    I have opt in to deploy on pythonanywhere.com because it is free.

    The deployment is straigth forward. After uploading files from my 
    localhost all i did next was edit the wsgi file to point my 
    app to pythonanywhere server

    The edited file looks something like this:
                import sys
                project_home = u'project path'
                if project_home not in sys.path:
                    sys.path = [project_home] + sys.path

                from app import app as application 


    After the that all i needed to do is to start the application by going 
    to the web dashboard and clicking on reload app and boom the site was live.

