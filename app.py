from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='db', port=6379)

@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
    except:
        count = "Error connecting to Redis"
    return f"<h1>DevOps Lab</h1><p>Visitor count: {count}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
