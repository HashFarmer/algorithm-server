from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api')
def my_microservice():
    return jsonify({'hello': 'world!'})
if __name__ == '__main__':
    app.run()
    
    

# 1，浏览器
# 2，curl -v http://127.0.0.1:5000/api
 
