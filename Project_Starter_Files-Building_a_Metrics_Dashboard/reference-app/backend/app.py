from flask import Flask, render_template, request, jsonify

import pymongo
from flask_pymongo import PyMongo

from jaeger_client import Config
from flask_opentracing import FlaskTracing
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
PrometheusMetrics(app)

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)

config = Config(
    config={
        'sampler': {'type': 'const',
                    'param': 1},
        'logging': True,
        'reporter_batch_size': 1},

    service_name="backend-service",
    validate=True
    )

tracer = config.initialize_tracer()
tracing = FlaskTracing(tracer, True, app)

with tracer.start_span('first-span') as span:
    span.set_tag('first-tag', '100')

@app.route('/')
def homepage():
    return "Hello World"


@app.route('/api')
def my_api():
    answer = "something"
    return jsonify(repsonse=answer)


@app.route('/star', methods=['POST'])
def add_star():
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']
    star_id = star.insert({'name': name, 'distance': distance})
    new_star = star.find_one({'_id': star_id})
    output = {'name': new_star['name'], 'distance': new_star['distance']}
    return jsonify({'result': output})


if __name__ == "__main__":
    app.run()
