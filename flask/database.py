import pyrebase
import json

class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)
            
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
    
    def insert_restaurant(self, name, data, img_path):
        restaurant_info = {
            "addr": data['addr'],
            "tel": data['tel'],
            "category": data['category'],
            "park": data['park'],
            "time1": data['time1'],
            "time2": data['time2'],
            "site": data['site'],
            "img_path": img_path
        }
        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").child(name).set(restaurant_info)
            print(data,img_path)
            return True
        else:
            return False
    
    
    
    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
            if res.key() == name:
                return False
        return True
