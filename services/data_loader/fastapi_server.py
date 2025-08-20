from services.data_loader.dal import Dal
from services.data_loader.object import Document
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bson import ObjectId

app = FastAPI()
dal = Dal()

class SoldierModel(BaseModel):
    ID: int
    first_name: str
    last_name: str
    phone_number: str
    rank: str

@app.post("/soldiersdb")
def create_soldier(soldier: SoldierModel):
    try:
        soldier_data = soldier.model_dump()
        doc = Document(**soldier_data)
        inserted_id = dal.create(doc)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"inserted_id": str(inserted_id)}

@app.get("/soldiersdb")
def read_all():
    try:
        result = dal.read_all()
        for r in result:
            r["_id"] = str(r["_id"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return result

@app.put("/soldiersdb")
def update_soldier(_id: str,field_dict: dict):
    try:
        updated_count = dal.update(ObjectId(_id), field_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"updated_count": updated_count}

@app.delete("/soldiersdb")
def delete_soldier(_id: str):
    try:
        deleted_count = dal.delete(ObjectId(_id))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"deleted_count": deleted_count}