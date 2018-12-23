from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from json import loads,dumps
from datetime import datetime
db=SQLAlchemy()


class FeatureRequest(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    description=db.Column(db.String)
    client=db.Column(db.String) #There is only 3 client availabale tho 
    client_priority=db.Column(db.Integer)
    target_date=db.Column(db.DateTime)
    product_area=db.Column(db.String)


    def __str__(self):
        d={}
        d["id"]=self.id
        d["title"]=self.title
        d["description"]=self.description
        d["client"]=self.client
        d["client_priority"]=self.client_priority
        d["target_date"]=self.parse_datetime( self.target_date)
        d["product_area"]=self.product_area
        return dumps(d)

    def __repr__(self):
        return self.__str__()
    def parse_datetime(self,datetime):
        return str(datetime.day)+"/"+str(datetime.month)+"/"+str(datetime.year)
    def to_json(self):
        return jsonify(self.__str__())

    def to_dict(self):
        return loads(self.__str__())

    @classmethod
    def add_feature(cls,title,description,client,\
                    client_priority,target_date,product_area):
        client_features=cls.query.filter_by(client=client).order_by(cls.client_priority.desc()).all()
        priority=1
        
        for feature in client_features:
            if feature.client_priority>=client_priority:
                priority=feature.client_priority
                feature.client_priority+=1
            else:
                break

        new_feature=cls(title=title,description=description,target_date=target_date,\
                        client_priority=priority,product_area=product_area,client=client)

        db.session.add(new_feature)
        db.session.commit()

    @classmethod
    def fetch_all(cls,client):
        trim =lambda x:x.delete()
        features=filter(trim,[feature for feature in cls.query.filter_by(client=client)\
                                        .order_by(cls.client_priority.asc()).all()])
        return [feature.to_dict() for feature in features]


    @classmethod
    def fetch_all_all(cls):
        return [feature.to_dict() for feature in cls.query.order_by(cls.client_priority.asc()).all()]

    def delete(self):
        if datetime.now()>self.target_date:
            db.session.delete(self)
            db.session.commit()
            return False
        else:
            return self


