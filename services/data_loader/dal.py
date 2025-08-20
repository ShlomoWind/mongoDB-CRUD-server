from services.data_loader.conection import Connection
from services.data_loader.object import Document

class Dal:
    def __init__(self):
        self.connection = Connection()

    def create(self, document: Document):
        result = self.connection.collection.insert_one({
            "ID": document.ID,
            "first_name": document.first_name,
            "last_name": document.last_name,
            "phone_number": document.phone_number,
            "rank": document.rank
        })
        return result.inserted_id

    def read_all(self):
        return list(self.connection.collection.find({}))

    def update(self,_id,field_dict):
        result = self.connection.collection.update_one(
            {"_id": _id},
            {"$set": field_dict}
        )
        return result.modified_count

    def delete(self, _id):
        result = self.connection.collection.delete_one({"_id": _id})
        return result.deleted_count