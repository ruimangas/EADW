from pymongo import MongoClient, IndexModel

def MongoConnection():
	client = MongoClient('localhost', 27017)
	db = client['gathnews']
	db.news.ensure_index('link', unique=True)

	return db

def addNews(link,title,date,document):
	db = MongoConnection()
	newReport = {'link' : link, 'title' : title, 'date' : date, 'document' : document}
	#news.save(newReport) #-> insert or update with upsert
	try:
		db.news.insert_one( newReport )
		return True
	except:
		return False

def getNews(link):
	db = MongoConnection()
	hit = db.news.find_one({"link" : link})

	if hit:
		return hit['title']

def getAllNews():
	db = MongoConnection()
	return db.news.find()
