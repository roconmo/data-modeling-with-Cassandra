#DROP TABLES
events_library_table_drop = "DROP TABLE IF EXISTS events_library0"
events_library1_table_drop = "DROP TABLE IF EXISTS events_library1"
events_library2_table_drop = "DROP TABLE IF EXISTS events_library2"


#Create tables events_library
query = "CREATE TABLE IF NOT EXISTS events_library0"
query = query + "(sessionId int, itemInSession int, artist varchar, song varchar, length float, PRIMARY KEY (sessionId, itemInSession))"

query1 = "CREATE TABLE IF NOT EXISTS events_library1"
query1 = query1 + "(userId int, sessionId int, itemInSession int, artist varchar, song varchar, user varchar, PRIMARY KEY ((userid, sessionId), itemInSession))"

query2 = "CREATE TABLE IF NOT EXISTS events_library2"
query2 = query2 + "(song varchar, user varchar, PRIMARY KEY (song))"

#####################################################################
#CREATE QUERIES 
#####################################################################
query_events_library = "select artist, song, length from events_library0 WHERE sessionId = 338 AND itemInSession = 4"
query_events_library1 = "select artist, song, user from events_library1 WHERE userId = 10"
query_events_library2 = "select user from events_library2 WHERE song = 'All Hands Against His Own'"

#####################################################################
# QUERY LISTS
#####################################################################
create_table_queries = [query, query1, query2]
select_table_queries = [query_events_library, query_events_library1, query_events_library2]
drop_table_queries = [events_library_table_drop, events_library1_table_drop, events_library2_table_drop]

