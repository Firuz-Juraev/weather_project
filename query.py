import sqlite3
import settings 


conn = sqlite3.connect(settings.DB_FILE_NAME)  
c = conn.cursor()

#c.execute("""CREATE TABLE cities(
#        city_id INTEGER PRIMARY KEY, 
#        name TEXT, 
#        lat REAL, 
#        lon REAL);""")


#c.execute("""CREATE TABLE weather(
#        city_id INTEGER, 
#        time INTEGER, 
#        summary TEXT, 
#        windSpeed REAL, 
#        temperature REAL, 
#        uvIndex INTEGER, 
#        visibility REAL, 
#        CONSTRAINT fk_departments
#        FOREIGN KEY (city_id)
#        REFERENCES cities(city_id));""")


#c.execute("INSERT INTO cities (city_id, name, lat, lon) VALUES('1', 'Samarkand', '39.65417', '66.95972');") 
#c.execute("INSERT INTO cities (city_id, name, lat, lon) VALUES('3', 'Los Angeles', '34.052235', '-118.243683');") 
#c.execute("INSERT INTO cities (city_id, name, lat, lon) VALUES('4', 'Moscow', '55.751244', '37.618423');") 
#c.execute("INSERT INTO cities (city_id, name, lat, lon) VALUES('5', 'London', '51.509865', '-0.118092');")
#c.execute("INSERT INTO cities (city_id, name, lat, lon) VALUES('6', 'New York', '40.730610', '-73.935242');")

c.execute("select * from weather;")

print (c.fetchall())

conn.commit()

conn.close()

# weather: time, summary, windSpeed, temperature, uvIndex, visibility  