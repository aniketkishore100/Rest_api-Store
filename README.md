## REST-API using FLask and sqlite
This is an example of an simple API of a store which folllows the RESTful architecture. 
It consists of a venv and a code folder. To start with the api, you have to activate the virtual environment by typing in cmd "venv/Scripts/activate which activates your virtual_env.
The code folder consists of all the python files.
The project uses Flask and sqlite for its functioning.
The project can run by first creating a database file by running the "python create_tablees.py" which creates a file 'data.db'
The next step is to run the Api by typing "python app.py" through the same directory where you have created the data.db.
The Api will then run on the port "5000" and will allow the user to Sign up, Log in, Post the items with price and Get the item_listof the store ,also the api consists of another GET endpoint which allows the user to access a specific item of the store.
