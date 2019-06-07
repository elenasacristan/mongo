import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Please select an option: ")
    return option

def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    print("")
    
    try:
        document = coll.find_one({'first':first.lower(), 'last':last.lower()})
    except:
        print('Error accessing the database')
        
    if not document:
        print('')
        print('Error, Not results found')
    
    return document

def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter your date of birth > ")
    gender = input("Enter your gender > ")
    hair_colour = input("Enter you hair colour > ")
    occupation = input("Enter your occupation > ")
    nationality = input("Enter your nationality > ")
    
    new_doc = {'first':first.lower(), 'last':last.lower(), 'dob':dob, 'gender': gender.lower(), 'hair_colour':hair_colour.lower(), 'occupation':occupation.lower(), 'nationality':nationality.lower()}
    
    try:
        coll.insert(new_doc)
        print("Record added!")
    except:
        print("Eror connection to the database")

def find_record():
    doc = get_record()
    
    if doc:
        for k,v in doc.items():
                if k != "_id":
                    print(k + " : " + v)

def edit_record():
    doc = get_record()
    
    if doc:
        doc_update = {}
        try:
            for k,v in doc.items():
                if k != "_id":
                    doc_update[k] = input(k + "[" + v + "] >" )
            if doc_update[k]=="":
                doc_update[k] = v
            coll.update_one(doc,{'$set':doc_update})
        except:
            print("Error connecting to the database")
    
def delete_record():
    doc = get_record()
    
    if doc:
        print("")
        for k,v in doc.items():
                if k != "_id":
                    print( k.capitalize() + " : " + v.capitalize() )
        print("")
        
        confirmation = input("Is this the document you want to delete? y/n >")
        
        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Record deleted!")
            except:
                print("Error connecting to the database")
        else:
            print("Record not deleted")
            
        


def main_lopp():
        while True:
            option = show_menu()
        
            if option == "1":
               add_record()
            elif option == "2":
                find_record()
            elif option == "3":
                edit_record()
            elif option == "4" :
                delete_record()
            elif option == "5":
                conn.close()
                break
            else:
                print("Wrong option, please try again.")
            print("")
        
#we call the funcion now with MONGODB_URI as argument
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

main_lopp()
