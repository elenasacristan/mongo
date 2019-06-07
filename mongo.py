import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mondo is connnected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


#we call the funcion now with MONGODB_URI as argument
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

    #PRINT records
#documents = coll.find()

#for doc in documents:
#    print(doc)

     #INSERT records  

# new_doc = {'first': 'douglas','last': 'adams','dob': '23/03/1983','hair_colour': 'grey','occupation': 'writer','nationality': 'english'}

# coll.insert(new_doc)

# documents = coll.find()

# for doc in documents:
#     print(doc)
    
     #INSERT more than 1 record  

# new_docs = [{'first': 'douglas','last': 'adams','dob': '23/03/1983','hair_colour': 'grey','occupation': 'writer','nationality': 'english'},
# {'first': 'tere','last': 'martin','dob': '21/03/1983','hair_colour': 'black','occupation': 'it','nationality': 'irish'},
# {'first': 'elena','last': 'sanchez','dob': '22/03/1983','hair_colour': 'blonde','occupation': 'nurse','nationality': 'french'},
# {'first': 'susana','last': 'perez','dob': '20/03/1983','hair_colour': 'grey','occupation': 'student','nationality': 'spanish'},]

# coll.insert_many(new_docs)

# documents = coll.find()

# or doc in documentfs:
#     print(doc)

    #FIND EXPECIFIC DATA

# documents = coll.find({'nationality':'spanish'})

# for doc in documents:
#      print(doc)


    #DELETE DATA DATA

# coll.remove({'first': 'tere'})
# documents = coll.find()

# for doc in documents:
#      print(doc)


    #UPDATE DATA ONE

# coll.update_one({'first': 'elena'},{'$set': {'last':'sacris'}})
# documents = coll.find()

# for doc in documents:
#      print(doc)
     
    #UPDATE DATA more than ONE

coll.update_many({'nationality': 'english'},{'$set': {'hair_colour':'maroon'}})
documents = coll.find({'nationality': 'english'})

for doc in documents:
     print(doc)