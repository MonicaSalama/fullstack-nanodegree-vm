Item Catalog:
  An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system.
  Registered users will have the ability to post, edit and delete their own items.


Getting Started:
  Clone https://github.com/MonicaSalama/fullstack-nanodegree-vm
  Go to directory: vagrant/Catalog
  Run using python project.py
  You May now access the application from your browser using the url : http://localhost:8000/

Prerequisites:
  Python 2.7
  framework : Flask
  Database : postgreSQL
  sqlalchemy

Application Demonstration:

  Authentication : You may login using your google account
    Siginig in gives you the privilege to add a category, add items.
    Also on the right you will  a logout button.

  Authorization :
    You are only authorized to edit or delete items you have created with your account.

  Home page:
    Url : http://localhost:8000/
    A list of all the items in the catalog.
    By clicking on an item, you are redirected to a page to show you all the item details.
    If you are signed in, and you are the owner of the item, you will be given the privilege to edit or delete the item.

  Categories:
    Url : http://localhost:8000/category
    On the left side of the page there is a button for showing all categories.
    By just clicking on, a list of all the categories in the system will be shows.
    Also, if you are signed in you will be given the privilege to create a new category.
    You may also click on a category which will redirect you to a page where all the items
    belonging to that category will be shown.


JSON endpoints:
  - http://localhost:8000/catalog.json
    Details of all the categories along with its items.

  - http://localhost:8000/category.json
    Details of all the categories listed in the system.

  - http://localhost:8000/category/'category_id'/items.json
    'category_id' should be replaced with the actual id.
    Details of all the items corresponding to this category_id.

  - http://localhost:8000/items.json
    Details of all the items in the catalog.

  - http://localhost:8000/'item_id'/item.json
    'item_id' shoud be replaced with the id of the item.
     Details of a specific item

Finally, Hope you will enjoy using the App!
