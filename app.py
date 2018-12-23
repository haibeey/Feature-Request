from flask import Flask,request,render_template,flash,url_for,redirect
from models.model import FeatureRequest,db
import config
from datetime import datetime


app=Flask(__name__)
app.config.from_object(config)
db.init_app(app)
db.create_all(app=app)


def load_features():
    client_a=FeatureRequest.fetch_all("Client A")
    client_b=FeatureRequest.fetch_all("Client B")
    client_c=FeatureRequest.fetch_all("Client C")
    
    return [client_a,client_b,client_c]

@app.route("/")
def home():
    return render_template("index.html",client_features=load_features())

@app.route("/add/features/",methods=["GET","POST"])
def add_feature():
    
    if request.method=="GET":
        return redirect(url_for('home',client_features=load_features()))
        
    elif request.method=="POST":
        title=request.form.get("title")
        description=request.form.get("description")
        client=request.form.get("client") or "Client A"
        client_priority=request.form.get("client_priority") or 1
        try:
            client_priority=int(client_priority)
            date=str(request.form.get("date")).split("-")
            target_year=int(date[0]) or 2019
            target_month=int(date[1]) or 12
            target_day=int(date[2]) or 31
        except ValueError as err:
            flash(str(err))
            return redirect(url_for('home',client_features=load_features()))
        
        
        product_area=request.form.get("product_area") or "Policies"
        target_date=datetime(target_year,target_month,target_day)
        FeatureRequest.add_feature(title,description,client,\
                            client_priority,target_date,product_area)
        
        return redirect(url_for('home',client_features=load_features()))
    else:
        return "method not allowed"

if __name__=="__main__":
    app.run(debug=True)