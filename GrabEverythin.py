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
    res = es.indices.get(index="customer")
    print("this is res-------")
    print(res)
    print("\n")


if __name__ == "__main__":
    main()
