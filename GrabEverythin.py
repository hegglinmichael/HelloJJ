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

    print("testing specific index")
    res = es.get(index="customer", doc_type="_doc", id=1)
    print("this is res-------")
    print(res)
    print("\n")


if __name__ == "__main__":
    main()
