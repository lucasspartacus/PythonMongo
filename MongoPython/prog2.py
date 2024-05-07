import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.aula

album_novo = {"nome":"Ants from up there", "duracao": "3300", "artista":"Black Country New Road"}

db.albuns.insert_one(album_novo)