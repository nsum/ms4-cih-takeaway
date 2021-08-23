[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://shields.io/)

![logo](/media/readme-files/nsum.png "nsum logo")

#### Code Institute - Milestone Project 4
## Full Stack Django App 
## Cork International Hotel Takeaway Service
![Am I Responsive](/media/readme-files/responsive.png)
[View the project live here](https://ms4-cih-takeaway.herokuapp.com/)
## Introduction
Welcome,
This Full Stack Web App was made as a 4th Milestone Project with Code Institute.
Hotel I work in was like many others severely impacted by Covid-19 pandemic. 
In efforts to create some revenue, the Hotel started to offer food takeaway service.
At the moment service operates by people calling the hotel's reception and receptionist taking the order over the phone.
This method is not very convenient as receptionists are sometimes unable to take a call or information sometimes gets lost in the process.
Hence the idea for this project. This app would make it easy for people to put in an order, and make it easier for the hotel to process it.


## Table of Contents

1. [User Experience (UX)](#user-experience)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Design](#design)
2. [Test Usage](#test-usage)
    - [Profile](#profile)
    - [Test Payments](#test-payments)
    - [Stripe Test CC](#stripe-test-credit-card)
3. [Techonologies Used](#technologies-used)
    - [Languages](#languages-used)
    - [Frameworks, Libraries & Tools Used](#frameworks-libraries-tools-used)
4. [Features](#features)
    - [General Features](#shared-features)
    - [Navbar](#navbar)
    - [Toast Messages](#toast-messages)
    - [Blog](#blog)
    - [Homepage](#homepage)
    - [Items](#items)
    - [Shopping Bag](#shopping-bag)
    - [Checkout](#checkout)
    - [Profile](#profile)
    - [Django-allauth](#django-allauth)
    - [Automatic E-mails](#automatic-e-mails)
5. [Testing](#testing)
    - [Valdators](#validators)
    - [Automated Testing](#automated-testing)
    - [Manual Testing Procedures](#manual-testing-procedures):
        - [Navigating The Site](#testing-navigating-the-site)
        - [Login](#login-testing)
        - [Logout](#log-out-testing)
        - [Register New User](#register-new-user-testing)
        - [Browsing & Adding Items to Shopping Bag](#browsing-and-adding-items-to-shopping-bag)
        - [Shopping Bag](#bag-testing)
        - [Checkout](#checkout-testing)
        - [Blog](#blog-testing)
        - [Post Comments](#post-comments)
        - [Profile Info and Order History](#profile-info-and-order-history)
        - [Search Bar](#search-bar)
    - [Unresolved Issues](#unresolved-issues)
    - [Testing User Stories from User Experience (UX) Section](#testing-user-stories):
        - [First Time Visitors](#testing-first-time-visitors)
        - [Non-registered Users](#testing-non-registered-users)
        - [Registered & Regular Visitors](#testing-registered-and-regular-visitors)
        - [Users With Special Diatery Requirements](#testing-users-with-special-diatery-requirements)
        - [Ordering & Purchasing](#testing-ordering-and-purchasing)
6. [Data Models](#data-models)
    - [Blog App Models](#blog-app)
    - [Checkout App Models](#checkout-app)
    - [Items App Models](#items-app)
    - [Profiles App Models](#profiles-app)

# User Experience
+   ## User Stories
+   ### First Time Visitors
    1. I want to be able to easily understand the purpose of the site and easily navigate it
    2. I want to easily and quickly purchase my takeaway
    3. I want to see collection location on map and clear instructions on how to get there and collect my order

+   ### Non-registered Users
    1. I want to freely browse the site without being registered
    2. I want to be able to make an order without registering on the site

+   ### Registered & Regular Visitors
    1. I want some kind of incentive to register and use the site
    2. I want to be able to see my order history

+   ### Users With Special Diatery Requirements
    1. As someone who has Gluten intolerance, I want to be able to be able to distinguish Gluten-free meals
    2. As a vegan, I want to be able to easily distinguish Vegan options from non-vegan ones
    3. As someone with allergies, I want the menu to have information on any allergens in the meals or drinks

+   ### Ordering & Purchasing
    1. I want to easily see my shopping bag and bag totals as I add items to it
    2. I want to see overview of my order before completing the purchase
    3. I want my payment to be securely proccessed


+ ## Wireframes
    + [Index Page - Desktop](/media/readme-files/home.png) 
    + [Basket - Desktop](/media/readme-files/basket.png) 
    + [Checkout - Desktop](/media/readme-files/checkout.png) 
    + [Menu - Desktop](/media/readme-files/menu.png)

+   ## Design
    + Colour Scheme: The main colour is carrot (#f2aa4c) with black and white notes.
    + Bootstrap classes and custom CSS were used to make the app fully responsive on all screen sizes.




# Test Usage
+   ### Profile
    - Application allows anonymous purchases
    - Anyone can visit the [live site](https://ms4-cih-takeaway.herokuapp.com/) and create a new profile by clicking "Register" in the upper right corner of the navbar.
    - After creating a profile, an email confirmation is sent and user needs to verify their email address in order to login
    - After successfully confirming the email address user will have access to his profile tab
+   ### Test Payments
    - Test purchases can be done using Stripe and stripe's test CC info found below
+   ### Stripe Test Credit Card:
    - Credit Card: 4242 4242 4242 4242
    - Expiration date: Any future date
    - CVC: Any 3-digit number
    - ZIP: Any 5-digit number

# Technologies Used

### Languages Used
+   [HTML5](https://en.wikipedia.org/wiki/HTML5)
+   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
+   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
+   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks Libraries Tools Used
+ [Django:](https://www.djangoproject.com/) was used as a web framework used to develop this app.
+ [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
+ [Jinja](http://jinja.pocoo.org/docs/2.10/) to simplify displaying data from the backend of this project smoothly and effectively in HTML.
+ [Heroku:](https://www.heroku.com/) was used as deployment platform
+ [requirements.txt:](requirements.txt) contains list off all dependancies
+ [Randomkeygen:](https://randomkeygen.com/) was used for encrypting vars.
+ [Git:](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
+ [GitHub:](https://github.com/) is used to store the project's code after being pushed from Git.
+ [Font Awesome:](https://fontawesome.com/) was used on all pages throughout the website to add icons for aesthetic and UX purposes.
+ [Imagecompressor.com:](https://imagecompressor.com/) was used to compress images
+ [Bootstrap:](https://getbootstrap.com/) was used for design and customization
+ [jQuery:](https://jquery.com/) was used for document traversal, manipulation, event handling & animations.
+ [Am I Responsive:](http://ami.responsivedesign.is/) was used to create the image at the top of README.md
+ [Stripe:](https://stripe.com/en-ie) was used as payment processor for test payments
+ [Amazon AWS:](https://aws.amazon.com/) were used as cloud storage for media and static files
+ [Gmail:](https://www.google.ie/) was used for sending automated emails
+ [SQLite:](https://www.sqlite.org/index.html) was used as db during development
+ [Heroku Postgres:](https://www.postgresql.org/) was used as attached database on Heroku used for deployed version of the app 

### Media
+	[Hero Image](https://www.corkinternationalairporthotel.com/wp-content/uploads/2021/03/Dinner-Date-1-1920x1080.jpg)












# Features
+   ### Shared Features
    - Is fully mobile responsive and reacts to changes in screen size. It also allows for collapsible menu on mobile screens.
    - Items lists and mobile view shopping bag have back to top button in lower right corner.
    - All external links open in a new tab
+   ### Navbar
    - Contains all the categories of products on the site through the various drop downs.
    - Users can also quickly search for items (no blog articles) via the navigation's search bar
    - Shopping bag subtotal and link to bag
    - Link to login/register for unlogged users and/or profile/logout for logged in users
    - CIH Takeaway logo is link to a home page
    - Navbar also contains a link to the blog app
+   ### Toast Messages
    - They flash on screen for all key actions such as logging in / registering / adding items to cart / rating and reviewing products / completing purchases / errors
    - Their purpose is to give messages displayed at the right corner of the page to provide the user confirmation of actions like sign out, adding or editing bag etc.
+   ### Blog
    - Simple blog app with useful food articles was added to enrich the content on the site.
    - Posts are made by admins of the site, while comments can be made by both logged/anonymous users.
    - After comment has been made it is not published until it is approved in the admin panel
+   ### Homepage
    - Homepage is a simple landing page with hero image in the background, call to action information and a link to items list.
+   ### Items
    - Can be sorted by price/category/rating/name
    - All items have: name, description, allergen info, price, rating, category
    - All items are connected to their perspective categories
    - All alcoholic drinks show a warning that ID may be required on collection to prove the age.
    - Allergen information for each can be viewed under item description
    - List of all allergens is available by clicking i icon next to any allergen
    - Adding an item to basket opens a modal which is closable by clicking outside it, by clicking x, or by clicking "keep shopping" button.
+   ### Shopping Bag
    - Contains list of all items added to it with their quantities and subtotals.
    - Bag will display totals before discount, discount (if applicable) and grand total for the order.
    - It also contains a call to action with amount additionally required to be spent in order for discount to be applied.
    - Users can increase/decrease quantity of items in the bag or remove them completely from the shopping bag.
    - "Keep Shopping" button brings the user back to items list while "Checkout" button proceeds to checkout page.
    - If there are no items in the shopping bag, it will say it's empty and only contain "Keep Shopping" button.
+   ### Checkout
    - If the user is logged in, form data will be prefilled by users information and can mark the checkbox to update their profile information if any info has changed
    - Users that are not logged in can still go through with the order but their information won't be saved to any profile. They will be asked if they would like to register or login towards the bottom of the form.
    - Payment proccessing is in testing environment so no real payments are accepted. Test payment can be made using test data found [here](#stripe-test-credit-card).
    - After completing the order, toast message is displayed containing Order Number 
    - If user is logged in, after completing the order his order information is saved on "Profile" page under "Order History".
    - A webhook is implemented within the checkout app, so the order is successfully processed even in case of process getting interrupted
+   ### Profile
    - Available only to logged in users
    - Contains of editable user information (used to prefill the form on checkout) and user's order history 
+   ### Django-allauth
    - Django-allauth is a Python package used to provide a set of features such as signup, login, logout, password change etc.
    - After signing up, a verification e-mail is sent to the registered e-mail to confirm it. Once confirmed, the user can log in with their credentials and access the profiles app.
+   ### Automatic e-mails
    - A Gmail account is set up for this project and used as a sender for all verification, reset and confirmation e-mails.






# Testing
### Validators
+   #### Validators were used to validate pages to ensure there were no errors:
    -   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](/media/readme-files/validate-css.png)
    -   [Lighhouse Tool](https://developers.google.com/web/tools/lighthouse) - [Results](/media/readme-files/lighthouse.png)
    -   [W3C HTML Validator](https://validator.w3.org/nu/) - Was returning "Duplicate ID" errors due to jinja for loops.




### Automated Testing
+   I wished to create more tests but as submission deadline approaching it was not possible.
    Below models tests were made to familiarize with testing procedures and practices.
+   #### Blog Models
    - Tested blog models with 93% coverage - [blog/tests.py](/blog/tests.py)
+   #### Checkout Models
    - Tested checkout models with 94% coverage - [checkout/tests.py](/checkout/tests.py)


### Manual Testing Procedures
+   #### Testing Navigating The Site
    - Browsing & purchasing as an unlogged user:
        - Expected: Have the same availability as logged user except having access to "Profile" page. 
        - Testing: visited site as unlogged user
        - Result: expected results
    - Typing directly in the URL bar as unlogged or non-admin user:
        - Expected: before the user is logged in if he tries to type in views directly in URL bar, he is redirected to login page 
        - Testing: Tried to type in directly in URL bar as both logged in and logged out.
        - Result: Expected results.
    - Browsing as admin user:
        - Expected: Experience indentical to non-admin users apart from access to admin panel
        - Testing: logged in as an admin user and browsed the site 
        - Result: Expected results.
    - Back to top buttons:
        - Expected: Items lists and mobile view shopping bag to have back to top button in the lower right corner
        - Testing: browsed the items and opened shopping bag on mobil view
        - Result: Expected results in both cases.
+   #### Login Testing
    - If either username or password is incorrect:
        - Expected: redirect back to login and flash message "Incorrect Username and/or Password"
        - Testing: tried inputting just wrong username, just wrong password, and tried both wrong password and username
        - Result: got expected results on all tries
    - If both username and password are correct:
        - Expected: user to be logged in and toast message confirming successful login
        - Testing: inputted correct username & password
        - Result: got expected results
+   #### Log Out Testing
    - Log the user out by clicking 'Log Out' button:
        - Expected: redirect back to homepage and delete the current session cookie
        - Testing: while logged in, clicking on 'Log Out' button
        - Result: expected result
+   #### Register New User Testing
    - Create a new user:
        - Expected: if all inputs are valid, insert a new record in in db, and flash message 
            that confirmation email has been sent
        - Testing: input valid information and click register
        - Result: got expected results
    - Passwords do not match:
        - Expected: If 'password' and 'repeat password' do not match exactly, flash 'Passwords Do Not Match' and return to the registration page
        - Testing: Input all correct values except input two different passwords and click submit
        - Result: got expected results
    - Any of the fields left blank:
        - Expected: form to warn that field is required and to fill it in
        - Testing: tried leaving just one field empty at a time, tried leaving all fields empty, tried leaving empty pairs
        - Result: got expected results on each try
    - Min / max chars:
        - Expected: If any of the inputs are to short or too long, form should warn the user
        - Testing: tried inputting less than min chars, tried inputting more than max, on all the fields
        - Result: Got expected results
+   #### Browsing and Adding Items to Shopping Bag
    - If the user selects a category:
        - Expected: only items under selected category to be shown
        - Testing: Browsed the site and selected different categories 
        - Result: got expected results
    - If the user sorts the results:
        - Expected: items to be sorted by desired criteria
        - Testing: Browsed the site and selected different sorting options 
        - Result: got expected results
    - If the user clicks "Add to Basket" on any of the items:
        - Expected: modal to open with item name, information, quantity and navigation buttons
        - Testing: Clicked on add to basket on various items
        - Result: got expected results
    - When the user adds items to the bag:
        - Expected: items and their quantities to be added to session's bag
        - Testing: Added various items with various quantities to bag 
        - Result: got expected results
    - If the user adds an alcoholic item:
        - Expected: warning the user that ID may be required on collection to prove the legal drinking age
        - Testing: Added alcoholic items with various quantities to bag 
        - Result: got expected results
+   #### Bag Testing
    - If there are no items in the bag:
        - Expected: text saying that the bag is empty and "Keep Shopping" button displayed
        - Testing: Visited bag without adding any items
        - Result: got expected results
    - If there are items in the bag:
        - Expected: a list with all the items, their descriptions, prices and quantities to be displayed
        - Testing: Visited bag after adding various items
        - Result: got expected results
    - If grand total is under discount threshold:
        - Expected: red text under the grand total showing user the amount needed to be spent more in order to get the discount.
        - Testing: Added items to the bag with total value less than the discount threshold
        - Result: got expected results
    - If grand total is over the discount threshold:
        - Expected: red text to dissapear and discount to be visible and applied to grand total.
        - Testing: Added items to the bag with total value greater than the discount threshold
        - Result: got expected results
    - Changing the quantities or removing the items:
        - Expected: if quantity is increased or decreased bag to update accordingly, and to remove the item if remove item link is clicked
        - Testing: changed quantities of the items in the bag as well as tried clicking remove item
        - Result: got expected results
    - "Keep Shopping" & "Checkout" buttons:
        - Expected: if keep shopping button is clicked return the user to items list, and if checkout button is clicked, than take the user to the checkout page
        - Testing: tested both keep shopping and checkout buttons
        - Result: got expected results
+   #### Checkout Testing
    - If the user is logged in:
        - Expected: order form to be prepopulated with data from his profile and checkbox on the bottom of the form to save changed information if there were any changes
        - Testing: Visited checkout page as a logged in user 
        - Result: got expected results
    - If the user is not logged in:
        - Expected: order form to be empty and register/login links to be displayed towards the bottom of the form
        - Testing: Visited checkout page without logging in 
        - Result: got expected results
    - Order Summary:
        - Expected: order summary to be displayed showing all the ordered items, their prices, discount and grand total amount
        - Testing: Visited checkout page with single item in the bag, multiple items, multiple items with various quantities
        - Result: got expected results
    - Checkout Form:
        - Expected: crispy forms to valdate the input in the form, and pickup date to have disabled past dates
        - Testing: Visited checkout page and filled in the form different ways 
        - Result: got expected results
    - Completing the order:
        - Expected: payment to be taken on Stripe, order to be put through to orders in admin panel, bag to be empty and if the user is logged in then show his order in order history under his profile
        - Testing: Completed the order as both logged and unlogged user, using different items and quantities
        - Result: got expected results
    - Stripe Payments:
        - Expected: order to go through on both Stripe and Admin panel even in the event of closing the browser, lost connection, or similar
        - Testing: Purposely closed the browser immediately after clicking complete the order and before the form was posted
        - Result: Stripe payment received but no order added to orders in admin panel. when visited the website again, bag was still populated with the items instead of being emptied.
+   #### Blog Testing
    - Blog status publish/draft:
        - Expected: if the created post is marked as draft, not to be displayed on the site, and if it's marked published then display it on a list of posts on the site
        - Testing: added couple of published posts, and few draft ones
        - Result: got expected results, draft posts are not displayed on the site
    - Post list view:
        - Expected: to display list of all published posts
        - Testing: added numerous posts and published them, then visited the blog
        - Result: got expected results
    - Post details view:
        - Expected: To display title, creator, date created, full post, related comments, and leave a comment section
        - Testing: visited various posts
        - Result: got expected results
+   #### Post Comments
    - Posting a new comment:
        - Expected: when user creates a comment, comment form do dissappear and display "Your comment is awaiting moderation". Comment to be added to admin panel for approval
        - Testing: added couple of comments to various posts
        - Result: got expected results
    - After comment has been approved:
        - Expected: comment to be displayed under the related post along with any other approved comments
        - Testing: approved comments through admin panel
        - Result: got expected results
+   #### Profile Info and Order History
    - If the user is not logged in:
        - Expected: user not to have access to profile page and to be redirected to login page
        - Testing: tried visitng profile page as unlogged user
        - Result: got expected results
    - If the user is logged in:
        - Expected: editable user info to be displayed, and order history with all previous orders to be visible
        - Testing: tried visitng profile page as logged in user
        - Result: got expected results
+   #### Search Bar
    - Using the Search Bar:
        - Expected: search through items only (no posts, comments) and return related results
        - Testing: searched different terms, items names, blogpost names, comment content
        - Result: got expected results

### Unresolved Issues
- Abrupting the complete order proccess:
    If the browser is forcefully closed or there is a loss of connection just after clicking complete order but before the page has refreshed and submitted the data, Stripe will receive the payment but the order won't be completed on the site. Bag will still show same items and admin panel won't have the order under the orders.


### Testing User Stories
+   #### Testing First Time Visitors
    1. I want to be able to easily understand the purpose of the site and easily navigate it
        - Top navbar is easily understandable and contains name of the site, while hero image explains the purpose 
    2. I want to easily and quickly purchase my takeaway
        - Items are organized into categories and after adding the items to the bag, order is quickly completed by filling out short form and paying for the order
    3. I want to see collection location on map and clear instructions on how to get there and collect my order
        - After order is processed order summary is displayed and contains all the information about the order as well as link to google maps location that users can easily follow to collect the order
+   #### Testing Non-registered Users
    1. I want to freely browse the site without being registered
        - unregistered users can freely browse the site and purchase orders, only restriction is they don't have a profile so their form information won't be saved and they won't have access to their order history
    2. I want to be able to make an order without registering on the site
        - unregistered users can freely browse the site and purchase orders, only restriction is they don't have a profile so their form information won't be saved and they won't have access to their order history
+   #### Testing Registered and Regular Visitors
    1. I want some kind of incentive to register and use the site
        - registered users have access to their order history and their information is stored for quicker consecutive ordering
    2. I want to be able to see my order history
        - logged in users have access to their order history by visiting their profile page
+   #### Testing Users With Special Diatery Requirements
    1. As someone who has Gluten intolerance, I want to be able to be able to distinguish Gluten-free meals
        - every item contains item's allergen information on it's detail view
    2. As a vegan, I want to be able to easily distinguish Vegan options from non-vegan ones
        - "Vegan Options" category contains vegan meals 
    3. As someone with allergies, I want the menu to have information on any allergens in the meals or drinks
        - on item detail views, every item has a list of all the allergens associated with that item, and there is an "i" icon next to allergens which opens modal with list of all allergens
+   #### Testing Ordering and Purchasing
    1. I want to easily see my shopping bag and bag totals as I add items to it
        - Upper right corner contains link to a bag and total amount of the bag at any given point. Clicking on the bag icon opens the shopping bag
    2. I want to see overview of my order before completing the purchase
        - Shopping bag contains all the items with their descriptions, prices, quantities and totals. Going forward to checkout again contains entire order summary with all the items, quantities and prices
    3. I want my payment to be securely proccessed
        - Stripe and Django handle secure processing of the payment
=====================================================
MS3==================================================
=====================================================



5. [Testing](#testing)
    - [Valdators](#validators)
    - [Manual Testing Procedures](#manual-testing-procedures):
        - [Navigating The Site](#navigating-the-site)
        - [Login](#login)
        - [Logout](#log-out)
        - [Register New User](#register-new-user)
        - [Creating new task](#creating-new-task)
        - [Editing tasks](#editing-tasks)
        - [Completing the task](#completing-the-task)
        - [Deleting the task](#deleting-the-task)
        - [Testing the lists](#testing-the-lists)
    - [Unresolved Issues](#unresolved-issues)
    - [Bugs & Fixes](#bugs-and-fixes)
    - [Coding Process](#coding-process)
    - [Testing User Stories from User Experience (UX) Section](#testing-user-stories):

6. [Data Schema](#data-schema)
    - [Tasks Collection](#tasks-collection)
    - [Departments Collection](#departments-collection)
    - [Users Collection](#users-collection)

7. [Credits](#credits)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)
    - [Media](#media)

8. [Deployment](#deployment)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)

9. [Contact](#contact)






# Data Models
+   Django's default SQLite3 was used as a database during the development fase, while Heroku's add-on PostgreSQL database is used in deployed version of the project.
+   ## Blog App
+   ### Post Model
    | Name          | Database Key  | Field Type        | Validation                             |
    | ------------- | ------------- | ----------------- | -------------------------------------- |
    | Title         | title         | models.CharField  | max_length=200, unique=True            |
    | Slug          | slug          | models.SlugField  | max_length=200, unique=True            |
    | Author        | author        | `models.ForeignKey` | `User`, on_delete=models.CASCADE, related_name="blog_posts" |
    | Content       | content       | models.TextField() |                                        |
    | Created On    | created_on    | models.DateTimeField | auto_now_add=True                   |
    | Status        | status        | models.IntegerField | choices=STATUS, default=0           |

+   ### Comment Model
    | Name          | Database Key  | Field Type        | Validation                             |
    | ------------- | ------------- | ----------------- | -------------------------------------- |
    | Post          | post          | `models.ForeignKey` | `Post`, on_delete=models.CASCADE, related_name="comments" |
    | Name          | name          | models.CharField  | max_length=80                          |
    | Email         | email         | models.EmailField() |                                      |
    | Body          | body          | models.TextField() |                                       |
    | Created On    | created_on    | models.DateTimeField | auto_now_add=True                   |
    | Active        | active        | models.BooleanField | default=False                        |
+   ## Checkout App
+   ### Order Model
    | Name          | Database Key  | Field Type        | Validation                             |
    | ------------- | ------------- | ----------------- | -------------------------------------- |
    | Order Number  | order_number  | models.CharField  | max_length=32, null=False, editable=False |
    | User Profile  | user_profile  | `models.ForeignKey` | `UserProfile`, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
    | Full Name     | full_name     | models.CharField  | max_length=50, null=False, blank=False |
    | Email         | email         | models.EmailField | max_length=254, null=False, blank=False |
    | Phone Number  | phone_number  | models.CharField  | max_length=20, null=False, blank=False |
    | Postcode      | postcode      | models.CharField  | max_length=20, null=True, blank=True   |
    | City          | town_or_city  | models.CharField  | max_length=40, null=False, blank=False |
    | Address 1     | street_address1 | models.CharField | max_length=80, null=False, blank=False |
    | Address 2     | street_address2 | models.CharField | max_length=80, null=False, blank=False |
    | Date          | date          | models.DateTimeField | auto_now_add=True                   |
    | Pickup Date   | pickup_date   | models.DateField  | null=False, blank=False                |
    | Pickup Time   | pickup_time   | models.TimeField  | null=False, blank=False                |
    | Optional Notes | optional_notes | models.CharField | max_length=254, null=True, blank=True |
    | Discount      | order_discount | models.DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |
    | Order Total   | order_total   | models.DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
    | Grand Total   | grand_total   | models.DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
    | Original Bag  | original_bag  | models.TextField  | null=False, blank=False, default=''    |
    | Stripe pid    | stripe_pid    | models.CharField  | max_length=254, null=False, blank=False, default='' |
+   ### OrderLineItem Model
    | Name          | Database Key  | Field Type        | Validation                             |
    | ------------- | ------------- | ----------------- | -------------------------------------- |
    | Order         | order         |  `models.ForeignKey` | `Order`, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
    | Item          | item          | `models.ForeignKey` | `Item`, null=False, blank=False, on_delete=models.CASCADE |
    | Quantity      | quantity      | models.IntegerField | null=False, blank=False, default=0   |
    | LineItem Total | lineitem_total | models.DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |
+   ## Items App
+   ### Category Model
    | Name          | Database Key  | Field Type        | Validation                             |
    | ------------- | ------------- | ----------------- | -------------------------------------- |
    | Category Name | name          | models.CharField  | max_length=254                         |
    | Friendly Name | friendly_name | models.CharField  | max_length=254, null=True, blank=True  |
+   ### Item Model
    | Name          | Database Key  | Field Type        | Validation                             |
    | ------------- | ------------- | ----------------- | -------------------------------------- |
    | Category      | category      |  `models.ForeignKey` | `'Category'`, null=True, blank=True, on_delete=models.SET_NULL |
    | Item Name     | name          | models.CharField  | max_length=254)                        |
    | Description   | description   | models.TextField() |                                       |
    | Allergens     | allergens     | models.CharField  | max_length=254, null=True, blank=True  |
    | Price         | price         | models.DecimalField | max_digits=6, decimal_places=2       |
    | Rating        | rating        | models.DecimalField | max_digits=3, decimal_places=1, null=True, blank=True |
+   ## Profiles App
+   ### UserProfile Model
    | Name          | Database Key  | Field Type        | Validation                             |
    | ------------- | ------------- | ----------------- | -------------------------------------- |
    | User          | user          | models.OneToOneField | User, on_delete=models.CASCADE      |
    | Phone Number  | default_phone_number | models.CharField | max_length=20, null=True, blank=True |
    | Postcode      | default_postcode | models.CharField | max_length=20, null=True, blank=True |
    | City          | default_town_or_city | models.CharField | max_length=40, null=True, blank=True |
    | Address 1     | default_street_address1 | models.CharField | max_length=80, null=True, blank=True |
    | Address 2     | default_street_address2 | models.CharField | max_length=80, null=True, blank=True |


============

# Credits

### Code
+	[Alvin Wang](https://github.com/Dogfalo) - `select.js` which solves the issue with form select on mobile

### Acknowledgements
+   [Spencer Barriball](http://www.5pence.net/) - Huge thank you to my mentor Spencer for all his help and guidance
+   [codeinstitute.net](https://codeinstitute.net/) - Lessons, videos, tutoring & support
+   [Cork International Hotel](https://www.corkinternationalairporthotel.com/) - For showing interest in using this app
+   [Anna Greaves](https://github.com/AJGreaves) - For README.md Heroku deployment section
+   [Code Institute Sample README](https://github.com/Code-Institute-Solutions/SampleREADME) - Readme Template

### Media
+	[Parallax Image 1](https://cf.bstatic.com/images/hotel/max1024x768/653/65346226.jpg)
+	[Parallax Image 2](https://www.corkinternationalairporthotel.com/wp-content/uploads/2019/07/lobby-003.jpg)

# Deployment

### Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) 
    to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### How to run this project locally
To run this project on your own IDE follow the instructions below:
Ensure you have the following tools: 
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine. 
    - How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).

#### Instructions
1. Save a copy of the github repository located at https://github.com/nsum/ms3-hotel-task-manager by clicking 
the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/nsum/ms3-hotel-task-manager
```

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
```
python -m .venv venv
```  
_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

4. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

5. Install all required modules with the command 
```
pip -r requirements.txt.
```

6. In your local IDE create a file called `.env.py`.

7. Inside the .env file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. 

8. You can now run the application with the command
```
python app.py
```

9. You can visit the website at `http://127.0.0.1:5000`

### Heroku Deployment

To deploy this app to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

### Contact

your.marketer1303@gmail.com