# Django
1) accounts app:
    - user login, signup
    - password change

2) addrecipe app:
    - models: Category - new categories added by admin only;
              Recipe   - new recipes in the defined categories may be seen by all users, added by authorized users;
              Comment  - new comments may be posted for the recipes may be seen by all users, added by authorized users. 
 
3) products app:
    - models: Group, Product - added and changed by admin only, seen by all users. Each Product belongs to one group;
              Cart - to keep track of desired Products;
              OrderedItem, Order - Products from cart may be added/removed from the Order by all users.
    
