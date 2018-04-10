# LeicaRentals

Rental management system for rental items, customers, and rentals (with
typeahead). Newsletters can also be sent out asynchronously (via task queue) to
signed up customers.

Technology
----------
* Flask
* PostgreSQL
* Celery (with Redis as the broker)
* Bootstrap 4
* Typeahead
* DataTables
* Noty

Screenshots
---
### Index
![index](/screenshots/index.png?raw=true "Index")
### Customers - Details
Customers select a membership and may optionally receive newsletters.
![customers](/screenshots/customers.png?raw=true "Customers")
### Lenses - Index
Pagination, sorting, and searching via DataTables. Inventory is also  managed
(number in stock and number available).
![lenses](/screenshots/lenses.png?raw=true "Lenses")
### Rentals
Lenes may be rented (autocomplete powered via typeahead.js) and returned.
![rentals](/screenshots/rentals.png?raw=true "Rentals")
### Returns
***
![returns](/screenshots/returns.png?raw=true "Returns")
### Newsletters 
Newsletters are sent out to signed up customers only.
![newsletter](/screenshots/newsletter.png?raw=true "Newsletter")
***
![mail](/screenshots/mail.png?raw=true "Mail")

Run
---

Create a database named 'leicarentals', open `config.py` and point the database
URI to your server. You may optionally configure the Celery URI and the mail server
if you would like to send emails. 

After configuring the settings, set the `FLASK_APP` env variable to
leicarentals.py, and install the javascript (e.g `npm install`) and python
dependencies (e.g. `pip install -r requirements.txt`). Be sure to install the
python dependencies using `requirements.txt` located `./leicarentals/`, not
`./leicarentals/requirements/` (I'm working on pruning the dev/prod/test dependencies).

`cd` into `./leicarentals` (if you are not already); then run:
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
