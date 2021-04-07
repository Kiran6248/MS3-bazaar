# Bazaar
  ### *Buy what you want, Sell what you don't*.
  
### A Webpage for buying and selling of second hand goods.

[View live site here](https://ms3-bazaar.herokuapp.com/get_ads)

![image](static/images/responsive.JPG)

This webpage is developed by me for my Third Milestone Project for Code Institute.
This site is made by using **HTML**, **CSS**, **javascript**, **Python**, **MongoDB**, and **Flask Framework**. 
The purpose of this site is to show CRUD functionality and Database accessibilty.
***

## **Table of Content**

* [Overview](#overview)

* [User Experience](#user-experience)
    
    * [User Goals](#user-goals)
    * [Business Goals](#business-goals)
    * [User Stories](#user-stories)
    * [Business Stories](#business-stories)

* [Planes of Development](#planes-of-development)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
        * [Wireframe](#wireframe)
        * [Database Schema](#database-schema)
        * [Sitemap](#sitemap)
    * [Surface](#surface)
        * [Color](#color)
        * [Typography](#typography)
        * [Images](#images)

* [Features](#features)
    * [Features Used](#features-used)
    * [Features to be implementd in Future](#features-to-be-implemented-in-future)

* [Technologies used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks](#frameworks)
    * [Extensions and Kits](#extensions-and-kits) 
    * [Project Management](#project-management)
    * [Tools](#tools)

* [Resources](#resources)

* [Testing](#testing)

* [Deployment](#deployment)
    * [Prerequisites](#prerequisites)
    * [How to Clone Bazaar](#how-to-clone-bazaar)
    * [How to Deploy to Heroku](#how-to-deploy-to-heroku)

* [Credits](#credits)
    * [Code](#code)
    * [Media](#media)
    * [Acknowledgments](#acknowledgments)
***

## **Overview**

A Bazaar is a permanently enclosed marketplace or street where goods and services are exchanged or sold. The term bazaar originates from the Persian word **bazar**.

I decided to keep *Bazaar* as the name of my site because it also serve that purpose.

This website is created as a platform to meet and know about potential buyers and sellers.

This is created for educational purposes only as my Third Milestone Project for Code Institute.
This site is made by using my newly learned skill of Backend Development with the addition of Frontend Development.

[Go back to Top](#table-of-content)
***

## **User experience**

### **User Goals**

1. Somewhere to search for few things which I want to have and do not want to pay a heavy price.
2. To find someplace where I can sell some of my Favourite things, which I do not need anymore.
3. To find a buyer for my favorite things, which I can't keep anymore and don't want to throw in the garbage as well.
4. Buyers who are relocating can find things at reasonable rate for the initial setup of their home and office.
5. In the current Pandemic situation, Users may want to browse things from the safe environment of their home.
6. User-friendly website, where I don't have to be very technically educated to publish my ads.

### **Business Goals**

1. During the current world condition, when it is difficult to find Non-essential shops, this site would provide a place to buy and sell some useful items.
2. A website, where Buyer and Seller can easily contact each other if they are interested in any product posted here.
3. An easy-to-navigate site, with buttons provided for these paths through the site.
4. All the items will be categorized and will be easy to search, to save the time and energy of everyone.
5. The site owner will have full control over every post, and He/She can add or remove categories or ads.


### **User Stories**
 **Visitor Stories**
1. As a new visitor, I want to be able to easily find the product that I am looking for.
2. As a new visitor, I want to search for the product by using simple words, it should not be always the keyword.
3. As a new visitor, I want to first select the item by its appearance and price.
4. As a new visitor, I want to contact the seller if I want to buy Something.
5. As a new visitor, I want to be able to contact the admin of the page if I am not satisfied with my purchase.
6. As a new visitor, I want to register my account easily if I want to sell something.
7. As a visitor, I want to know if the product is available or not, before clicking and viewing full details.
8. As a returning visitor, I want to login easily and make some changes to my product. i.e. price.
9. As a returning visitor, I want to login easily and remove my product from the site if it is sold.
10. As a regular visitor, I want to navigate easily through the pages.
11. As a regular visitor, I want to see the details of each item.
12. As a regular visitor, I want to login from my mobile and expect the site and image to be fully responsive.
13. As a seller, I want to see all the items posted by me in one place, so that I can take decisions on that.

### **Business Stories**

  As the site owner I want/expect/need:
  1. To display the ads colorfully.
  2. To manage all the ads posted on the site and delete any appropriate one.
  3. To add more categories later if required.
  4. The Buyers/Sellers can contact me easily through a contact form or they can find me on social media accounts.

  [Go back to Top](#table-of-content)
  ***

## **Planes of Development**
### **Strategy**

The aim of making this site is to make a website that has CRUD mechanism and Database access functionality.
I decided to make a Second-Hand good buying and selling site, which will work as a platform for peoples to meet potential buyers for their things, 
as well buyers can find items at reasonable rates.

### **Scope**

I want to make a website that is accessible to everyone, People can browse items without being Registered so that there will be no hesitation in searching for anything.
People can post their items for sale using simple steps and buyers can contact sellers from the contact details provides.
It will be easier to see the details of every item as it will open on a new page. 
Users can contact the admin easily for Feedback or Complaints. Sellers can see all the ads posted by them on their profile page.

### **Structure**

This website will be a multi-page site, where pages are connected through Navigation Bar or Python. 
The navigation bar will have links for the Home page, Login, Register, and Contact form. The navigation links will change and show the logout and Post ad option Once the user is logged in.
The navigation bar will be collapsible for Mobile view and expand in a sidebar when clicked.
There will be a footer, which will show the contact details of the admin. It will be sticky and always remain at the end of the page.
2 forms will be there, one for Login and the other for Registration. 
One contact form will also be there for the users to contact the admin.
There will be pages for Posting the ads and Editing the already published ads.
Users can delete their posts if they want.
Admin will have the power to delete any post if that is unsuitable for the page.
All the data will be stored in MongoDB and Flask framework will be used to develop the site and finally, it will be deployed by using Heroku.


### **Skeleton**
#### **Wireframe**
The wireframe for this project has been made for Three screen sizes(Mobile View, Tablet View, and Laptop View). Each page is shown in all three 
screen sizes on a single page foe a better understanding of the responsiveness of the page.

The wireframes for this Project can be seen here.
[Wireframe](static/images/wireframe.pdf)

#### **Database Schema**
The Schema is pepared for the better understanding of the Database Collection.

This Project has 4 collection. Ads, Category types, Condition of goods and Users.

Database Schema can be seen here. [Schema](static/images/schema.pdf)

#### **Sitemap**
Sitemap is prepared for this site to understand the navigation of the pages.

Sitemap can be seen here. [Sitemap](static/images/sitemap.pdf)

### **Surface**
#### **Color**
The color theme is used from Materializecss.com. It is decided by keeping Hero image in consideration and mainly two colours teal(#009688 ) 
and orange(#ff9800) and their shades are used according to the page requirement.

![image](static/images/colour1.jpg)

**Core**

Two shades of Materialize Teal is used as the core element of the page, namely the Nvabar, Footer and Card color.

*  ![#009688](https://via.placeholder.com/15/009688/000000?text=+) `#009688`(teal)
*  ![#00695c](https://via.placeholder.com/15/00695c/000000?text=+) `#00695c`(teal darken-3)


**Cards and Forms**

Lighter shade of teal is used as the background colour of the form and the cards.

*  ![#00695c](https://via.placeholder.com/15/e0f2f1/000000?text=+) `#e0f2f1`(teal lighten-5)

**Buttons**

It is important for the buttons to have consistent colour with the intuitive suggestions about their functions. 
Teal is used for **Login**, **Register**, Contact form **submit**, **Post ad**, **Edit Ad**,
**Add categories**, and **Edit category**.

Orange is used for the **Delete** , modal delete confirmation, **Delete** and Contact form **Cancel** button

*  ![#009688](https://via.placeholder.com/15/009688/000000?text=+) `#009688`(teal)
*  ![#ff9800](https://via.placeholder.com/15/ff9800/000000?text=+) `#ff9800`(orange)

**Badges**

Red is used for the Sold items and Green is used for the Available items.

*  ![#f44336](https://via.placeholder.com/15/f44336/000000?text=+) `#f44336`(red)
*  ![#4CAF50](https://via.placeholder.com/15/4CAF50/000000?text=+) `#4CAF50`(green)


#### **Typography**

[Roboto Slab](https://fonts.google.com/?query=roboto+slab)

Google font **Roboto Slab** with a fallback of **sans serif** is selected for the entire project.

#### **Images**
The images used in this project are taken by the developer and are subject of demonstration only.
The Hero Image is taken from Pexel.com. It is a market image of Dubai, clicked by Sanketh Rao.

[Go back to Top](#table-of-content)
***

## **Features**

### **Features Used**

#### *Elements on every page*

**Navigation Bar**

* [MaterializeCSS](https://materializecss.com/navbar.html) is referred for making the Navigation Bar.
* Navigatin Bar is situated on the top of the page with the **Bazaar** logo on left and menu on right.
* The menu is collapsible in mobile view and opens in sidebar, in mobile view the logo is situated in the middle of the Navbar. 
* The Navbar menu have **Home**, **Login**, **Register** and **Contact Us** link for every visitor who visites the site.
* The Navbar menu will change to **Home**, **Profile**, **Post Ad**, **Logout** and **Contact us** after the visitor logged in.
* The **Manage categories** link is visible only to Admin of the site.

**Footer**

* The Footer is situated at the bottom of every page. Which is having Copyright information and My Github and Linkedin account links.
* [MaterializeCSS](https://materializecss.com/footer.html) is used to make the footer sticky at the bottom of every page, 
by adding one code in the CSS Style sheet.
* The code added to style sheet is this.

   ![image](static/images/footer.JPG)

#### *Elements on different pages*

**Home Page**

* One Hero Image is there on the Home page, which is a very colorful image of a marketplace in Dubai. It is taken from 
  [Pexel.com](https://www.pexels.com/photo/assorted-commemorative-plates-716107/)
* A welcome note is situated on the Hero Image to give the introduction about the site and its purpose.
* A search Bar is given to search for ads through their keywords.
* Ad image cards are there as 3 in a row, Which shows the image of the Ad and details about its name and availability. 
 It is responsive and changes to 2 in a row for medium size screen and 1 in a row for Small size(mobile) screen.
* The card image will open a new page when clicked on it, that page will have details for individual Ads.

**View Ad Page**

* This page opens after clicking on the Ad card on the **Home** page.
* This page has a full-size image of the Ad and Detail of it. The details shown are 
  1. Ad Title
  2. Category
  3. Ad Description
  4. Price
  5. Condition (New, Good as New or Used)
  6. Location
  7. Posted by
  8. Email
  9. Telephone
  10. Availability (Available or Sold)
* The availability is shown by a **tooltip and one **badge** also, which is *Green* in color for available ads and *Red* for sold.
* There is a **Back** button on top of the page which takes back to the **Home** page.
* One **Edit** and One **Delete** buttons are also there on the top of the page, which is visible only to the owner of the Ad(Posted by) and to the Admin of the site.

**Login Page**

* The **Login** page has a form input for **Username** and **Password**. The input section will become Red if certain input conditions are not fulfilled.
 For example- the Username and Password should be 5-15 characters alphanumeric word with no spaces.
* There is one **Login** button that directs the User to the **Profile** page after login.
* For new users, One link is given to direct them to the Register page.
* One flash message saying "Username or Password is Incorrect" will show if the Username or Password is incorrect.

**Register Page**

* The Register page will have a form to enter the Username and Password. This will also have some input conditions, same as the Login Form.
* Submit button is there, which will take the user to the Profile page with a message of "Registration Successful" and a message which tells that the user has not 
 posted anything yet.
* For returning Users, the One Login link is given below the form.

**Contact Us Page**

* One contact form is given which is visible to every user, even if the user has not registered with the site. 
* It is addressed as **Suggestions and Complaints**, So that the users will feel free to give any suggestions and complaints if they have any.
* It has a **Full name**, **Email**, and one **Feedback** section. 
* the feedback section is a Textarea.
* One **Cancel** and one **Submit** button are given. The Submit button's text will change to **Feedback Sent** after successfully sending the feedback. 
  One message will also pop up stating that **Your Feedback is submitted** or **Try Again** if it fails.
* This contact form code is referred from my second Milestone project with some changes in the email template.

**Profile Page**

* The profile page is the first page the user sees after logging in or Registering for the first time.
* This page has One Welcome note with the current user name.
* This page will show all the Ads posted by the user. If the User has not posted anything then 
  it will show a link to the Post Ad page, Where the User can post its ads.

**Post Ad Page**

* Ths Post ad is a form with many different types of inputs. The input fields are-
  1. Category (Dropdown)
  2. Photo URL ( in https form)
  3. Ad Title
  4. Ad Description (textarea)
  5. Price
  6. Condition(Dropdown)
  7. Location
  8. Telephone
  9. Email
  10. Availability(Switch)
* This form has one button to Post the Ad.
* Once the Ad is posted the user is directed to the Home Page.
* The Categories included are 
  1. Antique
  2. Art
  3. Books
  4. Electronic
  5. Fashion
  6. Games
  7. Household
  8. Jewellery
  9. Shoes
    These categories can be added or removed by the Admin.
* The Condition Field have 3 types of conditions, from which the user can select one.
  1. New
  2. Good as New
  3. Used
* The availability switch have 2 conditions **Available** and **Sold**.
* Each input section is compulsory and is validated by adding one Materialize code in Script page. This code is provided by Code Institute.

**Edit Ad Page**

* This page looks the same as the Post Ad page.
* This page is directed from the View Ad page, where a button is given to Edit the post. 
  That button is only visible to the owner of the post and Admin of the site.
* When the Ad owner clicks the edit button, all the fields populate with already filled data, which makes it easier to make the changes.
* 2 buttons are given at the bottom of the form. One to Edit the changes and One to Cancel any changes. 
* The **Edit Ad Button** will remain on the page with a flash message of " Ad Successfully Updated".
* The **Cancel button** will bring the user to the Home page.

**Delete Ad**

* The Delete Ad feature is given to every ad with a button on the view Ad page, Which is visible to only the Owner of the post and the Admin of the site.
* When the Delete button is clicked One modal pop up, with a message of **Confirm Deletion**, which has 2 buttons, 
  The **Cancel** button cancels the modal, and the user remains on the same page. The **Delete** button deletes the ad and takes the user to the **Home Page**.

**Manage Categories**

* This section is visible only to the Admin. After logging in Admin can see this link in the Navbar. 
* This page will have one **Add Category** button on the top of the page.
* All the categories are shown there with one Edit and one Delete button with every category.
* The edit button will take the admin to the Edit Category page.
* The Delete button will popup one modal with **Confirm Deletion** message.  which has 2 buttons, 
  The **Cancel** button cancels the modal and Admin remains on the same page. 
  The **Delete** button deletes the Category the Admin remains on the **Manage Category** page.

**Delete Modal**

* The Delete function of the site has given defensive programming by adding one Modal from MaterializeCSS. 
* The modal asks about the confirmation and works accordingly.
* This Modal is referred from [MaterializeCSS.com](https://materializecss.com/modals.html)

**Logout**

* The **Logout** link is given in the Navbar and visible only after the user is logged in.
* When clicking on the Logout link, The user is logged out from the session and directed back to the Login page.

**Error Handler**

* Two Error Handlers are provided for the better performance of the site if something wrong happens.
* One is a 404 error handler and another is a 500 Internal error handler.
* These pages have one image of a man looking at the 404 written and looks confused.
* The text tells them to click on the **Ads** word, which directs the user to the **Home page**.

**Secure Password**

* When registering to the site, the User's password is hashed so that it is not revealed to the database owner.


### **Features to be implemented in future**

* One wishlist will be added with every Ad posted. By clicking on that ad the User can save that ad in his/her Bucket.
* Money transactions can also be implemented in the app only.
* Direct Email facility may be added in the future, so that buyer can directly contact the seller.
* Online chat facility or message thread may be added to discuss the item with the seller.
* In the current version, the email and the telephone of the seller are visible to all, which is not a good practice in the data protection act.
 so, In the future, it would be considered to hide it and add another portal to contact the seller.

[Go back to Top](#table-of-content)

***
## **Technologies used**

### **Languages Used**

 * [HTML](https://en.wikipedia.org/wiki/HTML) is the main language used to write code for this project.
 * [CSS](https://en.wikipedia.org/wiki/CSS) is used to write code for designing and beautifying the site.
 * [JavaScript](https://en.wikipedia.org/wiki/JavaScript) is used to add functionality and make the site more interactive.
 * [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is used for the Backend Programming.
   * [jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) is used as the template engine for Python.

### **Frameworks**

  * [Flask](https://palletsprojects.com/p/flask/) is used as the main framework for the Python.
  * [jQuery](https://jquery.com/) was used for the interactive features.
  * [Materialize](https://materializecss.com/) was used to assist with the responsiveness and styling of the website, respectively the navbar, footer, cards, card-panels, buttons, modals.
### **Extensions and Kits**

  * [Werkzeug](https://palletsprojects.com/p/werkzeug/) is used as a web application library.

### **Project Management**

 * [Balsamiq](https://balsamiq.com/wireframes/) is used to make wireframes for this project in the skeleton stage.
 * [GitHub](https://github.com/) is used to make **Repositories** and for **Version Control**.
 * [GitPod](https://gitpod.io/workspaces/) is the main cloud-based editor for this project. Workspaces are made using the green Gitpod button in Github.
 * [Heroku](https://www.heroku.com/about) was used for deploying the app.
 * [MongoDB](https://www.mongodb.com/) was used for creating the database collections.

### **Tools**

 * [Am I Responsive?](http://ami.responsivedesign.is/) is used to take a mockup screenshot of the project, which is attached at the beginning of this document.
 * [Autoprefixer](https://autoprefixer.github.io/) is used to make the site compatible with all browsers.
 * [iColorpalette](https://icolorpalette.com/) is used to find a relevant color palette for the site.
 * [Favicon.io](https://favicon.io//) is used to import the icon for the website favicon.
 * [Google Fonts](https://fonts.google.com/) was used to import the 'Roboto Slab' font into the style.css file which is used on all text throughout the website.
 * [W3C Validator](https://validator.w3.org/) is used for testing HTML and CSS for the site.
 * [JSHint](https://jshint.com/) is used for testing javascript code for the site.
 * [PEP8 online](http://pep8online.com/) is used for testing Python codes.
 * [Online Spelling Check](https://www.grammarly.com/), Grammarly is used to check spelling and grammatical errors.
 * [Font Awesome](https://en.wikipedia.org/wiki/Font_Awesome) is used to import Twitter, and Linkedin font awesome icons to beautify the footer, and icons for every input field in the Ad card.
 * [Randomkeygen](https://randomkeygen.com/) is used for generating Fort Knox password.
 * [EmailJS](https://www.emailjs.com/) is used to connect the contact form to the email address.
 * [Snipping Tool](https://en.wikipedia.org/wiki/Snipping_Tool) was used to take screenshots of the images and codes.
 * [ImgBB](https://imgbb.com/) is used to store my images.

 [Go back to Top](#table-of-content)
***


## **Resources**

 * [Code Institute Course Content](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/054c3813e82e4195b5a4d8cd8a99ebaa/)- Main source of fundamental knowledge.

 * Code institute **Slack Community**- Main source of assistance.

 * Code institute **Tutor Support**.

 * [Stack Overflow](https://stackoverflow.com/)- General Resources.

 * [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)

 * [MonoDB Documentation](https://docs.mongodb.com/)

[Go back to Top](#table-of-content)
***

## **Testing**

**The detailed testing report can be found here** [Testing](TESTING.md)

[Go back to Top](#table-of-content)

***
## **Deployment**

   The Master branch of this repository is used for the whole development of the site.

### **Prerequisites**

[Python 3](https://www.python.org/downloads/) - core code

[PIP](https://pypi.org/project/pip/) - package installation

[Git](https://git-scm.com/) - version control

[Mongo DB](https://www.mongodb.com/)

* MongoDB is the database used by the app tp store content uploaded by its users.
* The following collection should be created:

    * ads

    * categories
        
    * users
   
### **How to clone Bazaar**

To clone this project from its [GitHub repository](https://github.com/Kiran6248/MS3-bazaar):

 1. From the repository, click **Code**.
 2. In the **Clone >> HTTPS** section, copy the clone URL for the repository.
 3. In your local IDE open Git Bash.
 4. Change the current working directory to the location where you want the cloned directory to be made.
 5. Type `git clone`, and then paste the URL you copied in step 2.
    
        git clone https://github.com/Kiran6248/MS3-bazaar.git
6. Press Enter, Your local clone will be created.
7. Create a file called env.py to hold your app's environment variables, which should contain the following:

        import os 

        os.environ.setdefault("IP", "0.0.0.0")
        os.environ.setdefault("PORT", "5000")
        os.environ.setdefault("SECRET_KEY", "<app secret key>")
        os.environ.setdefault("MONGO_URI", ""mongodb+srv://<username>:<password>@<cluster_name>-ofgqg.mongodb.net/<database_name>?retryWrites=true&w=majority")
        os.environ.setdefault("MONGO_DBNAME", "<database name>")

8. **Make sure thet env.py is listed in your .gitignore file to prevent your environment variable being pushed publicly**.
9. The app can be run locally using 

        python3 app.py


### **How to deploy to Heroku**

To deploy the aoo to Heroku from its [GitHub repository](https://github.com/Kiran6248/MS3-bazaar): the following steps were taken:

  1. From the GitPod terminal, create **requirements.txt** and **Procfile** using these commands:

            pip3 freeze --local > requirements.txt
            echo web:python app.py > Procfile

   2. **Push** these files to GitHub
   3. Log In to [Heroku](https://id.heroku.com/login)
   4. Select **Create new app** from the dropdown in the Heroku dashboard
   5. Choose a unique name('ms3-bazaar') for the app and the location nearest to you.
   6. Go to the **Deploy** tab and under **Deployment method** choose GitHub.
   7. In the **Connect to Github** enter your GitHub repository details and once found, click **Connect**
   8. Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars**
   9. Enter the following keys and values, which must match those in the env.py file created earlier:

   
| Key           | Value                                                                                                  |
| ------------- |:------------------------------------------------------------------------------------------------------:| 
| IP            | 0.0.0.0                                                                                                 | 
| PORT          | 5000                                                                                                    |   
| SECRET_KEY    | app secret key                                                                                        | 
| MONGO_URI     | mongodb+srv://<username>:@<cluster_name>- ofgqg.mongodb.net/<database_name>?retryWrites=true&w=majority |
| MONGO_DBNAME  | database name                                                                                         |
     

   10. Go back to the **Deploy** tab and under **Automatic deploys** choose **Enable Automatic Deploys**
   11. Under **Manual deploy**, select **master** and click **Deploy Branch**
   12. Once the app has finished building, click **Open app** from the header row of the dashboard.

 [Go back to Top](#table-of-content)
***

## **Credits**

### **Code**

* Code Institute Task Manager Project [Mini project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/054c3813e82e4195b5a4d8cd8a99ebaa/)

* For 404.html and 500.html implementation, the code was referred from the [Flask Documentation Site](https://flask.palletsprojects.com/en/master/errorhandling/)

* The Navbar, Footer, Cards, Search bar, Forms, and Modal codes were referred from [MaterializeCSS](https://materializecss.com/)

* The colour placeholder code for README.md is taken from [Stack overflow](https://stackoverflow.com/questions/11509830/how-to-add-color-to-githubs-readme-md-file)


### **Media**

* the images and Ads used in the project are my personal things and all the images are clicked by me.

* The Hero-image is taken from [Pexel.com](https://www.pexels.com/photo/assorted-commemorative-plates-716107/)

* The 404.html and 500.html image is taken from [PNGTree.com](https://pngtree.com/freepng/404-error-page_2596665.html)


### **Acknowledgments**

 * Can Sucullu (Code Institute Mentor) - for his support and invaluable suggestions.

 * Miklos (Code Institute Tutor)- For helping me in finding out the error in View Ad page.

 * My Friends and Family for helping me in User testing of the site.

 [Go back to Top](#table-of-content)

***
















