import datetime
from flask import Flask, jsonify, request
from flask.ext.redis import FlaskRedis


app = Flask(__name__)
app.config['REDIS_URL'] = "redis://redis:6379"

redis_store = FlaskRedis(app)


@app.route("/")
def status():
    print vars(request)
    return jsonify(status="OKAY", requestor_ip=request.remote_addr,
                   user_agent=request.headers.get('User-Agent', 'none'),
                   timestamp=datetime.datetime.utcnow(), api_version="1.1")


@app.route("/incrementer")
def incrementer():
    counter = redis_store.incr('incrementer')
    return jsonify(incrementer=counter)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
