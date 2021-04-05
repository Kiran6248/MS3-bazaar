#  Testing page for Bazaar
  ### *Buy what you want , Sell what you don't*.

### A Webpage for buying and selling of second hand goods.

[Main README.md file](README.md)

[View live site here]()

## Testing

* [Code Testing](#code-testing)
    * [Markup](#markup)
    * [CSS](#css)
    * [Javascript](#javascript)
    * [Python](#python)

* [Client Stories Testing](#client-stories-testing)

* [Manual Testing](#manual-testing)
    
    * [Home Page](#home-page)
    * [View Ad Page](#view-ad-page)
    * [Post Ad Page](#post-ad-page)
    * [Edit Page](#edit-page)
    * [Delete Modal](#delete-modal)
    * [Profile Page](#profile-page)
    * [Manage Catagory Page](#manage-catagory-page)
    * [Contact Us Page](#contact-us-page)
    * [Login Page](#login-page)
    * [Register Page](#register-page)

* [Responsiveness](#responsiveness)

* [Browser Compatibility](#browser-compatibility)

* [Lighthouse](#lighthouse)

* [Project Barrier](#project-barrier)

* [Bug Report](#bug-report)
    * [Bug Found and Resolved](#bug-found-and-resolved)
    * [Open Bug](#open-bug)
***

## **Code Testing**
  [W3C Markup Validation Service](https://validator.w3.org/)

### **Markup**
 [W3C Markup Validation Service](https://validator.w3.org/)

  * W3C markup validation service is used for the testing of the **HTML** of all  HTML pages and 

    The results can be seen here.

### **CSS**
[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

* W3 CSS validation service is used for the testing of the **CSS** of the project and .

    The result can be seen here.

* [style.css]()

### **Javascript**
[JSHint](https://jshint.com/)

* JSHint, a JavaScript code quality tool was used to test the **JavaScript** codes of all 3 js pages from the project.

    The result can be seen here.

* []() 

### **Python**
[Python Validator](http://pep8online.com/)

***
## **Client Stories Testing**

Testing client stories from UX part of [README.md](README.md) 
 
1. As a new visitor, I want to be able to easily find the product that I am looking for.
    * This website has agiven a search functionality, which searches ads based on the words from ad title and ad description.
    * The search bar is situated in the Home page, below the Hero image. So, it is very easy to find out.

2. As a new visitor, I want to search the product by using simple words, it should not be always the keyword.
    * The keyword to function the search engine is any word from the ad title and ad description. So it can be just games, books, new anything.

3. As a new visitor, I want to first select the item by its appearance and price.
    * The Home page have card displayed, but they dont show full details of that particular card.
    * The Ad card show only Image, Price, Category and Status about its availability.
    * When someone likes anything and it is showing available then He/She can click the card, which takes them to a new page with description.
    * this kind of display saves time and users can decide easily.

4. As a new visitor, I want to contact the seller if I want to buy Something.
    * The selller's email id and Telephone number are given in the detailed Ad card page. 
    * The buyer can contact easily with the seller if the thing is available.
    
5. As a new visitor, I want to be able to contact the admin of the page if I am not satisfied with my purchase.
    * A contact Form is given with the site, the link of which can be found in the Navbar.
    * This contact form has title Suggestions and Complaints, so that user can give anyting in feedback.
    * The admin's contact details (Github and Linkedin) are given in the Footer also.

6. As a new visitor, I want to register my account easily if I want to sell something.
    * The link to Registration form is given in the Navbar, which is visible to anyone who is visiting the site.
    * The Registration form clearly states the conditions to Register as, Username and Password must be 5-15 characters long, with only numbers and letters.
    
7. As a visitor, I want to know if the product is available or not, before clicking and viewing full details.
    * A Red badge for Sold and a Green badge for Available items is given with every Ad card.
    * The badge is visible on the Home page only, which is helpful for the visitor to decide.
    * One tooltip is also given with the badge which shows the availability(Available or Sold) when the user hover over it.

8. As a returning visitor, I want to login easily and make some changes in my product. i.e. price.
    * The login form is given in the Navbar, so it is easy to find. 
    * After Logging in the user is directed to the Profile Page which shows all the ads posted by the user.
    * When the user clicks on the particular card, it opens in full view and Edit button is also visible on the top of the page.
    * After clicking the edit button , the user is directed to the edit Ad page , where user can make any changes easily.

9. As a returning visitor, I want to login easily and remove my product from the site if it is sold.
    * After logging in and opening the ad in full view, The user can see a delete button on top of the view ad page.
    * When the user clicks delete button, one Modal pops up asking for Deletion Confirmation.
    * After selecting delete button from modal, the user can delete the Ad card.

10. As a regular visitor, I want to navigate easily through the pages.
    * A Navbar is situated on top of the every page, which always shows the links to Home, Login, Register and Contact Us form.
    * After logging in the user can see Profile, Post Ad page and Logout Link.

11. As a regular visitor, I want to see details of each item clearly.
    * All the items open in a new page, after clicking on it.
    * Each item has Title, Description, Category, Price, Condition, Location, Posted By, Email, Telephone, and Availability.

12. As a regular visitor, I want to login from my mobile and expect the site and image to be fully responsive.
    * The site is fully rsponsive in mobile and can be easily navigated through the Navbar
    * The Navbar in mobile view is collapsible and opens in side bar.

13. As a seller, I want to see all the items posted by me in one place, so that I can take decisions on that.
    * There is a Profile page which shows all the Ads posted by the user.
    * The profile page opens after the user is logged in.

[Go to Top](#testing)
***
## **Manual Testing**

**Manual Testing of all elements and functionality of every page.**

#### **Home Page**
#### **View Ad Page**
#### **Post Ad Page**
#### **Edit Page**
#### **Delete Modal**
#### **Profile Page**
#### **Manage Catagory Page**
#### **Contact Us Page**
#### **Login Page**
#### **Register Page**
***

## **Responsiveness**

***

## **Browser Compatibility**

***
## **Lighthouse**

***

## **Project Barrier**

***
## **Bug Report**
#### **Bug Found and Resolved**

1. The Hero image is added through the style sheet because when I was trying to add it through materialize img tag, 
   the page was becoming very difficult to resize. As **img** tag is not there in HTML, I didn't add **alt**, instead I added **title** in the containing **div** after referring 
   from Stack Overflow.

   The Stack Overflow source can be verified here.[Stack Overflow](https://stackoverflow.com/questions/4216035/css-background-image-alt-attribute)

2. The cards added in the home page were not fixed in size, they were becoming big and small depending on the size of uploaded image. 
   To fix this problem I searched in stack oveflow and found one code to be added in the style sheet make the size equal for all image uploads. 
   the code used to fix this issue is this.

   ![image](static/docs/css.JPG)

3. To show the Ad cards in full view in a single page, I needed one ad id. The ad id was generated in edit function in the mini project. 
   I was following Mini project to understand basic functionality. So i had to make one temporary code to show the card on a single page. 
   Then I was able to make edit and delete buttons and added functionality through app.py 
   the temporary code is this ![image](static/docs/code1.JPG)
   
   After getting the ad id, I changed the code which was targeting the particular card id.
   that code is this
   
   ![image](static/docs/code2.JPG)
   
   
   I changed the code in app.py but did a spelling mistake in button where that id is required. I was not sure what I was doing wrong.
   as this error was showing
   
    ![image](static/docs/jinja-new.png)
   
   After many hours of trying I contacted Tutor support.
   The tutor said to check the url where this id is used , i saw and corrected the mistake. Card was starting to show but 12 times.

   ![image](static/docs/multipleimage-new.png)

   I added one for loop in the single page view, for the temporary code. After commenting out the for loop also, It was not getting fixed.

   ![image](static/docs/for.png)

   so, The Tutor suggested that sometimes jinja behaves odd and run commented out code also. So, he advised me to remove the for loop completely and try.
   I did that and it was a success.

4. The edit function was not showing the current values of the card. I checked the button links, it was all right.
   Then I checked the edit template multiple times and matched it with the mini project.
   It was all right.
   When I checking the app.route for the edit function there was a spelling mistake. 
   after correcting the mistake, the edit function started working as expected.

5. The delete modal was not popping up when delete button was clicked.
   I checked the button links, app.py code. When I was checking the modal code, i found that there was a space missing in jinja.
   After correcting the mistake the function started working as expected.


#### **Open Bug**













