# MACC-Kay!

## Code Institute - Milestone Project 4


## Table of Contents
> - [Overview](#overview)
> - [Description](#description)
> - [Ux](#ux)
> - [User Stories](#user-stories)
> - [Features](#features)
> - [Technologies Used](#technologies-used)
> - [Testing](#testing)
> - [Credits](#credits)
> - [Deployment](#deployment)

 
## Description 
MACC-Kay is an online shop where user can purchase C-Kay's prints, as well as book a tour with him around the hotest spots in London for Street Art. C-Kay takes an photos of London street art done by increadible artist. A user can purchase 10 signed prints by artist out of 50 available. Once user opens the website for the first time, they can see a Home, Captures, Book A Tour pages and My Profile and Cart on the right side of navigation bar (*on the desktop version*). Captures menu breaks down to - "By Artist", "By Price" and "All Captures". My Profile, for non-registered users, breaks down to - "Register" and "Log In". Non-registered user can make purchases and book a tour, however wouldn't be able to save order history or their delivery details. Registered user would be able to see their order history and would't have to fill in delivery details every time they order a print.

---
## UX  

## Strategy
**MACC-Kay** is targeting all age groups of those who interested in street art of London. It's target is to have a simple website where user can easely purchase prints of street art and book a tour around hot spots of London for street art. This website has fluid process of adding captures and a tour to the shopping cart. The easy to follow steps to secure checkout. Additionally, a registered user has the order history and delivery details saved to their profile for easy checkout on their next purchase.

**User Stories**
#### As a First Time User:
- I want the website to have a visually clear purpose.
- I want to be able intuitively browse through the website and easily find all the pages.
- I want the functionality to be simple with engaging content.

#### As a Returning User: 
- I want to learn how to purchase digital street art prints.
- I want to find out how to book a tour with the street artist.
- I want to easily browse the selection of captures and artists.

#### As a Frequent User: 
- As a registered user, I want to be able to view my purchase history and have my delivery details saved.
- As an unregistered user, I am still able to make a purchase and book a tour.
- I want to be able to comprehensively filter the products by price and by artist
- I want to learn more about the artists and have access to their social media accounts.

## Scope
- I have chosen minimalistic design with dark colour accents which matches the vibe of the photographer whose work is sold on this website, as well as it allows users to focus on the beautiful captures of street art on the Captures page.
- The Home page gives a brief information about photographer and links inviting user to visit Captures page & link to the Book A Tour page. On the Captures menu user can find break down to "By Artist", "By Price" and "All Captures", giving option to the user to filter captures in various ways or view all of them. Book A Tour page has form with button to add the tour with preferred time & date to the cart. My Profile for an unregistered user offers to register or logging in and for registered - to view their order history. Cart can be easily accessed on the right side of the navigation by simply clicking on the icon and on the page itself user may view products added as well as their images, and below secure checkout button is featured.
- I have used mixed content of images, buttons and text.

## Structure
This website has different sets of pages/funcionality, dependant on weather user is logged in or not, or if is an admin. 

**First time user four pages are visible:** 
- Home 
- Captures ("By Artist", "By Price" and "All Captures") 
- Book A Tour
- My Profile ("Register" and "Log In")
- Cart

**For registered User another four pages visible:**
- Home
- Captures ("By Artist", "By Price" and "All Captures") 
- Book A Tour
- My Profile ("Order History" and "Log Out")
- Cart (user can save delivery details on checkout)

**For Admin User five pages + Log Out:**
- Home
- Captures ("By Artist", "By Price" and "All Captures") 
- Book A Tour
- My Profile ("Content Management", "Order History" and "Log Out")
- Cart 

## Skeleton
- Home Page: <a href="wireframes/about-wireframe-mcck.pdf" target="_blank" >Home</a>

- Captures Page: <a href="wireframes/captures-wireframe-mcck.pdf" target="_blank" >Captures</a>

- Book A Tour Page: <a href="wireframes/tour-wireframe-mcck.pdf" target="_blank" >Book A Tour</a>

- Cart Page: <a href="wireframes/cart-wireframe-mcck.pdf" target="_blank" >Cart</a>

## Surface
I have used minimalistic design with simple layout. Home page has hero image with photographer avatar image and text box on top of it, apart from it the rest of elements are done in simplistic design with 3 main colours. Text box has transparent dark background with white text. Hero image consist mainly of dark colours with some white details. Captures are images with description in dark grey text underneeth . All the buttons, forms and capture print images are following the main colour scheme.


### Images
- Several images have been used for this website. The hero and avater images at the top of the Home page with the text box with the quotes are designed to draw user's attention to the purpose of the website and text box has links to the Captures & Book A Tour Pages. In the meantime, the "Captures" page mostly consist of images.

-   ### Design
    -   #### Colour Scheme
        - Main colors of the website are - dark gray, black and white. This colourscheme is consistant throughout all pages and is simple and classic without causing any distructions from main purpose of the website.
    -   #### Icons
        - Font Awesome was used for icons which are present on all pages: On the navbar for "My Profile" and "Cart", next to paragraphs of text box as the link to "Book A Tour" page on the Home page.

## Features

#### Navbar
- Logo/website name can be clicked on any page and it will take the user to Home page.
<!-- - Favicon has been added to show on the tab, matching the logo. -->
- On a mobile, the navbar is then collapsed to show the toggler which expands when clicked to display the nav elements as dropdown.

#### Home
- Contains the hero image of C-Kay as DJ in dark colours with C-Kay avatar and nearly transparant black text box with links to Captures and Book A Tour pages.

# Technologies Used
## Languages
+ [HTML5](https://en.wikipedia.org/wiki/HTML5)
+ [CSS3](https://en.wikipedia.org/wiki/CSS)
+ [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
+ [Python3](https://www.python.org/)

## Frameworks and Libraries
+ [Django](https://www.djangoproject.com/)
+ [Pip3](https://pip.pypa.io/en/stable/)
+ [jQuery](https://jquery.com/)
+ [FontAwesome](https://fontawesome.com/)
+ [Google Fonts](https://fonts.google.com/)
+ [Bootstrap](https://getbootstrap.com/)

## All Others
+ [Heroku](https://www.heroku.com/) used to deploy live site.
+ [Stripe](https://stripe.com/en-ie) used for the payments system.
+ [AWS](https://aws.amazon.com/) used for static and media files storage.
+ [GitHub](https://github.com/) used to host repository.
+ [GitPod](https://www.gitpod.io/) used to develop project and organise version control.
+ [TinyPNG](https://tinypng.com/) used to re-size site images. 
+ [Balsamiq](https://balsamiq.com/) used to create wireframes.
+ [RandomKeygen](https://randomkeygen.com/) used to create a strong password for required  `<SECRET_KEY>`.
+ [Lighthouse](https://developers.google.com/web/tools/lighthouse) for performance review.
+ [favicon.io](https://favicon.io/) used to create a site favicon.

## Testing

#### As a First Time User:
**"I want the website to have a visually clear purpose."**
> *The website has a sleek and minimal aesthetic. Appeals to the digital era i.e. digital services.*
 
**"I want to be able intuitively browse through the website and easily find all the pages."**
> *Easy to navigate and locate requirements*

**"I want the functionality to be simple with engaging content."**
> *Chic, functionable and content is engaging. Attractive user interface and edgy designs*

#### As a Returning User: 
- I want to learn how to purchase digital street art prints.
> *Ease of use to purchase art at the click of button.*

- I want to find out how to book a tour with the photographer, who owns the website.
> *Makes booking a tour so simple. Cuts out the need for phone calls and lengthy emails. Very efficient.*

- I want to easily browse the selection of captures and artists.
> *Very clear cut to peruse the art on offer.*

#### As a Frequent User: 
- As a registered user, I want to be able to view my purchase history and have my delivery details saved.
> *Makes it very easy to make a new purchase and all my details are saved on file, for reference.*

- As an unregistered user, I am still able to make a purchase and book a tour.
> *Allows the opportunity to trial the website, without the pressure of committing to signing up. This entices me to register in the future.*

- I want to be able to comprehensively filter the products by price and by artist.
> *Provides transparency to sift through price points from low to high, against different budgets.Gives the opportunity to view a specific artists work entirely.*

- I want to learn more about the artists and have access to their social media accounts.
> *Helpful to learn about the artists' perspectives, backgrounds, inspiration. Allows users to relate to the art work much closer.*


## Credits
- Most of the code taken from walkthrough project Boutique Ado and modified slightly

## Deployment

### Heroku Deployment
This project was deployed through Heroku using the following steps:

#### Requirements and Procfile
Heroku needs to know which technologies are being used and any requirements, so I created files to let it know. Before creating the Heroku app, create these files using the following steps in GitPod:
- In the GitPod terminal, type pip3 freeze --local > requirements.txt to create your requirements file.
- Create your Procfile and insert the following code: web: gunicorn ARTstop.wsgi:application and make sure there is no additional blank line after it.
- Push these files to your repository.

#### Creating Heroku App
- Log into Heroku
- Select 'Create New App' from your dashboard
- Choose an app name (if there has been an app made with that name, you will be informed and will need to choose an alternative)
- Select the appropriate region based on your location
- Click 'Create App'

#### Connecting to GitHub
- From the dashboard, click the 'Deploy' tab towards the top of the screen
- From here, locate 'Deployment Method' and choose 'GitHub'
- From the search bar newly appeared, locate your repository by name
- When you have located the correct repository, click 'Connect'
- DO NOT CLICK 'ENABLE AUTOMATIC DEPLOYMENT'
