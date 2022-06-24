# Django
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
    - add to cart as desired;
    - Order may be created only with the items that are available in the inventory.

5) inventory app:
    - access only for Manager;
    - models: InventoryItem - shows available Products with cost, amount, expiration date; 
    - LostInventory - inventory that may not be sold, tracking Product and losses (=amount * unit cost);
    - option to delete expired inventory;
    - inventory item is decreased in quantity/deleted when ordered.
   
6) sales app:
    - for now only shows all orders, quantity of each Product ordered.

    
