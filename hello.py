import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello stranger!.'
    
@app.route('/hello/<userName>', methods=['POST'])
def hello_user(userName):
    sql = "INSERT INTO username VALUES ('%s')" % (userName)
    conn = sqlite3.connect('data1.db')
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    return 'Hello %s!.'%(userName)
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, threaded=True, debug=True)
 

