###Catalog App

A basic catalog app built with Flask, sqlalchemy, and postgresDB. Dependencies can be found in the requirements.txt file. Dependencies can be installed via `pip install -r requirements.txt`. 

###Functionality
Users can optionally create an account via Google+ signin to have access for creating items and categories. Unauthenticated users can still browse the catalog by selecting a category which then shows the items in that category. Clicking on an item will show details about that item. Authenticated users can create items with various data fields like, price, description, title, sku, image url etc. Authenticated users can also create new categories. Users can edit the items and categories that they create. 


### Ubuntu setup:

1. To access the server (if you have the key: provider to review in reviewer notes): ssh -i ~/.ssh/udacity_key.rsa root@35.164.5.105 -p2200
2. To see the app in action, visit this URL in your broswer:  http://ec2-35-164-5-105.us-west-2.compute.amazonaws.com/
3. Dependencies required: apache2 webserver, mod_wsgi, sqlalchemy, psycopg2, flask, postgres db. Directions are easily found by googling the resepctive installs.
4. Postgres db is setup as follows: db name=catalog, db username/role="catalog" with password="bcr0072", Ubuntu username="catalog". The db console can be accessed by changing user to "catalog" `$ su catalog` and then `$ psql` into the console as the "catalog" user. 
5. mod_wsgi setup: the wsgi file name is "catalog.wsgi" and found in /var/www/html. The virutal host config must be changed to reflect the new file name. `sudo nano /etc/apache2/sites-enabled/000-default.conf` and add the following line at the end of the <VirtualHost *:80> block, right before the closing </VirtualHost>  .... `WSGIScriptAlias / /var/www/html/catalog.wsgi`  . Then Don't forget: `sudo apache2ctl restart` to activate the config change.
6. To setup the app:
....navigate to the app root dir:
  - Create the database by running: `python database_setup.py`
  - Optional. To populate the db with a bulk list of items you can modify the `catalog_items.py` file and then run it: `python catalog_items.py`
7. For debugging, access the apache2 error log at: `cat /var/log/apache2/error.log`
