# Django ORM isolated **template**

Django ORM isolated from the framework to be used in other projects independently

* You can interact with the database **through the Django ORM without starting a server**.
* In this example we have define a single model called **Person** with a single field (**name**).
* We have created a **sqlite3** database and configure the connexion in the _manage.py_ file, this can be easily substitute for the database of your choice. [Here](https://docs.djangoproject.com/en/4.0/ref/databases/) es the documentation about how to do it properly.
* There are two scripts included:
	* *populate_db.py*: This script generate elements in the database corresponding to the Person model.
	* *print_all_persons_name.py*: This script prints the _id_ and the _name_ of all the elements in the table Person in the database.

## Instructions

* First create a virtual environment `python3 -m venv .venv`. Note that this template has been developed using **python 3.9.12**.
* Activate (`source .venv/bin/activate`) and install the packages listed in *requirements.txt* (`pip install -r requirements.txt`).
* The *utils* forlder contains a single script that will generate a sqlite database as the one included in the project.	Execute it to create a database (`python db_sqlite_creation.py`). 
* Now we have to generate the migrations (this will be necessary each time we do changes in the models): `python manage.py makemigrations db`.
* Once the migrations are generated, we need to apply them to the database: `python manage.py migrate db`.
* Now we can interact with the dabatase with the two scripts included as an example, for instance we can create registers with `python populate_db.py`.

***

#### Contribute:

* If you want to contribute do not hesitate in open a PR, I'll reviewed asap.
* If you have any comment, question or suggestion contact me, you can find me on Twitter [@mgijon94](https://twitter.com/mgijon94).
