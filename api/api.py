import datetime
from flask import Flask, jsonify, request
from flask.ext.redis import FlaskRedis


app = Flask(__name__)
app.config['REDIS_URL'] = "redis://redis:6379"
app.config['APP_VERSION'] = "1.3"

redis_store = FlaskRedis(app)


@app.route("/")
def status():
    print vars(request)
    return jsonify(status="OKAY", requestor_ip=request.remote_addr,
                   user_agent=request.headers.get('User-Agent', 'none'),
                   timestamp=datetime.datetime.utcnow(),
                   api_version=app.config['APP_VERSION'])


@app.route("/incrementer")
def incrementer():
    counter = redis_store.incr('incrementer')
    return jsonify(incrementer=counter, api_version=app.config['APP_VERSION'])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
