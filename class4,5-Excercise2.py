user = {}
name = input('What is your name: ')
age = input('What is your age: ')
fav_movies = input('your fav movies seperated by , ').split(',')
fav_songs = input('your fav songs seperated by , ').split(',')

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs

for key, value in user.items():
    print(f"{key} : {value}")