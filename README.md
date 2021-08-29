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
**<details><summary>User Experience (UX)</summary>**
* [User Stories](#user-stories)
* [Wireframes](#wireframes)
* [Design](#design)
</details>

**<details><summary>Test Usage</summary>**
* [Profile](#profile)
* [Test Payments](#test-payments)
* [Stripe Test CC](#stripe-test-credit-card)
</details>

**<details><summary>Techonologies Used</summary>**
* [Languages](#languages-used)
* [Frameworks, Libraries & Tools Used](#frameworks-libraries-tools-used)
</details>

**<details><summary>Features</summary>**
* [General Features](#shared-features)
* [Navbar](#navbar)
* [Toast Messages](#toast-messages)
* [Blog](#blog)
* [Homepage](#homepage)
* [Items](#items)
* [Shopping Bag](#shopping-bag)
* [Checkout](#checkout)
* [Profile](#profile)
* [Django-allauth](#django-allauth)
* [Automatic E-mails](#automatic-e-mails)
</details>

**<details><summary>Testing</summary>**
* [Validators](#validators)
* [Automated Testing](#automated-testing)
* [Manual Testing Procedures](#manual-testing-procedures):
    * [Navigating The Site](#testing-navigating-the-site)
    * [Login](#login-testing)
    * [Logout](#log-out-testing)
    * [Register New User](#register-new-user-testing)
    * [Browsing & Adding Items to Shopping Bag](#browsing-and-adding-items-to-shopping-bag)
    * [Shopping Bag](#bag-testing)
    * [Checkout](#checkout-testing)
    * [Blog](#blog-testing)
    * [Post Comments](#post-comments)
    * [Profile Info and Order History](#profile-info-and-order-history)
    * [Search Bar](#search-bar)
    * [Unresolved Issues](#unresolved-issues)
    * [Testing User Stories from User Experience (UX) Section](#testing-user-stories):
        * [First Time Visitors](#testing-first-time-visitors)
        * [Non-registered Users](#testing-non-registered-users)
        * [Registered & Regular Visitors](#testing-registered-and-regular-visitors)
        * [Users With Special Diatery Requirements](#testing-users-with-special-diatery-requirements)
        * [Ordering & Purchasing](#testing-ordering-and-purchasing)
</details>

**<details><summary>Data Models</summary>**
* [Blog App Models](#blog-app)
* [Checkout App Models](#checkout-app)
* [Items App Models](#items-app)
* [Profiles App Models](#profiles-app)
</details>

**<details><summary>Deployment</summary>**
* [Local Deployment](#local-deployment)
* [Heroku Deployment](#deployment-to-heroku)
</details>

---

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

+   ### Users With Special Dietary Requirements
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



---
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

---
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

---
# Features
+   ### Shared Features
    - Is fully mobile responsive and reacts to changes in screen size. It also allows for collapsible menu on mobile screens.
    - Custom templates added for 403, 404, 500 & 503 HTTP Status code errors
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
---

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
+   #### Testing Users With Special Dietary Requirements
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
---

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
---

# Credits

### Acknowledgements
+   [Spencer Barriball](http://www.5pence.net/) - Huge thank you to my mentor Spencer for all his help and guidance
+   [codeinstitute.net](https://codeinstitute.net/) - Lessons, videos, tutoring & support
+   [Cork International Hotel](https://www.corkinternationalairporthotel.com/) - Menu items & Hero Image
+   [Sean McMahon](https://github.com/Sean-Mc-Mahon) - Readme deployment section

### Articles
+	[The Peanut Puzzle](https://www.newyorker.com/magazine/2011/02/07/the-peanut-puzzle) - by Jerome Groopman
+	[The Secret Life of Cheese](https://roadsandkingdoms.com/2015/the-secret-life-of-cheese/) - Mark Hay
+	[How Junk Food Can End Obesity](https://www.theatlantic.com/magazine/archive/2013/07/how-junk-food-can-end-obesity/309396/) - David H. Freedman
+	[Fruit of the Future](https://www.saveur.com/article/Kitchen/Fruit-of-the-Future/) - by Dan Koeppel
+	[The Vitamin Myth](https://www.theatlantic.com/health/archive/2013/07/the-vitamin-myth-why-we-think-we-need-supplements/277947/) - by Paul Offit

### Media
+	[Hero Image](https://www.corkinternationalairporthotel.com/wp-content/uploads/2021/03/Dinner-Date-1-1920x1080.jpg)
---

# Deployment
+   ### Local Deployment
    1. This repository may be cloned directly into an editor by pasting the following command into the terminal:   
        ````
        git clone https://github.com/nsum/ms4-cih-takeaway

    Alternatively, you can save a copy of this repository by clicking the green button "Clone or download" , then "Download Zip" button, and after extract the Zip file to your folder.

    2. In the terminal window change directory (CD) to the correct file location (directory that you have just created).

    3. Install all requirements from the **requirements.txt** file putting this command into your terminal:
        ```
        pip3 install -r requirements.txt
        ```

    *Note: GitPod does not require `sudo`, so if you use another IDE, you will need to include `sudo` in the beginning of the command: `sudo pip3 install -r requirements.txt`.*

    4. Set up the following environment variables to use the full functionality of the site.

        - SECRET_KEY = your secret key.
        - STRIPE_PUBLIC_KEY = your stripe public key.
        - STRIPE_SECRET_KEY = your stripe secret key.
        - STRIPE_WH_SECRET = your stripe webhook secret.
        - DEVELOPMENT = 'True' 

        - Your stripe variables can be found on your stripe dashboard.
        - You can generate a Django secret key here. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
    5. Then migrate:
        ```
        $ python manage.py migrate
        ```
    6. Populate using relavant fixtures:
        ```
        $ python manage.py loaddata fixtures/<filename>.json
        ```
    7. Create a superuser:

        ```
        $ python manage.py createsuperuser
        ```

    8. You will now be able to run the application using the following command 

        ```
        $ python3 manage.py runserver
        ```

+   ### Deployment to Heroku

    The app may be deployed to Heroku using the following steps:

    - **Create an app on the Heroku website.**
        - Click on the new button.
        - Click on the create a new app.
        - Give the app a name and choose current region.
        - Select create app.

    - **Set up Postgres Database**
    - Heroku
        - In the app resources search for Postgres
        - Add to the project and, choosing the free plan.
        - To use Postgres install 2 dependencies.
            - dj_database_url
            - psycopg2

    - **In Project.**
        - Install the two packages needed 
            ``` 
                pip3 install dj_database_url
            ```
        
            ```
                pip3 install psycopg2_binary
            ```
        - Add them to the requirements.txt file
            ```
            pip3 freeze > requirements.txt
            ```
        - In settings.py import dj_database_url
            ``` python
            import dj_database_url
            ```
        - Comment out the current database settings.
        - Replace them with the settings for the Postgres database.
            ``` python
                DATABASES = {
                    'default': dj_database_url.parse('DATABASE_URL')
                }
            ```
        - Get database URL from app config settings.

        - Then migrate:
            ```
            $ python manage.py migrate
            ```

        - Populate using relavant fixtures:
            ```
            $ python manage.py loaddata fixtures/<filename>.json
            ```

        - Create a superuser:
            ```
            $ python manage.py createsuperuser
            ```
        
        - Commit changes making sure to remove database URL beforehand so it isn't saved in version control.

        - Create an if-else statement in the settings.py to use Postgres if the DATABASE_URL variable is available and if not use the default database
            ``` python
                if "DATABASE_URL" in os.environ:
                    DATABASES = {
                        "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
                    }
                else:
                    DATABASES = {
                        'default': {
                            'ENGINE': 'django.db.backends.sqlite3',
                            'NAME': BASE_DIR / 'db.sqlite3',
                        }
                    }
            ```
        
        - The Postgres database is now ready for use.

    - **Gunicorn**
        - For the app to work install Greenunicorn.
        - To install:
            ```
            pip3 install Gunicorn
            ```
        - Create a Procfile to let Heroku know how to run the app:
            ``` 
                touch Procfile
            ```
        - Then in Procfile place the following code:
            ```
                web: gunicorn <app name>.wsgi:application
            ```

    - **Heroku in the command line.**
        - Log into Heroku using the terminal.
            ```
                heroku login -i
            ```
        - Temporarily disable the static files until they have been set up on Amazon Aws.
            ```
                heroku config:set DISABLE_COLLECTSTATIC=1 --app <app name>
            ```
            - Use the --app command if you have more than one Heroku app.
        - Then in settings, add Heroku into allowed hosts, and localhost so the project can still be run locally.
            ``` python
                ALLOWED_HOSTS = ["<heroku app name>.herokuapp.com", "localhost"]
            ```
        - Commit changes to Github.
        - Then set up pushing to Heroku
            ```
                heroku git:remote -a <heroku app name>
            ```
        - Then push the project to Heroku
            ```
                git push heroku master
            ```
        - Heroku will now build your app.

    - **Heroku Website**

        - Connect app to GitHub by opening the Deploy section.
        - Searched for the repository.
        - Connect and then enabled Automatic Deploys.
        - This now means that any changes pushed to GitHub will be automatically pushed to Heroku as well.

    - ### Amazon AWS

        - Amazon AWS was used to store both static files and media files.
        - Firstly create an AWS account and work through the sign-up process. Once account is set up set the project up on AWS.

        - **Create a bucket.**

            - #### Create the bucket:
                - Create a new bucket on the AWS S3 service.
                - From the main dashboard search for S3 and then click to get started.
                - Click on the Create bucket button.
                - Give the bucket a name and select region.
                - Then uncheck the block public access and acknowledge that the bucket will now be public.
                - Then click create bucket.
            
            - #### Bucket settings:
                - #### Properties:
                    - Navigate to the bucket properties settings.
                    - Turn on static website hosting.
                    - In the index and error add index.html and error.html.
                    - Click Save.
                - #### Permissions:
                    - Click on the buckets Permissions tabs
                    - Firstly paste in the following cors config:
                        ```
                        [
                            {
                                "AllowedHeaders": [
                                    "Authorization"
                                ],
                                "AllowedMethods": [
                                    "GET"
                                ],
                                "AllowedOrigins": [
                                    "*"
                                ],
                                "ExposeHeaders": []
                            }
                            ]
                        ```
                    - Then in the bucket policy tap, click on generate policy.
                - #### Policy:
                    - Select S3 bucket policy
                    - Add * to the principal field to select all principals
                    - Set the action to get object.
                    - Paste in your ARN which is available on the previous page.
                    - Click, add statement
                    - Then click, generate policy.
                    - Now copy and paste your new policy into the bucket policy.
                    - Add /* onto the end of the resources key
                    - Click Save.
                - #### Access control list:
                    - In the access control list tab set the list objects permission to everyone.
            
        - **Create a User.**
            - To create a user for the bucket search for IAM and select it.
            - Create a Group.
            - Firstly create a group to put user in.
            - Click create a new group and name it.
            - Click through to the end and save the group.
            - Create a policy.
                - In the group click, policy and then, create policy.
                - Select the JSON tab and then import managed policies.
                - Search S3 and select AmazonS3FullAccess and import.
                - In the resources section paste in the arn from before.
                - click through to review the policy.
                - Fill in name and description and then click generate policy.
            - Back in your group click permission and then attach the policy.
            - Find the policy you've just created and attach it.
            
            - Create the User.
            - Select Users from the sidebar and then click, add user.
            - Create a user name and select programmatic access then click next.
            - Then select the group to add user to.
            - Click through to the end and then click create user.
            - ** Make sure to now download the CSV file as it contains the users keys needed to access from our app.**

    - **Heroku Config Vars**
        - #### Set up the following environment variables in your heroku app settings:
            - AWS_ACCESS_KEY_ID = found in the CSV file from the above step
            - AWS_SECRET_ACCESS_KEY = found in the CSV file from the above step
            - DATABASE_URL = generated by Heroku once you created postrgres db in above steps
            - SECRET_KEY = your secret key.
            - STRIPE_PUBLIC_KEY = your stripe public key.
            - STRIPE_SECRET_KEY = your stripe secret key.
            - STRIPE_WH_SECRET = your stripe webhook secret.
            - USE_AWS = 'True' 

            - AWS KEYs can be found in the CSV file from 'Create a User' step in AWS section
            - Your stripe variables can be found on your stripe dashboard.
            - You can generate a Django secret key here. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
---
### Contact: your.marketer1303@gmail.com

#### back to [top](#table-of-contents)