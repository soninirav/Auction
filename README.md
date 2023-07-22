# Auction App

Welcome to the Auction Web App - a dynamic platform powered by Django framework! Engage in exciting auctions with features like creating listings, closing listings, managing watchlists, placing bids, and engaging in discussions through comments. Seamlessly sign in or sign up to explore a world of competitive bidding and connect with other auction enthusiasts. Experience the online auctions with user-friendly and feature-rich application!

### Home Page 
Where you can explore a comprehensive display of all items currently available for auction. Browse through a diverse array of captivating items and discover your next bidding opportunity on this centralized platform.
### Sign up 
Sign up page for users.
### Login 
Login Page for users.
After login users will be redirected to Active Listing page.
###Create Listing 
The page offers users the ability to auction their items by filling out a simple form, providing product images, descriptions, start bidding prices, and selecting the appropriate category.
### Categories
Where the currently logged-in user gains exclusive access to all available auction items, effortlessly filtered by categories.
###Watchlist
Users can track their watchlisted items here.
### Logout 
Logout functionality for users.

### APIs

`/` : Return the home page

`login/` : Logging In

`logout/` : Logging Out

`register/` : Save user details to database

`category/` : Returns all active listings on website

`add_to_watchlist/<int:listing_id>/` : Add selected item to watchlist for currently logged in user

`remove_from_watchlist/<int:listing_id>/` : Remove selected item to watchlist for currently logged in user

`watchlist/` : Returns all watchlisted items for currently logged in user

`category/<int:id>/` : Returns all items having categoryId=id

`listing/create/` : Allows users to place their items for auction

`listing/<int:listing_id>/` : Returns details of requested item having comments, bid details, updated price etc.

`listing/<int:listing_id>/close/` : User can take down the product if he/she is satisfied with current bid price.

## **Demo**

#### YouTube Link: https://www.youtube.com/watch?v=t2-m9cCHtb8

![demoVideo](https://github.com/soninirav/Notes/blob/master/notesDemo.gif)
