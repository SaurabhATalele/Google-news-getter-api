import pyrebase

config = {
  "apiKey": "AIzaSyAYBny-J4hzRk1WfHdNtLbZjS_YxC8iFpk",
  "authDomain": "login-form-969fb.firebaseapp.com",
  "databaseURL": "https://login-form-969fb.firebaseio.com/",
  "storageBucket": "login-form-969fb.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()