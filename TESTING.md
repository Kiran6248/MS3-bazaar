#  Testing page for Bazaar
  ### *Buy what you want , Sell what you don't**.

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













