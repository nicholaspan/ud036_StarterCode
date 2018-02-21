#!/usr/bin/python 

import media
import urllib
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "Talks about Andy and his journey into College", 
	"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-wt2it4_fbf729c8.jpeg?region=0,0,300,450", 
	"https://www.youtube.com/watch?v=JcpWXaA2qeg")

print(toy_story.storyline)

avatar = media.Movie("Avatar", "Extraterrestrial beings and following their lives",
	"http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

inception = media.Movie("Inception", "Tracks a world where you can incept dreams",
	"http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
	"https://www.youtube.com/watch?v=8hP9D6kZseM")

#inception.show_trailer()

gone_girl = media.Movie("Gone Girl", "A couple who falls out of love and things take a dark turn",
	"http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
	"https://www.youtube.com/watch?v=8hP9D6kZseM")

movies = [toy_story, avatar, inception, gone_girl]
fresh_tomatoes.open_movies_page(movies)

