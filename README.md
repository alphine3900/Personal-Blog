# Blog

####  My personal blog web application.

## Live Site link
You can view the live application by following this [link]().

####  User view
* User can view the blog posts on the site
* User sees random quotes on the site
* User can view the most recent posts
* User can subscribe to blog mailing list and receives an email alert when a new post is made.
* User can comment on blog posts


####  Writer view
* sign in to the blog.
* create a blog from the application.
* delete comments that I find insulting or degrading
* update or delete blogs I have created.


## Author
[Alphine kirimi](https://github.alphine3900), 13/02/2022.

## Description
This is a personal blogging website where you can create and share your opinions and other users can read and comment on them. with a feature that displays random quotes to inspire your users.

## Technologies Used
* Python 3.8
* Flask 1.1.1
* PostgreSQL 11.5
* SQLAlchemy
* HTML5  
* CSS3
* Javascript
* Bootstrap 4.0
* Font Awesome 5.8.2
* jQuery 3.4.1
* Google Font API

## Requirements
* This program requires python3.+ (and pip) installed,

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/alphine3900/Personal-Blog`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        
    * On the same file write down the command **`python3 manage.py server`** 
* **Step 6** : On your terminal, run the following command, **`chmod a+x start.sh`**
    * You can now launch the application locally by running the command **`./start.sh`** 
    


## Known Bugs
* On creating a new post, a subscribed user wil receive a notification email. However, the page will display an error when redirecting the writer to the post page. This feature has been temporarily disabled due to this -- FIXED


## License
#### Copyright (c) [2021] [Alphine mutwiri kirimi]