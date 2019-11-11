import os
from flask import Flask, render_template, request, redirect, url_for
import pymongo


app = Flask(__name__)

MONGO_URI= os.getenv('MONGO_URI')
DATABASE_NAME='people_manager'
COLLECTION_DEPARTMENT = 'department'
COLLECTION_EMPLOYEE = 'employee_details'

conn = pymongo.MongoClient(MONGO_URI)
department = conn[DATABASE_NAME][COLLECTION_DEPARTMENT]




@app.route('/')
def hello():
    data = department.find({})
    
    return render_template('index.html', dep=data)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
        