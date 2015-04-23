from pymongo import MongoClient, IndexModel

def MongoConnection():
	client = MongoClient('localhost', 27017)
	db = client.eadw
	db.news.ensure_index('link', unique=True)
	return db

def addNews(link,title,date,document):
	db = MongoConnection()
	newReport = {'link' : link, 'title' : title, 'date' : date, 'document' : document}
	try:
		db.news.insert_one(newReport)
		return True
	except:
		return False

def getNews(link):
	db = MongoConnection()
 	hit = db.news.find_one({"link" : link})

 	if hit: return hit['title']


def getAllNews():
	db = MongoConnection()
	return db.news.find()

def entities_mongo_helper():
	client = MongoClient('localhost', 27017)
	db = client.eadw
	peps = db.namesOfPersons
	return peps

