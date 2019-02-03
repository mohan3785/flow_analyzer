from pymongo import MongoClient
import pprint

class dbase():
    #Class Attributes
    client = MongoClient()

    def __init__(self):
        # Instance Attributes
        self.db_name = "pkt_captures"
        self.col_name = "pkts"

    def connect_to_db(self):
        # Method creates a handle to Database and collection

        self.dbase = self.client[self.db_name]  
        self.pkts = self.dbase[self.col_name]
   
    def insert_to_db(self,packet):
        results = self.pkts.insert_many(packet)   
        for db_id in  results.inserted_ids:
            print('Data is written with id' + str(db_id))
        
         

    def close_db_con(self):
        # Method to close the instance

        self.client.close()

if __name__ == "__main__":
    db = dbase()
    db.connect_to_db()
    packet = [
      {
        'l2_src_port' : '800',       
        'l2_dst_port' : '80',
        'l2_proto' : 'tcp',
        'l3_src_ip' : '20.20.20.1',
        'l3_dst_ip' : '40.40.40.1'
      },
      {
        'l2_src_port' : '1800',
        'l2_dst_port' : '21',
        'l2_proto' : 'udp',
        'l3_src_ip' : '120.120.120.1',
        'l3_dst_ip' : '140.140.140.1'
      },
    ]
    db.insert_to_db(packet)
    db.close_db_con()


