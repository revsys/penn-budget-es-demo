import sys
import json

from connect import get_credentials, get_es_connection


def search(value):
    """ Search for a specific value in Penn Budget Metadata """
    auth = get_credentials()
    es = get_es_connection(auth)

    data = es.search(
        index="metadata", body={"query": {"query_string": {"query": value}}}
    )

    return data


if __name__ == "__main__":
    # Get value from commandline
    query_value = sys.argv[1]

    # Perform query
    results = search(query_value)

    # Pretty print results
    json_string = json.dumps(results, indent=4)
    print(json_string)
