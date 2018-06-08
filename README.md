# Website built with Django Framework

Website Developed using Django Framework. This is assignment submitted in course CS 699 Software lab.

## Overview of website developed:

- I have created website named 'StudyTonight' which is a Q&A Forum and online study material.
  - (my version of http://www.studytonight.com/)
- Once you visit homepage (http://127.0.0.1:8000/) , you will be shown the Home page.
- If Users is not log-in then page is redirected to login page.
- Users can ask questions Or answer any question.	
- I have added following users to system as a part of initial database setup script.		

| Username | Password | Permissions |
|--| -- |--|
|admin | pass12345 | admin |
|demo1 | demo12345 | normal |
|demo2 | demo12345 | normal |
|prac1 | pass12345 | normal |
|prac2 | pass | normal |
|demo3 | demo | normal |
>**Note:** there is no constraint on password.
- All normal users can be added through webpage but admin user can only be created through Database.

### Main functionality Implimented
```
  1] Login, Register User Interface - Any user can register and login into website
		Functions Implemented :
		i) 	Login
		ii)	Logout
		iii)	Register
	
	2] Q&A Forum - Registered User can see the Forum
		Functions Implemented :
		i)	List of questions Posted: (sorted by newest question posted first)
				Details Shown to user:
					- question title
					- question uploaded/ asked date with time
					- user name who asked the question
					- number of views : number of times user checks/sees the details of the question
					- topic name related to question
					- number of Answers given to the question
					And
					- link to ask the question

		ii)	Question Details (if user click on question title then question details are shown)
				It displayes:
					- question title
					- question uploaded/ asked date with time
					- user name who asked the question
					- number of views : number of times user checks/sees the details of the question
					- topic name related to question
					- Answers given to the question:
						It contains:						
						- user name who answered the question
						- answer written by that user
						- date with time at which answer were uploaded
					And
					- link to answer the question 
		iii)	Add Question OR Answer : user can asked questions and also can answer the questions.
		
	3] Tutorials 
		- List of Tutorials : User can only see the list of tutorials/courses available.
				* this is static ie passive functionality as data is not coming from DB
				* Users can only view the courses. 
```

- Once users successfully logs into system, page will show website's home page.
- All pages after successfully login consist of top navigation bar with oprions:
  1. ***StudyTonight*** - go to Home page.
  2. ***Tutorials*** - display the Tutorials available to user.
  3. ***Q&A Forum*** - display the Questions which were asked previously.
      - You can explore a question further by clinking on question title. It will also show the detailed question and answers posted by user.
  4. ***Logout*** - expire your session.
 


