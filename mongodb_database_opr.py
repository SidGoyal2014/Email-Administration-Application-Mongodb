import pymongo

class Database:

    def __init__(self):

        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        self.db = self.myclient["Emailadminapp"]

        self.col = self.db["dataemployee"]

    def insert_data(self,firstname,lastname,department,email,password):

        data = {"FirstName" : firstname, "LastName" : lastname, "Department" : department, "Email" : email, "Password" : password}

        x = (self.col).insert_one(data)

    def delete_data(self,email):

        data = {"Email" : email}

        x = (self.col).delete_one(data)

    def view_full_data(self):

        for x in (self.col).find({},{"_id" : 0,"FirstName" : 1,"LastName" : 1,"Department" : 1,"Email" : 1,"Password" : 1}):
            print(x)

    def update_password(self,email,oldpass,newpass):

        try:

            query = {"Password" : oldpass,"Email" : email}
                
            newquery = {"$set": {"Password" : newpass}}
                
            (self.col).update_one(query,newquery)

            return (True)
        
        except:

            return (False)
