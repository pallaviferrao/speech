import  firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from src.enter import enter



cred = credentials.Certificate("C:/Users/Pallavi/Downloads/service.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://quiz-85773.firebaseio.com/'
})

root = db.reference()
print(root.get())

trial = enter("What is the date?","11","20","28","40","28")
new_user = root.child('Questions').push(enter.json(trial))

