import boto3
from envparse import env
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

# Try importing environment variables from a fil enamed .env in the
# current directory.  This will also load any environment variables
# directly from the environment if set
env.read_envfile()

ES_HOST = env("ES_HOST")
REGION = env("AWS_DEFAULT_REGION")
SERVICE = "es"  # es == 'elasticsearch'


def get_credentials():
    """
    Get our AWS credentials from boto and return a valid
    AWS4Auth object for our ES host
    """
    # Load AWS IAM credentials using the normal environment / credentials
    # file mechanisms
    credentials = boto3.Session().get_credentials()
    auth = AWS4Auth(credentials.access_key, credentials.secret_key, REGION, SERVICE)
    return auth


def get_es_connection(auth):
    """
    Build and return an ElasticSearch connection using AWS4Auth
    and our specific PWBM IAM user
    """
    return Elasticsearch(
        hosts=[{"host": ES_HOST, "port": 443}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
    )


if __name__ == "__main__":
    print(f"Using region: {REGION}")
    print(f"Connecting to ES Host: {ES_HOST}")

    auth = get_credentials()
    es = get_es_connection(auth)

    # Create document in an index
    document = {
        "name": "Frank Wiles",
        "gender": "male",
        "location": "Kansas",
        "description": "Python Consultant",
    }
    print("Indexing document...")
    es.index(index="frank-test", doc_type="person", id=1, body=document)

    print("Retrieving by id...")
    print(es.get(index="frank-test", doc_type="person", id=1))

    print("Retrieving by searching...")
    print(es.search(index="frank-test", body={"query": {"match": {"name": "frank"}}}))
