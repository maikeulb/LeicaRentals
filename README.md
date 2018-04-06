# LeicaRentals

Rental management system for managing lenses, customers (powered by DataTables), and lens rentals (with typeahead). Newsletters can also be sent out (asynchronously) to signed up customers.

Technology
----------
* Flask
* PostgreSQL
* Celery (with Redis as the broker)
* Bootstrap 4
* Typeahead
* DataTables

Screenshot
---
### Main
![index](/screenshots/index.png?raw=true "Index")
### Customers - Details (customers can sign up for newsletters)
![customers](/screenshots/customers.png?raw=true "Customers")
### Lenses - Index (pagination, sorting, and searching supported)
![lenses](/screenshots/lenses.png?raw=true "Lenses")
### Rentals (autocomplete powered by typeahead)
![rentals](/screenshots/rentals.png?raw=true "Rentals")
### Returns (lenses can also be returned)
![returns](/screenshots/returns.png?raw=true "Returns")
### Newsletters (sent out to signed up customers only)
![newsletter](/screenshots/newsletter.png?raw=true "Newsletter")
![mail](/screenshots/mail.png?raw=true "Mail")

Run
---
Create a database, open `config.py` and point the database URI to your
server. You may optionally configure the Celery URI and mail server if you would like to send emails. After configuring the settings, set the
`FLASK_APP` env variable to leicarentals.py, and then install the javascript
and python dependencies (e.g. `npm install` and `pip install -r
requirements.txt`). 

`cd` to `./src` and run the following:
```
celery-worker -A leicarentals.celery --loglevel=info (optional)
flask db upgrade
flask seed-db
npm run start (runs the webpack dev server and flask dev server simultaneously)
Go to http://localhost:5000
```
TODO
----
Dockerfile
