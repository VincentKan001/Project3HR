{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":39,"position":39,"stack":[[{"start":{"row":79,"column":0},"end":{"row":107,"column":24},"action":"remove","lines":["@app.route('/delete-employee/<department_id>/confirm_delete')","def delete_employee(department_id):","    conn = get_connection()","    employee = conn[DATABASE_NAME]['department'].delete_one({","        '_id': ObjectId(department_id)","    })","    return render_template('delete_employee.html',department=department_id)","    ","@app.route('/delete-employee/<department_id>/delete')","def process_delete_employee_form(department_id):","    department_name = request.form.get('department-name')","    employee_name = request.form['employee-name']","    employee_position = request.form['employee-position']","    contact_no = request.form['contact-no']","    out_of_office = request.form['out-of-office']","    ","    conn = get_connection()","    conn[DATABASE_NAME][\"department\"].delete_one({","        '_id':ObjectId(department_id)","    }, {","        \"department_name\" : department_name,","        \"employee_name\" : employee_name,","        \"employee_position\" : employee_position,","        \"contact_no\" : contact_no,","        \"out_of_office\" : out_of_office","    })","   ","    ","    return redirect(\"/\")"],"id":2}],[{"start":{"row":79,"column":0},"end":{"row":82,"column":41},"action":"insert","lines":["@app.route('/delete_task/<task_id>')","def delete_task(task_id):","    mongo.db.tasks.remove({'_id': ObjectId(task_id)})","    return redirect(url_for('get_tasks'))"],"id":3}],[{"start":{"row":82,"column":19},"end":{"row":82,"column":41},"action":"remove","lines":["(url_for('get_tasks'))"],"id":4},{"start":{"row":82,"column":19},"end":{"row":82,"column":24},"action":"insert","lines":["(\"/\")"]}],[{"start":{"row":79,"column":23},"end":{"row":79,"column":24},"action":"remove","lines":["k"],"id":5},{"start":{"row":79,"column":22},"end":{"row":79,"column":23},"action":"remove","lines":["s"]},{"start":{"row":79,"column":21},"end":{"row":79,"column":22},"action":"remove","lines":["a"]},{"start":{"row":79,"column":20},"end":{"row":79,"column":21},"action":"remove","lines":["t"]}],[{"start":{"row":79,"column":20},"end":{"row":79,"column":21},"action":"insert","lines":["e"],"id":6},{"start":{"row":79,"column":21},"end":{"row":79,"column":22},"action":"insert","lines":["m"]},{"start":{"row":79,"column":22},"end":{"row":79,"column":23},"action":"insert","lines":["p"]},{"start":{"row":79,"column":23},"end":{"row":79,"column":24},"action":"insert","lines":["l"]},{"start":{"row":79,"column":24},"end":{"row":79,"column":25},"action":"insert","lines":["o"]},{"start":{"row":79,"column":25},"end":{"row":79,"column":26},"action":"insert","lines":["y"]},{"start":{"row":79,"column":26},"end":{"row":79,"column":27},"action":"insert","lines":["e"]},{"start":{"row":79,"column":27},"end":{"row":79,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":79,"column":33},"end":{"row":79,"column":34},"action":"remove","lines":["k"],"id":7},{"start":{"row":79,"column":32},"end":{"row":79,"column":33},"action":"remove","lines":["s"]},{"start":{"row":79,"column":31},"end":{"row":79,"column":32},"action":"remove","lines":["a"]},{"start":{"row":79,"column":30},"end":{"row":79,"column":31},"action":"remove","lines":["t"]}],[{"start":{"row":79,"column":30},"end":{"row":79,"column":31},"action":"insert","lines":["d"],"id":8},{"start":{"row":79,"column":31},"end":{"row":79,"column":32},"action":"insert","lines":["e"]},{"start":{"row":79,"column":32},"end":{"row":79,"column":33},"action":"insert","lines":["p"]},{"start":{"row":79,"column":33},"end":{"row":79,"column":34},"action":"insert","lines":["a"]},{"start":{"row":79,"column":34},"end":{"row":79,"column":35},"action":"insert","lines":["r"]},{"start":{"row":79,"column":35},"end":{"row":79,"column":36},"action":"insert","lines":["t"]},{"start":{"row":79,"column":36},"end":{"row":79,"column":37},"action":"insert","lines":["m"]},{"start":{"row":79,"column":37},"end":{"row":79,"column":38},"action":"insert","lines":["e"]},{"start":{"row":79,"column":38},"end":{"row":79,"column":39},"action":"insert","lines":["n"]},{"start":{"row":79,"column":39},"end":{"row":79,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":80,"column":14},"end":{"row":80,"column":15},"action":"remove","lines":["k"],"id":9},{"start":{"row":80,"column":13},"end":{"row":80,"column":14},"action":"remove","lines":["s"]},{"start":{"row":80,"column":12},"end":{"row":80,"column":13},"action":"remove","lines":["a"]},{"start":{"row":80,"column":11},"end":{"row":80,"column":12},"action":"remove","lines":["t"]}],[{"start":{"row":80,"column":11},"end":{"row":80,"column":12},"action":"insert","lines":["e"],"id":10},{"start":{"row":80,"column":12},"end":{"row":80,"column":13},"action":"insert","lines":["m"]},{"start":{"row":80,"column":13},"end":{"row":80,"column":14},"action":"insert","lines":["p"]},{"start":{"row":80,"column":14},"end":{"row":80,"column":15},"action":"insert","lines":["l"]},{"start":{"row":80,"column":15},"end":{"row":80,"column":16},"action":"insert","lines":["o"]},{"start":{"row":80,"column":16},"end":{"row":80,"column":17},"action":"insert","lines":["y"]},{"start":{"row":80,"column":17},"end":{"row":80,"column":18},"action":"insert","lines":["e"]},{"start":{"row":80,"column":18},"end":{"row":80,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":23},"end":{"row":80,"column":24},"action":"remove","lines":["k"],"id":11},{"start":{"row":80,"column":22},"end":{"row":80,"column":23},"action":"remove","lines":["s"]},{"start":{"row":80,"column":21},"end":{"row":80,"column":22},"action":"remove","lines":["a"]},{"start":{"row":80,"column":20},"end":{"row":80,"column":21},"action":"remove","lines":["t"]}],[{"start":{"row":80,"column":20},"end":{"row":80,"column":21},"action":"insert","lines":["e"],"id":12},{"start":{"row":80,"column":21},"end":{"row":80,"column":22},"action":"insert","lines":["m"]},{"start":{"row":80,"column":22},"end":{"row":80,"column":23},"action":"insert","lines":["p"]},{"start":{"row":80,"column":23},"end":{"row":80,"column":24},"action":"insert","lines":["l"]},{"start":{"row":80,"column":24},"end":{"row":80,"column":25},"action":"insert","lines":["o"]},{"start":{"row":80,"column":25},"end":{"row":80,"column":26},"action":"insert","lines":["y"]},{"start":{"row":80,"column":26},"end":{"row":80,"column":27},"action":"insert","lines":["e"]},{"start":{"row":80,"column":27},"end":{"row":80,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":81,"column":17},"end":{"row":81,"column":18},"action":"remove","lines":["s"],"id":13},{"start":{"row":81,"column":16},"end":{"row":81,"column":17},"action":"remove","lines":["k"]},{"start":{"row":81,"column":15},"end":{"row":81,"column":16},"action":"remove","lines":["s"]},{"start":{"row":81,"column":14},"end":{"row":81,"column":15},"action":"remove","lines":["a"]},{"start":{"row":81,"column":13},"end":{"row":81,"column":14},"action":"remove","lines":["t"]}],[{"start":{"row":81,"column":13},"end":{"row":81,"column":14},"action":"insert","lines":["d"],"id":14},{"start":{"row":81,"column":14},"end":{"row":81,"column":15},"action":"insert","lines":["e"]},{"start":{"row":81,"column":15},"end":{"row":81,"column":16},"action":"insert","lines":["p"]},{"start":{"row":81,"column":16},"end":{"row":81,"column":17},"action":"insert","lines":["a"]},{"start":{"row":81,"column":17},"end":{"row":81,"column":18},"action":"insert","lines":["r"]},{"start":{"row":81,"column":18},"end":{"row":81,"column":19},"action":"insert","lines":["t"]},{"start":{"row":81,"column":19},"end":{"row":81,"column":20},"action":"insert","lines":["m"]},{"start":{"row":81,"column":20},"end":{"row":81,"column":21},"action":"insert","lines":["e"]},{"start":{"row":81,"column":21},"end":{"row":81,"column":22},"action":"insert","lines":["n"]},{"start":{"row":81,"column":22},"end":{"row":81,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":81,"column":51},"end":{"row":81,"column":52},"action":"remove","lines":["k"],"id":15},{"start":{"row":81,"column":50},"end":{"row":81,"column":51},"action":"remove","lines":["s"]},{"start":{"row":81,"column":49},"end":{"row":81,"column":50},"action":"remove","lines":["a"]},{"start":{"row":81,"column":48},"end":{"row":81,"column":49},"action":"remove","lines":["t"]}],[{"start":{"row":81,"column":48},"end":{"row":81,"column":49},"action":"insert","lines":["d"],"id":16},{"start":{"row":81,"column":49},"end":{"row":81,"column":50},"action":"insert","lines":["e"]},{"start":{"row":81,"column":50},"end":{"row":81,"column":51},"action":"insert","lines":["p"]},{"start":{"row":81,"column":51},"end":{"row":81,"column":52},"action":"insert","lines":["a"]},{"start":{"row":81,"column":52},"end":{"row":81,"column":53},"action":"insert","lines":["r"]},{"start":{"row":81,"column":53},"end":{"row":81,"column":54},"action":"insert","lines":["t"]},{"start":{"row":81,"column":54},"end":{"row":81,"column":55},"action":"insert","lines":["m"]},{"start":{"row":81,"column":55},"end":{"row":81,"column":56},"action":"insert","lines":["e"]},{"start":{"row":81,"column":56},"end":{"row":81,"column":57},"action":"insert","lines":["n"]},{"start":{"row":81,"column":57},"end":{"row":81,"column":58},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":20},"action":"insert","lines":["mongo = PyMongo(app)"],"id":17}],[{"start":{"row":81,"column":23},"end":{"row":81,"column":24},"action":"insert","lines":["_"],"id":18},{"start":{"row":81,"column":24},"end":{"row":81,"column":25},"action":"insert","lines":["i"]},{"start":{"row":81,"column":25},"end":{"row":81,"column":26},"action":"insert","lines":["d"]}],[{"start":{"row":81,"column":25},"end":{"row":81,"column":26},"action":"remove","lines":["d"],"id":19},{"start":{"row":81,"column":24},"end":{"row":81,"column":25},"action":"remove","lines":["i"]},{"start":{"row":81,"column":23},"end":{"row":81,"column":24},"action":"remove","lines":["_"]}],[{"start":{"row":80,"column":27},"end":{"row":80,"column":28},"action":"remove","lines":["e"],"id":20},{"start":{"row":80,"column":26},"end":{"row":80,"column":27},"action":"remove","lines":["e"]},{"start":{"row":80,"column":25},"end":{"row":80,"column":26},"action":"remove","lines":["y"]},{"start":{"row":80,"column":24},"end":{"row":80,"column":25},"action":"remove","lines":["o"]},{"start":{"row":80,"column":23},"end":{"row":80,"column":24},"action":"remove","lines":["l"]},{"start":{"row":80,"column":22},"end":{"row":80,"column":23},"action":"remove","lines":["p"]},{"start":{"row":80,"column":21},"end":{"row":80,"column":22},"action":"remove","lines":["m"]},{"start":{"row":80,"column":20},"end":{"row":80,"column":21},"action":"remove","lines":["e"]}],[{"start":{"row":80,"column":20},"end":{"row":80,"column":21},"action":"insert","lines":["d"],"id":21},{"start":{"row":80,"column":21},"end":{"row":80,"column":22},"action":"insert","lines":["e"]},{"start":{"row":80,"column":22},"end":{"row":80,"column":23},"action":"insert","lines":["p"]},{"start":{"row":80,"column":23},"end":{"row":80,"column":24},"action":"insert","lines":["a"]},{"start":{"row":80,"column":24},"end":{"row":80,"column":25},"action":"insert","lines":["r"]},{"start":{"row":80,"column":25},"end":{"row":80,"column":26},"action":"insert","lines":["t"]},{"start":{"row":80,"column":26},"end":{"row":80,"column":27},"action":"insert","lines":["m"]},{"start":{"row":80,"column":27},"end":{"row":80,"column":28},"action":"insert","lines":["e"]},{"start":{"row":80,"column":28},"end":{"row":80,"column":29},"action":"insert","lines":["n"]},{"start":{"row":80,"column":29},"end":{"row":80,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":20},"action":"remove","lines":["mongo = PyMongo(app)"],"id":22}],[{"start":{"row":81,"column":4},"end":{"row":82,"column":24},"action":"remove","lines":["mongo.db.department.remove({'_id': ObjectId(department_id)})","    return redirect(\"/\")"],"id":23},{"start":{"row":81,"column":4},"end":{"row":90,"column":6},"action":"insert","lines":["conn = get_connection()","    conn[DATABASE_NAME][\"department\"].update({","        '_id':ObjectId(department_id)","    }, {","        \"department_name\" : department_name,","        \"employee_name\" : employee_name,","        \"employee_position\" : employee_position,","        \"contact_no\" : contact_no,","        \"out_of_office\" : out_of_office","    })"]}],[{"start":{"row":79,"column":0},"end":{"row":107,"column":24},"action":"remove","lines":["@app.route('/delete-employee/<department_id>/confirm_delete')","def delete_employee(department_id):","    conn = get_connection()","    employee = conn[DATABASE_NAME]['department'].delete_one({","        '_id': ObjectId(department_id)","    })","    return render_template('delete_employee.html',department=department_id)","    ","@app.route('/delete-employee/<department_id>/delete')","def process_delete_employee_form(department_id):","    department_name = request.form.get('department-name')","    employee_name = request.form['employee-name']","    employee_position = request.form['employee-position']","    contact_no = request.form['contact-no']","    out_of_office = request.form['out-of-office']","    ","    conn = get_connection()","    conn[DATABASE_NAME][\"department\"].delete_one({","        '_id':ObjectId(department_id)","    }, {","        \"department_name\" : department_name,","        \"employee_name\" : employee_name,","        \"employee_position\" : employee_position,","        \"contact_no\" : contact_no,","        \"out_of_office\" : out_of_office","    })","   ","    ","    return redirect(\"/\")"],"id":24},{"start":{"row":79,"column":0},"end":{"row":86,"column":24},"action":"insert","lines":["@app.route('/delete_profile/<profile_id>') #To delete profile","def delete_profile(profile_id):","    profile = conn[DATABASE_NAME][COLLECTION_NAME].remove({","        '_id': ObjectId(profile_id)","        ","    })","    flash(\"The profile has been deleted.\")","    return redirect(\"/\")"]}],[{"start":{"row":79,"column":26},"end":{"row":79,"column":27},"action":"remove","lines":["e"],"id":25},{"start":{"row":79,"column":25},"end":{"row":79,"column":26},"action":"remove","lines":["l"]},{"start":{"row":79,"column":24},"end":{"row":79,"column":25},"action":"remove","lines":["i"]},{"start":{"row":79,"column":23},"end":{"row":79,"column":24},"action":"remove","lines":["f"]},{"start":{"row":79,"column":22},"end":{"row":79,"column":23},"action":"remove","lines":["o"]},{"start":{"row":79,"column":21},"end":{"row":79,"column":22},"action":"remove","lines":["r"]},{"start":{"row":79,"column":20},"end":{"row":79,"column":21},"action":"remove","lines":["p"]},{"start":{"row":79,"column":19},"end":{"row":79,"column":20},"action":"remove","lines":["_"]}],[{"start":{"row":79,"column":19},"end":{"row":79,"column":20},"action":"insert","lines":["-"],"id":26},{"start":{"row":79,"column":20},"end":{"row":79,"column":21},"action":"insert","lines":["e"]},{"start":{"row":79,"column":21},"end":{"row":79,"column":22},"action":"insert","lines":["m"]},{"start":{"row":79,"column":22},"end":{"row":79,"column":23},"action":"insert","lines":["p"]},{"start":{"row":79,"column":23},"end":{"row":79,"column":24},"action":"insert","lines":["l"]},{"start":{"row":79,"column":24},"end":{"row":79,"column":25},"action":"insert","lines":["o"]},{"start":{"row":79,"column":25},"end":{"row":79,"column":26},"action":"insert","lines":["y"]},{"start":{"row":79,"column":26},"end":{"row":79,"column":27},"action":"insert","lines":["e"]},{"start":{"row":79,"column":27},"end":{"row":79,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":79,"column":36},"end":{"row":79,"column":37},"action":"remove","lines":["e"],"id":27},{"start":{"row":79,"column":35},"end":{"row":79,"column":36},"action":"remove","lines":["l"]},{"start":{"row":79,"column":34},"end":{"row":79,"column":35},"action":"remove","lines":["i"]},{"start":{"row":79,"column":33},"end":{"row":79,"column":34},"action":"remove","lines":["f"]},{"start":{"row":79,"column":32},"end":{"row":79,"column":33},"action":"remove","lines":["o"]},{"start":{"row":79,"column":31},"end":{"row":79,"column":32},"action":"remove","lines":["r"]},{"start":{"row":79,"column":30},"end":{"row":79,"column":31},"action":"remove","lines":["p"]}],[{"start":{"row":79,"column":30},"end":{"row":79,"column":31},"action":"insert","lines":["d"],"id":28}],[{"start":{"row":79,"column":30},"end":{"row":79,"column":31},"action":"remove","lines":["d"],"id":29}],[{"start":{"row":79,"column":30},"end":{"row":79,"column":31},"action":"insert","lines":["d"],"id":30},{"start":{"row":79,"column":31},"end":{"row":79,"column":32},"action":"insert","lines":["e"]},{"start":{"row":79,"column":32},"end":{"row":79,"column":33},"action":"insert","lines":["p"]},{"start":{"row":79,"column":33},"end":{"row":79,"column":34},"action":"insert","lines":["a"]},{"start":{"row":79,"column":34},"end":{"row":79,"column":35},"action":"insert","lines":["r"]},{"start":{"row":79,"column":35},"end":{"row":79,"column":36},"action":"insert","lines":["t"]},{"start":{"row":79,"column":36},"end":{"row":79,"column":37},"action":"insert","lines":["m"]},{"start":{"row":79,"column":37},"end":{"row":79,"column":38},"action":"insert","lines":["e"]},{"start":{"row":79,"column":38},"end":{"row":79,"column":39},"action":"insert","lines":["n"]},{"start":{"row":79,"column":39},"end":{"row":79,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":79,"column":47},"end":{"row":79,"column":65},"action":"remove","lines":["#To delete profile"],"id":31}],[{"start":{"row":80,"column":17},"end":{"row":80,"column":18},"action":"remove","lines":["e"],"id":32},{"start":{"row":80,"column":16},"end":{"row":80,"column":17},"action":"remove","lines":["l"]},{"start":{"row":80,"column":15},"end":{"row":80,"column":16},"action":"remove","lines":["i"]},{"start":{"row":80,"column":14},"end":{"row":80,"column":15},"action":"remove","lines":["f"]},{"start":{"row":80,"column":13},"end":{"row":80,"column":14},"action":"remove","lines":["o"]},{"start":{"row":80,"column":12},"end":{"row":80,"column":13},"action":"remove","lines":["r"]},{"start":{"row":80,"column":11},"end":{"row":80,"column":12},"action":"remove","lines":["p"]}],[{"start":{"row":80,"column":11},"end":{"row":80,"column":12},"action":"insert","lines":["e"],"id":33},{"start":{"row":80,"column":12},"end":{"row":80,"column":13},"action":"insert","lines":["m"]},{"start":{"row":80,"column":13},"end":{"row":80,"column":14},"action":"insert","lines":["p"]},{"start":{"row":80,"column":14},"end":{"row":80,"column":15},"action":"insert","lines":["l"]},{"start":{"row":80,"column":15},"end":{"row":80,"column":16},"action":"insert","lines":["o"]},{"start":{"row":80,"column":16},"end":{"row":80,"column":17},"action":"insert","lines":["y"]},{"start":{"row":80,"column":17},"end":{"row":80,"column":18},"action":"insert","lines":["e"]},{"start":{"row":80,"column":18},"end":{"row":80,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":26},"end":{"row":80,"column":27},"action":"remove","lines":["e"],"id":34},{"start":{"row":80,"column":25},"end":{"row":80,"column":26},"action":"remove","lines":["l"]},{"start":{"row":80,"column":24},"end":{"row":80,"column":25},"action":"remove","lines":["i"]},{"start":{"row":80,"column":23},"end":{"row":80,"column":24},"action":"remove","lines":["f"]},{"start":{"row":80,"column":22},"end":{"row":80,"column":23},"action":"remove","lines":["o"]},{"start":{"row":80,"column":21},"end":{"row":80,"column":22},"action":"remove","lines":["r"]},{"start":{"row":80,"column":20},"end":{"row":80,"column":21},"action":"remove","lines":["p"]}],[{"start":{"row":80,"column":20},"end":{"row":80,"column":21},"action":"insert","lines":["d"],"id":35},{"start":{"row":80,"column":21},"end":{"row":80,"column":22},"action":"insert","lines":["e"]},{"start":{"row":80,"column":22},"end":{"row":80,"column":23},"action":"insert","lines":["p"]},{"start":{"row":80,"column":23},"end":{"row":80,"column":24},"action":"insert","lines":["a"]},{"start":{"row":80,"column":24},"end":{"row":80,"column":25},"action":"insert","lines":["r"]},{"start":{"row":80,"column":25},"end":{"row":80,"column":26},"action":"insert","lines":["t"]},{"start":{"row":80,"column":26},"end":{"row":80,"column":27},"action":"insert","lines":["m"]},{"start":{"row":80,"column":27},"end":{"row":80,"column":28},"action":"insert","lines":["e"]},{"start":{"row":80,"column":28},"end":{"row":80,"column":29},"action":"insert","lines":["n"]},{"start":{"row":80,"column":29},"end":{"row":80,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":82,"column":30},"end":{"row":82,"column":31},"action":"remove","lines":["e"],"id":36},{"start":{"row":82,"column":29},"end":{"row":82,"column":30},"action":"remove","lines":["l"]},{"start":{"row":82,"column":28},"end":{"row":82,"column":29},"action":"remove","lines":["i"]},{"start":{"row":82,"column":27},"end":{"row":82,"column":28},"action":"remove","lines":["f"]},{"start":{"row":82,"column":26},"end":{"row":82,"column":27},"action":"remove","lines":["o"]},{"start":{"row":82,"column":25},"end":{"row":82,"column":26},"action":"remove","lines":["r"]},{"start":{"row":82,"column":24},"end":{"row":82,"column":25},"action":"remove","lines":["p"]}],[{"start":{"row":82,"column":24},"end":{"row":82,"column":25},"action":"insert","lines":["d"],"id":37},{"start":{"row":82,"column":25},"end":{"row":82,"column":26},"action":"insert","lines":["e"]},{"start":{"row":82,"column":26},"end":{"row":82,"column":27},"action":"insert","lines":["p"]},{"start":{"row":82,"column":27},"end":{"row":82,"column":28},"action":"insert","lines":["a"]},{"start":{"row":82,"column":28},"end":{"row":82,"column":29},"action":"insert","lines":["r"]},{"start":{"row":82,"column":29},"end":{"row":82,"column":30},"action":"insert","lines":["m"]},{"start":{"row":82,"column":30},"end":{"row":82,"column":31},"action":"insert","lines":["t"]}],[{"start":{"row":82,"column":30},"end":{"row":82,"column":31},"action":"remove","lines":["t"],"id":38},{"start":{"row":82,"column":29},"end":{"row":82,"column":30},"action":"remove","lines":["m"]}],[{"start":{"row":82,"column":29},"end":{"row":82,"column":30},"action":"insert","lines":["t"],"id":39},{"start":{"row":82,"column":30},"end":{"row":82,"column":31},"action":"insert","lines":["m"]},{"start":{"row":82,"column":31},"end":{"row":82,"column":32},"action":"insert","lines":["e"]},{"start":{"row":82,"column":32},"end":{"row":82,"column":33},"action":"insert","lines":["n"]},{"start":{"row":82,"column":33},"end":{"row":82,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":81,"column":4},"end":{"row":81,"column":50},"action":"remove","lines":["profile = conn[DATABASE_NAME][COLLECTION_NAME]"],"id":40},{"start":{"row":81,"column":4},"end":{"row":82,"column":37},"action":"insert","lines":["conn = get_connection()","    conn[DATABASE_NAME][\"department\"]"]}],[{"start":{"row":86,"column":4},"end":{"row":86,"column":42},"action":"remove","lines":["flash(\"The profile has been deleted.\")"],"id":41}]]},"ace":{"folds":[],"scrolltop":1309,"scrollleft":0,"selection":{"start":{"row":83,"column":38},"end":{"row":83,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":80,"state":"start","mode":"ace/mode/python"}},"timestamp":1573669958485,"hash":"3b480f100991ca14915272b6c7295e4a582c99a0"}