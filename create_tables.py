from cql_queries import create_table_queries, drop_table_queries

def create_cluster():
    # This should make a connection to a Cassandra instance your local machine 
    # (127.0.0.1)
    from cassandra.cluster import Cluster
    cluster = Cluster()
    # To establish connection and begin executing queries, need a session
    session = cluster.connect()
    
    return session
            
def create_keyspace():
    '''function that creates the database and set the keyspace. Returns the current session'''  
    session = create_cluster()
    session.execute("CREATE KEYSPACE IF NOT EXISTS udacity WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }")
    session.set_keyspace('udacity')
                    
    return session       

def create_database():
    """
    - Creates and connects to the db_name database
    - Returns the session
    """
    session = create_keyspace()
    return session

def create_tables(session):
    """
    Creates each table using the queries in 'create_table_queries' list. 
    Args:
        session: current session
    """
    for query in create_table_queries:
        session.execute(query)
        

def drop_tables(session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        session.execute(query)
        
def main():
    """
    - Drop (if exists) and creates the sparkify database. 
    - Establishes connection with the sparkify database and gets cursor to it.  
    - Drops all the tables.  
    - Creates all tables needed. 
    - Finally, closes the connection. 
    """
    session = create_database()
    
    drop_tables(session)
    create_tables(session)

    

if __name__ == "__main__":
    main()
