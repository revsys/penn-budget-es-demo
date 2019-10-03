import csv
import codecs

from elasticsearch.helpers import bulk

from connect import get_credentials, get_es_connection


def get_items():
    with codecs.open("data/iiseries.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {
                "_index": "metadata",
                "_type": "items",
                "id": row["Id"],
                "seriesname": row["Seriesname"],
                "attribute1": row["Attribute1"],
                "value1": row["Value1"],
                "attribute2": row["Attribute2"],
                "value2": row["Value2"],
                "attribute3": row["Attribute3"],
                "value3": row["Value3"],
                "attribute4": row["Attribute4"],
                "value4": row["Value4"],
                "attribute5": row["Attribute5"],
                "value5": row["Value5"],
            }


def populate_index():
    auth = get_credentials()
    es = get_es_connection(auth)
    print("=== Starting ===")
    bulk(es, get_items())
    print("=== Finished ===")


if __name__ == "__main__":
    populate_index()
