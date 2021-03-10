from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
 
app = Flask(__name__)
         
app.secret_key = "caircocoders-ednalan"
         
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'patterndb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app) 
         
@app.route('/')
def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cur.execute("SELECT DISTINCT office FROM employee ORDER BY office ASC")
    cur.execute("SELECT DISTINCT type FROM typesoftrees ORDER BY type ASC")
    typesoftrees = cur.fetchall()  
    return render_template('index.html', typesoftrees = typesoftrees)
 
@app.route("/Iterator",methods=["POST","GET"])
def Iterator():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        query = request.form['query']
        #print(query)
        if query == '':
            cur.execute("SELECT * FROM typesoftrees ORDER BY id DESC")
            typesoftrees = cur.fetchall()
            print('all list')
        else:
            search_text = request.form['query']
            print(search_text)
            cur.execute("SELECT * FROM typesoftrees WHERE type IN (%s) ORDER BY id DESC", [search_text])
            typesoftrees = cur.fetchall()  
    return jsonify({'htmlresponse': render_template('response.html', typesoftrees= typesoftrees)})
 
if __name__ == "__main__":
    app.run(debug=True)