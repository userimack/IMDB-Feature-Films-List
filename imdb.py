from bs4 import BeautifulSoup
import urllib


response = urllib.urlopen("http://www.imdb.com/search/title?at=0&release_date=2005,2015&sort=moviemeter&title_type=feature&user_rating=1.0,10")
readHtml = response.read() # reading the source from the url

soup = BeautifulSoup(readHtml,"html.parser")

tableClassResults = soup.find("table",{"class":"results"})
	
for row in tableClassResults.find_all('tr'):
	print("\n")
	title = row.find_all("td",{"class":"title"})
	for titletd in title:
		print("Title: "+titletd.a.string)
		print("Year: "+titletd.find(class_="year_type").string)
		genreClass = titletd.find(class_= "genre")
		print("Genries: ")
		for eachGenre in genreClass.find_all('a'):
			print("\t"+eachGenre.string)
		print("Run Time: "+titletd.find(class_="runtime").string)
		rating_rating = titletd.find(class_="rating-rating")
		ratingValue = rating_rating.find(class_="value")
		print("Rating: "+ratingValue.string)

