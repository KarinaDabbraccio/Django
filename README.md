# Django

Youtube video: https://youtu.be/NvkHwFEusYg

![presentationDjango](https://user-images.githubusercontent.com/103450865/201493033-1831e850-1927-4124-abdb-286bbec0a48f.png)



1) accounts app:
    - user login, signup;
    - password change;
    - Profile model to have users groups: Manager and User.
    User would receive an alert if the username alredy exists after filling the username field. The default image is assigned and may be changed.
    On the Account page user may see summary of orders, an option to update info, change password (for that, settings.py need to be updated to connect to a valid Google account). If user updates their info, on Django admin their first and last name show up, and new email. By default, users have no access to sales and inventory pages.
    

2) addrecipe app:
    - models: Category - new categories added by admin only;
              Recipe   - new recipes in the defined categories may be seen by all users, added by authorized users;
              Comment  - new comments may be posted for the recipes may be seen by all users, added by authorized users. 

 
3) products app:
    - models: Group, Product - added and changed by admin only, seen by all users. Each Product belongs to one group;
    - availability for the Product is based on the inventory.InventoryItem without expired items.
    

4) orders app:
    - Cart - to keep track of desired Products from session, available for all users;
    - models: OrderedItem, Order - Products from cart may be added/removed from the Order by all users;
    - add to cart at once limited by choice field (1-10 items), by availability of inventory(yes/no);
    - Order may be created only with the items that are available in the inventory;
    - each Order when created has total cost of the inventory ordered for further profit calculation.
    
    
5) inventory app:
    - access only for Manager;
    - models: InventoryItem - shows available Products with cost, amount, expiration date; 
    - LostInventory - inventory that may not be sold, tracking Product and losses (=amount * unit cost);
    - option to delete expired inventory, create new inventory item;
    - inventory item is decreased in quantity/deleted when ordered.
    
   
6) sales app:
    - access for Manager users;
    - shows all orders, quantity of each Product type that was ordered (rating of most popular products);
    - allows to update order as paid, shipped.


7) Django admin 
    - has some customized views for usability. 
   
   
