#DROP TABLES
artist_song_by_session_table_drop = "DROP TABLE IF EXISTS artist_song_by_session"
artist_by_session_table_drop = "DROP TABLE IF EXISTS artist_by_session"
song_playlist_session_table_drop = "DROP TABLE IF EXISTS song_playlist_session"


#Create tables
query = "CREATE TABLE IF NOT EXISTS artist_song_by_session"
query = query + "(sessionId int, itemInSession int, artist varchar, song varchar, length float, PRIMARY KEY (sessionId, itemInSession))"

query1 = "CREATE TABLE IF NOT EXISTS artist_by_session"
query1 = query1 + "(userId int, sessionId int, itemInSession int, artist varchar, song varchar, user varchar, PRIMARY KEY ((userid, sessionId), itemInSession))"

query2 = "CREATE TABLE IF NOT EXISTS song_playlist_session"
query2 = query2 + "(song varchar, user_id int, user varchar, PRIMARY KEY (song, user_id))"

#####################################################################
#CREATE QUERIES 
#####################################################################
#Here the Primary Key has two fields: sessionId is the partition key, and itemInSession is clustering key. Partitioning is done by sessionId and within that partition, rows are ordered by the itemInSession.
query_artist_song_session = "SELECT artist, song, length FROM artist_song_by_session WHERE sessionId = 338 AND itemInSession = 4"

#Here the Primary Key has three fields: userId and sessionId are the partition key, and itemInSession is clustering key. Partitioning is done by userId and sessionId and within that partition, rows are ordered by the itemInSession.
query_artist_session = "SELECT artist, song, itemInSession, user, sessionId FROM artist_by_session WHERE userId = 10 AND sessionId = 182"

#Here the Primary Key has two fields: song is the partition key, and userId is clustering key. Partitioning is done by song and within that partition, rows are ordered by the userId.
query_song_playlist_session = "SELECT user FROM song_playlist_session WHERE Song = 'All Hands Against His Own'"

#####################################################################
# QUERY LISTS
#####################################################################
create_table_queries = [query, query1, query2]
select_table_queries = [query_artist_song_session, query_artist_session, query_song_playlist_session]
drop_table_queries = [artist_song_by_session_table_drop, artist_by_session_table_drop, song_playlist_session_table_drop]

