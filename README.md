# Penn Budget ES Demo

## Overview

Simple example for how to access ElasticSearch from Python

## Getting Setup

You'll need to create a Python virtual environment using Python 3.6+.  I specifically built/tested this using Python 3.7.3 but should be fine
with anything 3.6 or higher.

Once your virtualenv is created and activated install the dependencies:

```shell
$ pip install -r requirements.txt
```

## Running example

To run the example just execute it:

```shell
$ python connect.py
```

## Explanation of Code

There are a few libraries in play here so let me explain them.  The `Elasticsearch` object from the `elasticsearch` library is the standard Python library for working with ES.

However, AWS's hosted ES is a bit weird about it's auth and needs to use
AWS's special request signing algorithm.  This `get_credentials()` function
retrieves our AWS creds from the environment or `~/.aws/credentials` file as it normally would and builds a `AWS4Auth` object for the Python requests
library to use for all of the https connections.

We then pass this object to `get_es_connection` which finishes the `Elasticsearch` object's initialization needs.

Our example then creates a simple document, indexes it, retrieves it by ID, and then also by search just to give you some examples.

## Environment variables

To get this working easily just set the following in a `.env` file in the
current directory.

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `ES_HOST`

Where `ES_HOST` is the FQDN/hostname of the endpoint and not the full URL
so for example:

`search-whatever.klasdhfkjhadfkjhadsf.es-east-2.es.amazonaws.com`

and not:

`https://search-whatever.klasdhfkjhadfkjhadsf.es-east-2.es.amazonaws.com`

## Documentation Links

- [Python ElasticSearch Library](https://elasticsearch-py.readthedocs.io/en/master/index.html)
- [AWS4Auth](https://github.com/DavidMuller/aws-requests-auth)

## Example simple queries

To do a simple programatic query, you can just run:

```shell
$ python search_metadata.py <value>
```

To query the entire metadata set.  So for example, to look for things related
to Kansas you would type:

```shell
$ python search_metadata.py kansas
```

Which will return a JSON result of matching metadata items.