import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.aula

album = db.albuns.find_one({"nome": "Imaginations from the Other Side"})

nome = album["artista"]["nome"]
print(nome)