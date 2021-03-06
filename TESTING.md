#  Testing page for Bazaar
  ### *Buy what you want , Sell what you don't*.

### A Webpage for buying and selling of second hand goods.

[Main README.md file](README.md)

[View live site here](https://ms3-bazaar.herokuapp.com/get_ads)

## Testing

* [Code Testing](#code-testing)
    * [Markup](#markup)
    * [CSS](#css)
    * [Javascript](#javascript)
    * [Python](#python)

* [Client Stories Testing](#client-stories-testing)

* [Manual Testing](#manual-testing)

    * [Elements on every page](#elements-on-every-page)
       * [Navigation Bar](#navigation-bar)
       * [Footer](#footer)
       * [Flashed messages](#flashed-messages)
    * [Elements on separate page](#elements-on-separate-page)
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
       * [Error Handler](#error-handler)

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

    The initial result was this.

    ![image](static/docs/htmlvalidation.JPG)

  So, the Type is removed from script tag, Aria-label is removed from search a tag, and section is removed. The final result is this

![image](static/docs/html.JPG)

### **CSS**
[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

* W3 CSS validation service is used for the testing of the **CSS** of the project and .

    The result can be seen here.

* style.css
    <p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
        


### **Javascript**
[JSHint](https://jshint.com/)

* JSHint, a JavaScript code quality tool was used to test the **JavaScript** codes of all 2 js pages from the project.

    The result can be seen here.

* ![script.js](static/docs/script.JPG) 
 
  This is warning fron using jQuery $ sign and can be ignored.

### **Python**
[Python Validator](http://pep8online.com/)

 The result can be seen here.

 ![python](static/docs/python.JPG)

***
## **Client Stories Testing**

Testing client stories from UX part of [README.md](README.md) 
 
1. As a new visitor, I want to be able to easily find the product that I am looking for.
    * This website has given a search functionality, which searches ads based on the words from ad title and ad description.
    * The search bar is situated on the Home page, below the Hero image. So, it is very easy to find out.

2. As a new visitor, I want to search for the product by using simple words, it should not be always the keyword.
    * The keyword to function in the search engine is any word from the ad title and ad description. So it can be just games, books, new anything.

3. As a new visitor, I want to first select the item by its appearance and price.
    * The Home page has card displayed, but they don't show the full details of that particular card.
    * The Ad card show only Image, Price, Category, and Status about its availability.
    * When someone likes anything and it is showing available then He/She can click the card, which takes them to a new page with a description.
    * this kind of display saves time and users can decide easily.

4. As a new visitor, I want to contact the seller if I want to buy Something.
    * The seller's email id and Telephone number are given on the detailed Ad card page. 
    * The buyer can contact easily the seller if the thing is available.
    
5. As a new visitor, I want to be able to contact the admin of the page if I am not satisfied with my purchase.
    * A contact form is given with the site, the link of which can be found in the Navbar.
    * This contact form has the title Suggestions and Complaints so that users can give anything in feedback.
    * The admin's contact details (Github and Linkedin) are given in the Footer also.

6. As a new visitor, I want to register my account easily if I want to sell something.
    * The link to the Registration form is given in the Navbar, which is visible to anyone who is visiting the site.
    * The Registration form clearly states the conditions to Register as, Username and Password must be 5-15 characters long, with only numbers and letters.
    
7. As a visitor, I want to know if the product is available or not, before clicking and viewing full details.
    * A Red badge for Sold and a Green badge for Available items are given with every Ad card.
    * The badge is visible on the Home page only, which is helpful for the visitor to decide.
    * One tooltip is also given with the badge which shows the availability(Available or Sold) when the user hovers over it.

8. As a returning visitor, I want to login easily and make some changes to my product. i.e. price.
    * The login form is given in the Navbar, so it is easy to find. 
    * After Logging in the user is directed to the Profile Page which shows all the ads posted by the user.
    * When the user clicks on the particular card, it opens in full view and the Edit button is also visible on the top of the page.
    * After clicking the edit button, the user is directed to the edit Ad page, where the user can make any changes easily.

9. As a returning visitor, I want to login easily and remove my product from the site if it is sold.
    * After logging in and opening the ad in full view, The user can see a delete button on top of the view ad page.
    * When the user clicks the delete button, one Modal pops up asking for Deletion Confirmation.
    * After selecting the delete button from the modal, the user can delete the Ad card.

10. As a regular visitor, I want to navigate easily through the pages.
    * A Navbar is situated on top of every page, which always shows the links to the Home, Login, Register, and Contact Us form.
    * After logging in the user can see Profile, Post Ad page, and Logout Link.

11. As a regular visitor, I want to see the details of each item.
    * All the items open on a new page, after clicking on it.
    * Each item has Title, Description, Category, Price, Condition, Location, Posted By, Email, Telephone, and Availability.

12. As a regular visitor, I want to login from my mobile and expect the site and image to be fully responsive.
    * The site is fully responsive in mobile and can be easily navigated through the Navbar
    * The Navbar in mobile view is collapsible and opens in the sidebar.

13. As a seller, I want to see all the items posted by me in one place, so that I can take decisions on that.
    * There is a Profile page that shows all the Ads posted by the user.
    * The profile page opens after the user is logged in.

[Go to Top](#testing)
***
## **Manual Testing**

**Manual Testing of all elements and functionality of every page.**

### **Elements on every page**
#### **Navigation Bar**

1. Check if the **navigation bar** has a Brand Name and Menu.
2. Click the Brand name, check if the **Home** page opens.
3. Click the **Home** link, check if the page stays on the home page.
4. Click the **Login** link, check if the Login page opens.
5. Click the **Register** link, check if the Register page opens.
6. Click the **Contact us** link, check if the Contact Us page opens.
7. Log in to the site, Check If **Profile**, **Post Ad**, and **Logout** link are visible.
8. Click the **Profile** link, check if the Profile page opens.
9. Click the **Post Ad** link, check if the Post Ad page opens.
10. Click the **Logout** link, check if the user logs out, and Log in page opens.
11. Log in from the Admin's account, Check if the **Manage Categories** link is visible.
12. Click the **Manage categories** link, check if the Manage Categories page opens.
13. Check for **Responsiveness** in mobile view, the navigation bar collapsed in the hamburger icon.
14. Check in the mobile view if the menu is opening in the sidebar. 
15. Repeat steps from 2 to 12 in mobile view.

#### **Footer**

1. Check the **Footer** is always fixed at the bottom of the page.
2. Click the **Github** link, check if it opens my Github page on a different page.
3. Click the **Linkedin** link, check if it opens the Linkedin login page.
4. Check the copyright date.
5. Go to the mobile view and check for **responsiveness**.
6. Repeat steps 1 to 4 in the mobile view.

#### **Flashed Messages**

1. Register with a new account and check if the flash message **"Registration Successful"** appears.
2. Log in to the site and check if the flash message **"username's profile"** appears.
3. Log in with an incorrect account and check if the flash message **"Incorrect Username or Password"** appears.
4. Logout from the session and check if the flash message **"You have been Logged Out"** appears.
5. Post some Ads and check the flash message **"Ad successfully posted"** appears.
6. Edit some posts and check for the flash message **"Ad Successfully Updated"** appearance.
7. delete some posts and check if the flash message **"Ad successfully deleted"**  appears.
8. log in from Admin account and add some category, check if the flash message **" New category Added"** appears.
9. Edit some categories and check if the flash message **"Category successfully updated"** appears.
10. Delete some categories and check if the Flash message **"Category successfully deleted"** appears.
11. Send some feedback through the Contact form and see if the flash message **"Your message has been sent"** appears.

### **Elements on separate pages**

### **Home Page**
#### **Hero Image**

 1. Check the Hero image is also loading fine and is always on top of the Home page.
 2. Check for **Responsiveness** on different screen sizes.

#### **Welcome Note**

  1. Check that the welcome note is always on the Hero Image.
  2. Check for the fonts, and is readable with the dark background.
  3. Check for the Grammatical mistakes if any, in the text written.
  4. Check for **Responsiveness** on different screen sizes.

#### **Search Bar**

 1. Check the search bar is loading correctly on the Home page.
 2. Type any random word and click the teal-colored search button, the result is showing below the search bar.
 3. Type any word which has very rare chances of being on the ad page. like- "airplane", then "No Result Found" should flash below the search bar.
 4. Click the orange refresh button and the page should be refreshed and all the ads should appear.
 5. Go to mobile view and repeat steps 1 to 4.

#### **Ad Cards**

 1. Check for the positioning of the Ad cards, it is well-aligned.
 2. Check for the image sizing of the cards, all images are equal in size.
 3. Check for the description below the image, it is informative enough to know about the thing.
 4. Click on the card, it opens on a new page.
 5. Go to the mobile view and repeat steps 1 to 4.


### **View Ad Page**

#### **Back Button**

 1. Check the back button, it is always on the top left of the page.
 2. Click the button, It is taking the user to the Home page.
 3. Repeat the steps in mobile view.

#### **Edit Button**

 1. Log in with a username, who has posted anything, or with an admin profile.
 2. Check the Edit button is showing on the top of the View Ad page.
 3. Click the Edit Button, It opens the Edit Ad page.
 4. Go to the Mobile view, the button is visible there and working fine.

#### **Delete Button**

 1. Log in with a username, who has posted anything, or with an admin profile.
 2. The delete button should be there on top of the page.
 3. Click the Delete button, The Delete Modal pos up with Cancel and Delete buttons.
 4. Click Cancel and the modal should close.
 5. Click Delete and the Ad should get deleted and the user is directed back to the Home page.

#### **Ad Card Image**

 1. Check the Ad card image is fully responsive and covers half the page in medium to large screen size.
 2. Check the image takes a full-screen size in mobile view.
 3. Check for the responsiveness and the image doesn't stretch or squished while checking responsiveness.

#### **Ad Details**

 1. Check the Ad card details are fully responsive and cover half the page in medium to large screen size.
 2. Check the details takes a full-screen size in mobile view.
 3. Check for the details spelling error.
 4. Check the Tooltip if it showing correct status when hovered over.
 5. Check the Ad description is informative.

### **Post Ad Page**

 1. Log in to the site and check if the Post Ad link appears in the Navbar.
 2. Click the Post Ad link and the **Post Ad** form should open.
 3. Check the Category dropdown and select anything, the category gets selected.
 4. Do not select anything and got o next input, the category section becomes red because of proper validation.
 5. Check the Photo URL input section, upload some link and it should turn green.
 6. Check Price, Description, and Title inputs by adding some text and numbers, it takes everything.
 7. Check the condition dropdown, It is allowing to select from the 3 conditions. 
 8. Check Location, email, and Telephone by adding some details, it is taking all details.
 9. Check the switch if it is working by selecting available or sold, of your choice.
 10. Click the **Post Ad** button, The ad is posted and the user is directed back to Home Page with a new Ad posted.
 11. Leave any input field blank and click **Post Ad**, the blank section will prompt you to fill it up.
 12. Check in different screen sizes, repeat steps 1 to 11.

### **Edit Page**

 1. Log in through any user profile who has posted anything or Admin's profile.
 2. The Edit button should be visible on vied Ad page, which directs the user to the Edit Ad page.
 3. Check if the details of the cards are already filled in the input sections.
 4. Change any input, dropdown, or switch status, Click the **Edit Ad** button at the bottom of the page.
 5. Flash message appears as **Ad Successfully Updated** and the user remains on the Edit Ad page.
 6. After any change, click the **Cancel** button at the bottom of the page, 
    the user is directed to the home page without any change done to the card detail.
 7. Go to the mobile view and repeat steps 1 to 6.


### **Delete Modal**

 1. Log in through any user profile who has posted anything or Admin's profile.
 2. The Delete button should be visible on vied Ad page, which opens the Delete Modal.
 3. The delete modal has 2 buttons, Cancel and Delete.
 4. Click **Cancel** and Modal get closed and the User remains on the View Ad page.
 5. Click **Delete** and the Ad gets deleted and the user is directed to the Home Page.
 6. Repeat steps for the mobile view also.


### **Profile Page**

 1.  Log in through any user profile who has posted anything or Admin's profile.
 2. A Welcome message with username appears.
 3. All the Ads posted by the user are visible on the page, like the home page.
 4. Logout and then log in again with a username that has not posted anything.
 5. A message appears that the user has not posted anything and one link is there which directs the user to the Post Ad page.
 6. Go to mobile view and repeat steps 1 to 5.


### **Manage Catagory Page**

 1. Log in with Admin's profile, The **manage Category** link should be there on the Navbar.
 2. Click that and Manage category page opens.
 3. Click the **Add Category** button on the top, Add Category Page opens.
 4. Add any category, and click the Add Category button, The new category gets added with a flash message that **New category added** and the user is directed to the Category page.
 5. On the Category card, click the Edit button, the edit category page opens, with the existing category name already there.
 6. Make some changes and click Edit, user gets directed back to manage Category page with message "category successfully Updated".
 7. Click the Cancel and User directed back to Manage Category page.
 8. Click the Delete button on the Category Card, Delete modal pops up, click cancel, and Model is closed.
 9. Click delete on Modal and the category card gets deleted with a flash message that Category Successfully Deleted.
 10. Go to the mobile View and repeat steps 1 to 9.

### **Contact Us Page**

 1. Check spelling and content in the form.
 2. Check the **Full Name** section and the form, check if it allows writing.
 3. Check in the **Email** section, check if it gives a message when the email format is not correct.
 4. Write some text in the **Feedback** area, check if it allows writing more than 3 lines.
 5. Click the **Submit** button, check if the email is received in the recipient email address.
 6. Click the submit button, check it turns **green** color after submitting, and its text changes to `"Feedback Sent"`.
 7. Go to Mobile view and repeat steps 1 to 6.

### **Login Page**

 1. Check the Username section, check if it allows entering after following the pattern.
 2. Try to enter something, not in the pattern, the sections turn red and a message also turns red, which says "Username and Password must be
    5-15 characters long, with only numbers and letters"
 3. Repeat this with the password.
 4. Click the Log In button, profile Page gets opens.
 5. Check the small text below the form, click the Register link and the registration form gets opens.
 6. Repeat the steps with the Mobile view.

### **Register Page**

 1. Check the Username section, check if it allows entering after following the pattern.
 2. Try to enter something, not in the pattern, the sections turn red and the message also turns red, which says "Username and Password must be
    5-15 characters long, with only numbers and letters"
 3. Repeat this with the password.
 4. Click the Register button, profile Page gets open with a "Registration Successful" message.
 5. Check the small text below the form, click the log in link, and the Login form gets opens.
 6. Repeat the steps with the Mobile view. 

### **Error Handler**

 1. On the live Heroku app , type something (which is not the name of any page of the site) in the URL .
 2. Press enter and 404 image will show. 
 3. Click to the word "Ads" and the user is back to the Home page.
   

 [Go to Top](#testing)
***

## **Responsiveness**

 * DevTools- Devices tested across a range of widths: iPhone5(320px)| Samsung S5(360px)| iPhone6/7/8/X(375px)| iPhone6/7/8 Plus(414px)| iPad(768px)| iPad Pro(1020px)| Laptop(1200px)| Large Desktop Screen(1920px)
 * Viewed site on above range on various browsers: Google Chrome, Firefox, Opera, Safari.
 * Viewed on physical devices: small phone(320px)| Large phone(414px)| large tablet(768px)| medium, laptop(1366px)| Large Desktop Screen(1920px)

[Go to Top](#testing)
***

## **Browser Compatibility**

### **Desktop / Laptop**

 **Google Chrome** - All tested and working correctly.

 **Microsoft Edge** - All tested and working correctly.

 **Mozilla Firefox** - All tested and working correctly.

 **Safari** - All tested and working correctly.

### **Tablet**

 **Safari** - All tested and working correctly.

### **Mobile**

 **Google Chrome** - All tested and working correctly.

 **Safari** - All tested and working correctly.

 **Samsung Internet** - All tested and working correctly.
 
     
[Go to Top](#testing)
***
## **Lighthouse**
 * The Lighthouse testing done in the beginning was giving not very good result.

   ![image](static/images/lighthouse.JPG)

   So, the suggestion given by the DEvtools were followed and these steps are taken:

   * The suggestion was to add meta description in the head tag. Which is done by doing this.

      ![image](static/docs/meta.JPG)

    * The suggestion was to add rel where target blank is given. Target blank ia given in the Footer with Github and Linkedin links.
      so the code is added and now it looks like this.

      ![image](static/docs/rel.JPG)

    * The suggestion was to add aria-label in the search bar cancel anchor tag. The code is added but it was 
     later removed as it was giving error in HTML validation .

      ![image](static/docs/aria.JPG)

    * The suggestion was to add async or defer in script tag if it is in head. 

      ![image](static/docs/emailjs.JPG)

    * The Hero image was taking a long time to load, so I ahve reduced the size of the image by TinyPNG and added it back.

    After doing all this changes the Lighthouse score is finally this.

    ![image](static/docs/lighthousefinal.JPG)



[Go to Top](#testing)
***

## **Project Barrier**

* During User Testing it was found that the View Ad page can be edited and deleted from the URL even if the user is not the owner of the post.
 To prevent this One defensive Programming is added in the app.py, which directs the user to Home page if anyone tries to do that.
 The code can be seen here:

  ![image](static/images/app.JPG)

* During User Testing it was found that User gets confused after coming to Profile page, 
  They had no idea which link to click next, so one message is added at the bottom of the page, which has link to Home page and tell them of they want to
  view all ads then click here.

* During User testing it was observed that after opening View Ad page, user has no idea what to do next, so one statement is added based on availability of the item,
  If it is available then contact seller with email or telephone, if sold then keep shopping. 

* The Email.js user id, which is used for this site was first kept in base.html as it has to be in <head> element, but after considering of 
  not disclosing any sensitive information on front page, it is transferred to to contact.html page and to keep it in head element , it is being wrapped in 
  another code which is a part of head element.
  
[Go to Top](#testing)
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
* The console shows error that 'env' imported but never used, env is hidden in the .gitignore file.

* The Home page(get_ads.html) is showing one warning in console on line 44 that special chahracters must be escaped.
  the character [>] is a part of the if loop and can not be escaped.

* The Profile page is also showing warning in console in line 15 that special chahracters must be escaped.
  the character [>] is a part of the if loop and can not be escaped.

* Every page is showing that the Doctype must be declared first. 
 As jinja template is used in the project, so that warning can be ignored for now.

* Edit ad page is giving error that is_available id is used twice, That is part of the code and can not be changed. 

[Go to Top](#testing)
***












