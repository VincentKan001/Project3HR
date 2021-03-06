import os
from flask import Flask, render_template, request, redirect, url_for
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

MONGO_URI= os.getenv('MONGO_URI')
DATABASE_NAME='people_manager'
COLLECTION_DEPARTMENT = 'department'

def get_connection():
    conn = pymongo.MongoClient(MONGO_URI)
    return conn
    

@app.route('/')
def index():
    conn = get_connection()
    department = conn[DATABASE_NAME]['department'].find()
    return render_template('index.html', results=department)

@app.route('/search-employee/<department_id>') 
def search_employee():
    department_name = request.args.get('department_name')
    employee_name = request.args.get('employee_name')
    employee_position = request.args.get('employee_position')
    contact_no = request.args.get('contact_no')
    out_of_office = request.args.get('out_of_office')
    critera= {} 
    
    if department_name and department_name != 'department_name':
        critera['department_name'] = department_name
    else:
        department_name = 'department_name'
        
    if employee_name and employee_name != 'employee_name':
        critera['employee_name'] = employee_name
    else:
        employee_name = 'employee_name'
        
    if employee_position and employee_position != 'employee_position':
        critera['employee_position'] = employee_position
    else:
        employee_position = 'employee_position'
        
    if contact_no and contact_no != 'contact_no':
        critera['contact_no'] = contact_no
    else:
        contact_no = 'contact_no'
    
    if out_of_office and out_of_office != 'out_of_office':
        critera['out_of_office'] = out_of_office
    else:
        out_of_office = 'out_of_office'
        
    conn = get_connection()
    conn[DATABASE_NAME]['department'].find(critera)
    
    return render_template('search_employee.html', department_name=department_name, employee_name=employee_name, employee_position=employee_position, contact_no=contact_no, out_of_office=out_of_office)
    
    
    
@app.route('/add-employee')
def show_add_employee_form():
    return render_template('add_employee.html')

@app.route('/add-employee', methods=['POST'])
def process_add_employee_form():
    department_name = request.form.get('department-name')
    employee_name = request.form['employee-name']
    employee_position = request.form['employee-position']
    contact_no = request.form['contact-no']
    out_of_office = request.form['out-of-office']
    
    conn = get_connection()
    conn[DATABASE_NAME]['department'].insert({
        "department_name" : department_name,
        "employee_name" : employee_name,
        "employee_position" : employee_position,
        "contact_no" : contact_no,
        "out_of_office" : out_of_office
    })
    
    # redirect back to root url
    return redirect("/")


# /edit-employee
@app.route('/edit-employee/<department_id>')
def show_edit_employee_form(department_id):
    conn = get_connection()
    employee = conn[DATABASE_NAME]['department'].find_one({
        '_id': ObjectId(department_id)
    })
    
    return render_template('edit_employee.html', department=department_id)
    
@app.route("/edit-employee/<department_id>", methods=['POST'])
def process_edit_employee_form(department_id):
    department_name = request.form.get('department-name')
    employee_name = request.form['employee-name']
    employee_position = request.form['employee-position']
    contact_no = request.form['contact-no']
    out_of_office = request.form['out-of-office']
    
    conn = get_connection()
    conn[DATABASE_NAME]["department"].update({
        '_id':ObjectId(department_id)
    }, {
        "department_name" : department_name,
        "employee_name" : employee_name,
        "employee_position" : employee_position,
        "contact_no" : contact_no,
        "out_of_office" : out_of_office
    })
    
    return redirect("/")

# /delete-employee
@app.route('/delete-employee/<department_id>') 
def delete_employee(department_id):
    conn = get_connection()
    conn[DATABASE_NAME]["department"].remove({
        '_id': ObjectId(department_id)
        
    })
    
    return redirect("/")

@app.route('/welcome')
def show_welcome():
    return render_template('welcome.html')
    

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    



        