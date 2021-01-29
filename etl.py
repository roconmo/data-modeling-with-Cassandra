import pandas as pd
import cassandra
import re
import os
import glob
import json
import csv
from cql_queries import *
from create_tables import *

def creating_list_filepaths():
    '''
    Function that creates a list of files 
    Returns: a file path list
    '''
    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):

    # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root,'*'))
        
    return file_path_list
        
def create_csv():
    '''
    Function that creates a single csv file with 
    '''
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = [] 
    
    file_path_list = creating_list_filepaths()

    # for every filepath in the file path list 
    for f in file_path_list:

    # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)

     # extracting each data row one by one and append it        
            for line in csvreader:
                full_data_rows_list.append(line) 

    # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
    # Apache Cassandra tables
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                    'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
            
def populate_tables(session, file):
    '''
    Function that populate the tables with the values from the csv file
    Args:
        session: current session
        file: path to the csv file
    '''
    query_tables = (
        ("artist_song_by_session"), ("artist_by_session"), ("song_playlist_session")
    )
    query_val = (
        ("sessionId, itemInSession, artist, song, length"),
        ("userId, sessionId, itemInSession, artist, song, user"),
        ("song, user_id, user")
    )
    query_value = (
        ("%s, %s, %s, %s, %s", "%s, %s, %s, %s, %s, %s", "%s, %s, %s")
    )
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        
        for line in csvreader:
            query_vect = (
                (int(line[8]), int(line[3]), line[0], line[9], float(line[5])), 
                (int(line[8]), int(line[10]), int(line[3]), line[0], line[8],"{} {}".format(line[1], line[4])), 
                (line[9], int(line[8]), "{} {}".format(line[1], line[4]))
            )
            for i in range(2):
                #Insert data into tables
                query = ("INSERT INTO {} ({})".format(query_tables[i], query_val[i]))
                query = query + " VALUES ({})".format(query_value[i])
                session.execute(query, query_vect[i])  
                
def select_values(session):
    '''
    Function that retrieves the asked select
    Args:
        session: current session
    Prints the results.
    '''
    
    for i in range(3):
        rows = session.execute(select_table_queries[i])
        print("The query {} has the following results:".format(select_table_queries[i]))
        for row in rows:
            if i==0:
                print(row.artist, row.song, row.length)
            elif i==1:
                print(row.artist, row.song, row.itemInSession, row.user)
            else:
                print(row.user)
    
def main():
    """
    - creates csv files. 
    - Establishes connection with the sparkify database and gets session to it.  
    - Populate the tables 
    - Finally, closes the connection. 
    """
    
    create_csv()
    session = create_keyspace()

    populate_tables(session, 'event_datafile_new.csv')
    select_values(session)
    session.shutdown()
    #cluster.shutdown()

if __name__ == "__main__":
    main()
