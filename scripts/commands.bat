docker commands::
====================
docker login
docker build -t shlomowind/fastapi-crud:latest .
docker run -d -p 8000:8000 ^
  -e MONGO_URL="mongodb://host.docker.internal:27017" ^
  -e MONGO_DB_NAME="enemy_soldiers" ^
  -e MONGO_COLLECTION_NAME="soldier_details" ^
  shlomowind/fastapi-crud:latest
docker ps
docker logs <CONTAINER_ID>
docker push shlomowind/fastapi-crud:latest