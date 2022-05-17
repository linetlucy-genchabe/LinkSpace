# LinkSpace

## Description

Basic flask application starter files

## Author

[](https://github.com/linetlucy-genchabe/)

```
Landing Page
```
<img src="./app/static/home.png">

### Running the Application

1. Pre-requisites

   - Ensure to activate virtual environment called virtual,using:

     - source virtual/bin/activate

   - Install flask and pip
   - Install flask_script

2. Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app ('development')
3. Add the export configurations in a start.sh

   - export SECRET_KEY= "Your secret key"
   - export API_KEY= "Your Api key"

4. Run using the executable file ,with command :
   - ./start.sh

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all blogs, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with blogs that have been posted by writes and be able to subscribe to the blog|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|
|Subscription | **Email Address**| Flash message "Succesfully subsbribed to KalebsBlog"|

## Contact Information

For any further inquiries or contributions or comments, reach me at 
### License

[MIT License](https://github.com/MugeraH/flask_code/blob/main/license)

Copyright (c) 2021
