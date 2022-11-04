# Django
![image](https://user-images.githubusercontent.com/103450865/199138211-22d1d9d0-c5b2-4d37-b19a-c88e927d30da.png)


User views have desktop and mobile versions. 

1) accounts app:
    - user login, signup;
    - password change;
    - Profile model to have users groups: Manager and User.
    User would receive an alert if the username alredy exists after filling the username field. The default image is assigned and may be changed.
    On the Account page user may see summary of orders, an option to update info, change password (for that, settings.py need to be updated to connect to a valid Google account). If user updates their info, on Django admin their first and last name show up, and new email. By default, users have no access to sales and inventory pages.
    
    ![image](https://user-images.githubusercontent.com/103450865/200011375-1abad45d-72a2-48e4-bdb8-3cccc269d652.png)
    
    ![image](https://user-images.githubusercontent.com/103450865/200013496-3e073007-d42f-4392-8c65-9d395e7b6fa8.png)
    
    ![image](https://user-images.githubusercontent.com/103450865/200021638-7f2517ff-8081-4088-90bd-b94d2a599d69.png) 


2) addrecipe app:
    - models: Category - new categories added by admin only;
              Recipe   - new recipes in the defined categories may be seen by all users, added by authorized users;
              Comment  - new comments may be posted for the recipes may be seen by all users, added by authorized users. 
              
   ![image](https://user-images.githubusercontent.com/103450865/200020346-8ce67181-3315-444c-bc51-bdec19de913b.png)
        
   ![image](https://user-images.githubusercontent.com/103450865/200019495-8e53864b-22c0-4bca-9bec-88e8b79c8c2b.png)

   ![image](https://user-images.githubusercontent.com/103450865/200020577-33f1ee08-3ab9-4d89-913d-e1578ee44fb6.png)

 
3) products app:
    - models: Group, Product - added and changed by admin only, seen by all users. Each Product belongs to one group;
    - availability for the Product is based on the inventory.InventoryItem without expired items.
    
     ![image](https://user-images.githubusercontent.com/103450865/199138381-5fad85d5-4f15-4723-947c-095b189f7920.png)
     
     ![image](https://user-images.githubusercontent.com/103450865/199138496-a98fdcc1-834c-435f-84ad-82696f3ec99e.png)



4) orders app:
    - Cart - to keep track of desired Products from session, available for all users;
    - models: OrderedItem, Order - Products from cart may be added/removed from the Order by all users;
    - add to cart at once limited by choice field (1-10 items), by availability of inventory(yes/no);
    - Order may be created only with the items that are available in the inventory;
    - each Order when created has total cost of the inventory ordered for further profit calculation.
    
    
![image](https://user-images.githubusercontent.com/103450865/199138606-adca7a59-c1e0-43c3-a1e3-99254e597456.png)

![image](https://user-images.githubusercontent.com/103450865/200015450-73cb0849-0565-480c-9793-d143ad9ca53e.png)


5) inventory app:
    - access only for Manager;
    - models: InventoryItem - shows available Products with cost, amount, expiration date; 
    - LostInventory - inventory that may not be sold, tracking Product and losses (=amount * unit cost);
    - option to delete expired inventory, create new inventory item;
    - inventory item is decreased in quantity/deleted when ordered.
    
![image](https://user-images.githubusercontent.com/103450865/199138674-7a644011-263a-4cea-b6cf-27a0fa1e41ff.png)

![image](https://user-images.githubusercontent.com/103450865/200022115-f23b5020-5ab5-4469-8288-2aedcc57d496.png)



   
6) sales app:
    - access for Manager users;
    - shows all orders, quantity of each Product type that was ordered (rating of most popular products);
    - allows to update order as paid, shipped.
    
![image](https://user-images.githubusercontent.com/103450865/199138760-6fadff22-8389-4088-9fc3-cd503af869d7.png)

7) Django admin 
    - has some customized views for usability. 
   
![image](https://user-images.githubusercontent.com/103450865/200023097-d9097524-387c-473f-9b7b-cfe518997acc.png)


    
