# Fresh

* Goal: Nowadays barbers work at barbershops or anywhere else they can set up shop (i.e their/your apartment). Fresh is allowing Barbers to stay on the radar of potential customers. We give people the ability to search for barbers in their neighborhood by location and name.

## Wireframes

Also found here while publically available https://trello.com/b/zAkZUSTd/project-3

## User Stories
- A barber can have a profile so that people can find them online and leave a review of the experience
- A user can browse anonymously so that they see the barber options
- A user can sign-up/in so that they are able to save their user data
- A user can leave a barber review so that other users can read about the experience
- A user can edit a barber review so that they can modify reviews given for barbers
- A user can delete a barber review so that they can ensure their comment isn't incorporated into the barber review
- A user can view a map of local barbers so that they can get better context regarding what barbers are in their neighborhood
- A user can search for barbers by name and location so that they can find the best barber for their needs
- A user can pay through the app so that they don't have to pay with cash or another payment system other than stripe
Also found here while publically available https://trello.com/b/zAkZUSTd/project-3

## Heroku Link
https://fresh-barbers.herokuapp.com

## Technologies Used

- Flask
- Flask Login
- Javascript
- HTML5
- CSS3
- Peewee
- Sqlite (initially)
- Postgres (for production)
- Bootstrap
- FlexBox
- Google MAP API
- Stripe Payment API

## Design and Methodologies
- Conducted a small survey of local barbers to ask about pain points and incorporate feedback into MVP
- ERDs (Referenced Data)
- Wireframing
- Agile Development/Srum/Sprints

## Existing Features

- User can securely login via Flask Login
- A user can leave a barber review so that other users can read about the experience
- A user can sign-up/in so that they are able to save their user data
- A user can browse so that they see barber options
- User can filter for barbers by name and neighborhood
- User can add only after login
## Core Technical Requirements
Requirement met - Flask: Use Flask as the core framework for Python.
Requirement met - PostgreSQL: Use PostgreSQL for your database in development and production.
Requirement met - Data Models Include at least two data models with associations.
Requirement met - Data Validation: Your application should validate incoming data before entering it into the database.
Requirement met - Error Handling: Forms in your application should also validate data, handle incorrect inputs, and provide user feedback on the client side.
Requirement met - Views: Use Jinja templates.
Requirement pending - Home & About Pages: Create a landing page (homepage) that clearly explains your app's value proposition and guides the user through the "get started" funnel. Create an about page that includes photos and brief bios of your team members.
Requirement met - User Experience: Ensure a pleasing and logical user experience. Use a framework like Bootstrap, Bulma, or Skeleton to enhance and ease your CSS styling.
Requirement met - Responsive Design: Make sure your app looks great on a phone or tablet.
Requirement met - Heroku: Deploy your app to Heroku. Ensure no app secrets are exposed. Do not commit secret keys to GitHub!

## Flexible Technical Requirements
Your app should have 3 out of the 5 following options:

Requirement met - User Login Make sure you have authentication and authorization.
Requirement met - AJAX Use AJAX to communicate with the server without reloading the page when appropriate.
External APIs Use a third-party API back-end package to integrate third-party data into your app.
JavaScript & jQuery: Add dynamic client-side behavior with event-driven functionality.
User-Friendly URLs: Make pretty URLs that don't expose database IDs.

## Endpoints

- API Endpoints
1. '/'
  Home Page
2. '/register'
  Register a User
3. '/login'
  User Login 
4. '/logout'
  User Logout
5. '/new_post'
  POST Reviews
6. '/stream'
  GET Live stream of user thoughts and concerns, unrelated to specific barbers. Live tweeting basically
7. '/barbers'
  GET
8. /barbers/<barberid>/reviews/<id>/delete
  DELETE request to delete barber review
9. /barbers/<barberid>/reviews/<id>/edit
  PUT request to edit barber review
8. '/pay'
  Pay Barber with Stripe


## Planned Features
- Calendar on front end for barber booking (Calendly api pull)
- Barber UX to add New Barbers into Database (allow barbers to create a profile)

## Code Snippets

https://docs.google.com/presentation/d/1wCmpj2-Hkzu6t9kcIpD2TMcSOnT8DfZuHb8rjT_hveY/edit#slide=id.g548456ec7d_0_7

## Contributor GitHubs
- Paris: https://github.com/paristechprofile
- Chike: https://github.com/Chike17
- Darnell: https://github.com/rightbrainpapi

