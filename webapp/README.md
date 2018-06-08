# Directory Structure:

```
* webapp  -> Projects parent directory

	- accounts -> accounts app for user interface
			
      - migrations	-> Database migrations
			- static	-> CSS Stylesheets (style.css). Websites design stylesheet.

				- accounts -> same name as app
					- images -> images used in the app(like background images)
					- style.css -> Websites design stylesheet.	
	
			- templates	-> All HTML templates for user interface app(i.e. login, registration, logout pages).

				- accounts -> same name as app(inside this directory we include all html files for app)
					-base.html  
					-login.html
					-logout.html
					-register.html	
			
		- forum	-> main website's parent directory / app

			- migrations	-> Database migrations
			- static	-> CSS Stylesheets (style.css). Websites design stylesheet.

				- forum -> same name as app
					- images -> images used in the app(like background images)
					- style.css -> Websites design stylesheet.	
	
			- templates	-> All HTML templates for user interface app(i.e. tutorials, Q&A Forum, Questions details).

				- accounts -> same name as app(inside this directory we include all html files for app)
					-answer_form.html  
					-form-template.html
					-home.html      
					-question.html
					-base.html
					-forum.html
					-question_form.html
					-tutorial.html
	
		- webapp -> Project configuration directory

		- db.sqlite3 -> Built-in database
```
>**Note:** All website code and scripts are present within webapp folder which has been submitted as a part of assignment.
