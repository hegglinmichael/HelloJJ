from elasticsearch import Elasticsearch


def main():

    es = Elasticsearch()

    for i in es.indices.get("*"):
        res = es.search(index=i, body={"query": {"match_all": {}}})
        for hit in res['hits']['hits']:
            name = hit["_source"]['name']


if __name__ == "__main__":
    main()