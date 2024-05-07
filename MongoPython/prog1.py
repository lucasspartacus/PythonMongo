import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.aula

albuns = db.albuns.find()

file = open("C:\\MongoPython\\albuns.txt","a")

for item in albuns:
    nome = item["nome"]
    file.write(nome + '\n')

file.close