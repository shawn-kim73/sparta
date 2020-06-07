from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017) 
db = client.dbsparta  

@app.route('/')
def home():
    return render_template('firstwork.html')

@app.route('/honeysells', methods=['POST'])
def write_honeysell():
    name_receive = request.form['name_give']
    inputGroupSelect01_receive = request.form['inputGroupSelect01_give']
    address_receive = request.form['address_give']
    callnumber_receive = request.form['callnumber_give']
    honeysell={
    'name':name_receive,
    'quantity':inputGroupSelect01_receive,
    'address':address_receive,
    'callnumber':callnumber_receive
    }  
    db.honeysells.insert_one(honeysell)
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})  

@app.route('/honeysells', methods=['GET'])
def read_honeysell():
    
    honeysells = list(db.honeysells.find({},{'_id':0}))
    return jsonify({'result':'success', 'honeysells': honeysells})

 

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)