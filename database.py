import sqlite3

mod = sqlite3.connect('moviestable.db')

cor = mod.cursor()


cor.execute(""" CREATE TABLE moviess (
	movie_name text,
	actor_name text,
	actress_name text,
	year_released int,
	director_name text
	)""")

many_movies = 	[
			('Thor', 'Chris hemsworth', 'Natalie Portman', '2011', 'Kenneth Branagh'),
			('Captain America', 'Chris Evans', 'Hayley Atwell', '2011', 'Joe Johnston'),
			('Karma', 'jackie shroff', 'Sridevi', '1986', 'Subhash Ghai'),
			('Kashmir Files', 'Darshan Kumar', 'Pallavi Joshi', '2022', 'Vivek Agnihotri'),
			('Student of the year', 'Siddarth Malhotra', 'Alia Bhatt', '2016', 'Karan Johar'),
		]

cor.executemany("INSERT INTO movie VALUES (?,?,?,?,?)", many_movies)

cor.execute("SELECT * FROM movie")

items = cor.fetchall()

for item in items:
	print(item)


cor.execute("SELECT * FROM movie WHERE actor_name='Chris hemsworth'")
print("Your search for actor is")
print(cor.fetchone())

mod.commit()

mod.close()
