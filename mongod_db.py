from pymongo import MongoClient
import pprint

class dbase():
    #Class Attributes
    client = MongoClient()

    def __init__(self, database="pkt_captures", collections="pkts"):
        """ MongoDB constructor.

        This construtor will gets database name and collections name from the provided arguments.
        """
        # Instance Attributes
        self.db_name = database
        self.col_name = collections

    def connect_to_db(self):
        # Method creates a handle to Database and collection

        self.dbase = self.client[self.db_name]  
        self.pkts = self.dbase[self.col_name]
   
    def insert_to_db(self,packet):
        #results = self.pkts.insert_many(packet)   
        #results = self.pkts.insert_one(packet, bypass_document_validation=False)   
        results = self.pkts.insert_many(packet, bypass_document_validation=False)   
        for db_id in  results.inserted_ids:
            print('Data is written with id' + str(db_id))
        
         

    def close_db_con(self):
        # Method to close the instance

        self.client.close()



