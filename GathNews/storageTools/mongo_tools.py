from pymongo import MongoClient

def MongoConnection():
	client = MongoClient('localhost', 27017)
	return client

def addNews(link,title,date,document):
	client = MongoConnection()
	db = client.test
	news = db.news
	newReport = {'link' : link, 'title' : title, 'date' : date, 'document' : document}
	#news.save(newReport) #-> insert or update with upsert
	news.update({"link":link}, newReport, True);

def getNews(link):
	client = MongoConnection()
	db = client.test
	news = db.news
	report = news.find_one({"link" : link})

	if report:
		return report['title']
	else: return "Empty"

def getAllnews():
	client = MongoConnection()
	db = client.test
	news = db.news

	return news.find()