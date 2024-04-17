from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

redis_db = redis.Redis(host = 'redis', port=6379,db=0)

@app.route('/')
def baze():
    value = redis_db.keys()
    if not value:
        return "база пуста"
    else:
        new_value = []
        for i in value:
            new_value.append(i.decode('utf-8'))
        return new_value


@app.route('/data', methods=['GET', 'POST', 'PUT'])
def handler():
    if request.method == 'GET':
        key = request.args.to_dict()
        goal = list(key.items())
        if not goal:
            print("нету")
            return "ничего"
        else:
            print("есть")

            key = goal[0][0]
            value = redis_db.get(key)
            print(value)
            return jsonify({key: value.decode('utf-8')}) if value else 'Key not found'

    if request.method == 'POST' or request.method == 'PUT':
        data = request.get_json()
        for i,j in data.items():

            redis_db.set(i,j)
  #      for key, value in data.items():
   #         redis_db.set(key, value)
        
        return jsonify(data)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)