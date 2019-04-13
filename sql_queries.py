# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE  IF EXISTS users"
song_table_drop = "DROP TABLE  IF EXISTS songs"
artist_table_drop = "DROP TABLE  IF EXISTS artists"
time_table_drop = "DROP TABLE  IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id SERIAL PRIMARY KEY, 
                                start_time varchar,
                                user_id varchar, 
                                level varchar, 
                                song_id varchar , 
                                artist_id varchar ,
                                session_id varchar, 
                                location varchar, 
                                user_agent varchar)
                                """)

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                            user_id varchar PRIMARY KEY, 
                            first_name varchar NOT NULL, 
                            last_name varchar NOT NULL, 
                            gender varchar NOT NULL, 
                            level varchar NOT NULL
                            )""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                            song_id varchar PRIMARY KEY, 
                            title varchar NOT NULL, 
                            artist_id varchar NOT NULL,
                            year int NOT NULL, 
                            duration float NOT NULL
                            )""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                              artist_id varchar PRIMARY KEY, 
                              artist_name varchar NOT NULL,
                              artist_location varchar NOT NULL,
                              artist_latitude real NOT NULL,
                              artist_longitude real NOT NULL
                          )""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                            start_time varchar PRIMARY KEY, 
                            hour varchar NOT NULL, 
                            day varchar NOT NULL,
                            week varchar NOT NULL,
                            month varchar NOT NULL,
                            year varchar NOT NULL,
                            weekday varchar NOT NULL
                        )""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            VALUES(DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s) 
                            """)

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                        VALUES(%s, %s, %s, %s, %s) 
                        ON CONFLICT (user_id)
                        DO UPDATE SET (first_name, last_name, gender, level) = (EXCLUDED.first_name, EXCLUDED.last_name, EXCLUDED.gender, EXCLUDED.level)
                        """)

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
                        VALUES(%s, %s, %s, %s, %s) 
                        ON CONFLICT (song_id)
                        DO UPDATE SET (title, artist_id, year, duration) = (EXCLUDED.title, EXCLUDED.artist_id, EXCLUDED.year, EXCLUDED.duration)
                    """)

artist_table_insert = ("""INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
                        VALUES(%s, %s, %s, %s, %s) 
                        ON CONFLICT (artist_id)
                        DO UPDATE SET (artist_name, artist_location, artist_latitude, artist_longitude) = (EXCLUDED.artist_name, EXCLUDED.artist_location,
                            EXCLUDED.artist_latitude, EXCLUDED.artist_longitude)
                        """)


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)\
                        VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING""")

# FIND SONGS

song_select = ("""SELECT songs.song_id, artists.artist_id 
                  FROM songs 
                      INNER JOIN artists 
                      ON songs.artist_id = artists.artist_id 
                      WHERE title = %s 
                      AND   artist_name = %s 
                      AND duration = %s
                """)




# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
 