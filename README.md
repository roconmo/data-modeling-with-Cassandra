#### Sparkify project with Cassandra

The aim of this project is to create a Apache Cassandra database.

There are 3 files in this project:
	* etl.py MAIN FILE
        There are some functions:
        functions creating_list_filepaths and create_csv: deal with the csv file creating a list of files and creating one single csv file.
        function populate_tables receives the current session and a path and populates the database tables.
        function select_tables: given a session, retrieves the asked values
    
    	* cql_queries.py:
        All the queries to create, and delete tables.
    	* create_tables.py
        The script to create cluster, set the keyspace, session and databases.

#### How to run the solution:
```
$ python create_tables.py
```
To create custom tables and 
```
$ python etl.py
```
To populate the tables and show the info asked.

