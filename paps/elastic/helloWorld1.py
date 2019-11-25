from datetime import datetime
from elasticsearch6 import Elasticsearch

es = Elasticsearch()

# create an index in elasticsearch, ignore status code 400 (index already exists)
es.indices.create(index='my-index', ignore=400)

es.index(index="my-index", id=42, body={"any": "data", "timestamp": datetime.now()})

