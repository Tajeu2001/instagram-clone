# Insta-Clone

An instagram clone that has similar functionalities with instagram.The users get to create profiles of their own to be able to upload images with captions on them.They can also view images uploaded by other users.Apart from viewing they can also comment and like the photos.

## Prerequisites

* Text Editor
* Python3
* Git

## Getting Started

* Install git in your computer.
* Open termimal.
* Clone the repository using the command $git clone.
* You will now have the repository in your local folder.


### Setup and Installation  
To get the project .......    
##### Cloning the repository:  
 ```bash 
git clone https://github.com/Tajeu2001/instagram-clone.git
```
##### Navigate into the folder 
 ```bash 
cd instagram-clone
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
pip install -r requirements.txt 
```  
##### Setup Database  
SetUp your database User,Password, Host then make migrations
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
python3.8 manage.py migrate 
```
##### Run the application  
 ```bash 
python3.8 manage.py runserver 
```  
##### Testing the application  
 ```bash 
python3.8 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

### View of the application homepage

![alt text](https://github.com/Tajeu2001/instagram-clone/blob/master/static/images/home.png)

### View of the search_results page


![alt text](https://github.com/Tajeu2001/instagram-clone/blob/master/static/images/profile.png)

## User Story

* Users get to sign up and login
* Update their profile
* Post their own photos
* View photos uploaded by other users
* Comment on photos
* Like photos


## Deployment

Deploy the project to heroku.

## Built With

* Django2.2
* Python3.8
* Bootstrap
* Javascript

## Live link



## Author

* Rosemary Siantayo Tajeu

## Contact details
Email: tajeusanta7@gmail.com

### License
This is under the [MIT](LICENSE) license 