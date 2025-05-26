# code-challenge-2
## project Overview
this project models the relationship between Authors, Articles, and Magazines with data persisted in an SQLite database.

- An Author can write many Articles.
- A magazine can publish many Articles.
- An Article belongs to both an Author and a Magazine.
- The Author-magazine relationship is many-to-many via Articles.

## Setup Instructions

### Environment Setup
You will use Pipenv. 
###  Using Pipenv
``` bash 
pipenv install pytest sqlite3
pipenv shell

### Database Setup
run the following script to create tables and seed initial data:

PYTHONPATH=. python scripts/setup_db.py

-  the script executes the SQL schema in lib/db/schema.sql and inserts sample data.

PYTHONPATH=. python -m lib.db.seed
calls the seed() function.
connects to the database.
insert data into authors, articles, and magazines.
print a success message.


PYTHONPATH=. python scripts/run_queries.py
 it outputs a one-to-many relationships:
 -one author -many articles
 -one article - one magazine

 it also demonstrate the many-to-many relationship via articles:
  -one author - multiple magazines
  - one magazine - multiple authors
it shows contributors to tech today.
it shows authors contributing more than 2 articles to tech today

## Project structure
code-challenge/
├── lib/ # Main code directory
│ ├── models/ # Model classes
│ │ ├── __init__.py # Makes models a package
│ │ ├── author.py # Author class with SQL methods
│ │ ├── article.py # Article class with SQL methods
│ │ └── magazine.py # Magazine class with SQL methods
│ ├── db/ # Database components
│ │ ├── __init__.py # Makes db a package
│ │ ├── connection.py # Database connection setup
│ │ ├── seed.py # Seed data for testing
│ │ └── schema.sql # SQL schema definitions
│ ├── controllers/ # Optional: Business logic
│ │ └── __init__.py # Makes controllers a package
│ ├── debug.py # Interactive debugging
│ └── __init__.py # Makes lib a package
├── tests/ # Test directory
│ ├── __init__.py # Makes tests a package
│ ├── test_author.py # Tests for Author class
│ ├── test_article.py # Tests for Article class
│ └── test_magazine.py # Tests for Magazine class
├── scripts/ # Helper scripts
│ ├── setup_db.py # Script to set up the database
│ └── run_queries.py # Script to run example queries
└── README.md # Project documentation