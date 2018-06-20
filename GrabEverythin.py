from elasticsearch import Elasticsearch


def main():

    es = Elasticsearch()

    # loops through a list of indices
    # does access info in them
    for index in es.indices.get("*"):
        print("\n")
        print("Info------")
        print(index)
        print("\n")

    # more specific to a specific index in elasticsearch
    print("testing specific index")
    res = es.get(index="customer", doc_type="_doc", id=1)
    print("this is res-------")
    print(res)
    print("\n")

    # stuff below could be used in a look to gather all data
    print("new stuff -----------------")

    res = es.search(index="customer", body={"query": {"match_all": {}}})
    for hit in res['hits']['hits']:
        print(hit)
        print("type: ", type(hit))
        print("accessing element in the dict", hit["_source"]['name'])
        print("\n")


if __name__ == "__main__":
    main()
