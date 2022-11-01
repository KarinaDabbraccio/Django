# Django
![image](https://user-images.githubusercontent.com/103450865/199138211-22d1d9d0-c5b2-4d37-b19a-c88e927d30da.png)

1) accounts app:
    - user login, signup;
    - password change;
    - Profile model to have users groups: Manager and User.

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

    
