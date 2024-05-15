from mongoengine import connect

URI = "mongodb+srv://misamihajluk1:A03LBdqNq5xiqcmw@testmongo.rvxofnn.mongodb.net/HW_09?retryWrites=true&w=majority&appName=TestMongo"


def get_data():
    client = connect(host=URI)
    db = client.HW_09
    return db