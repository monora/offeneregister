==============
OffeneRegister
==============


.. image:: https://img.shields.io/pypi/v/offeneregister.svg
        :target: https://pypi.python.org/pypi/offeneregister

.. image:: https://img.shields.io/travis/monora/offeneregister.svg
        :target: https://travis-ci.org/monora/offeneregister

.. image:: https://readthedocs.org/projects/offeneregister/badge/?version=latest
        :target: https://offeneregister.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Offene Register with Neo4j

* Free software: MIT license
* Documentation: https://monora.github.io/offeneregister

With this library you can analyse data from offeneregister_ with Neo4j_. The Json-Schema ist defined in
`openc-schema`_. It parses the data using the python jsonschema_ library and imports it
into a Neo4j database using py2neo_ driver by Nigel Small. See also `Cypher: LOAD JSON from URL AS Data`_

.. _offeneregister: https://offeneregister.de/daten
.. _Neo4j: https://neo4j.com
.. _openc-schema: https://github.com/openc/openc-schema/blob/master/schemas/company-schema.json
.. _jsonschema: https://github.com/Julian/jsonschema
.. _py2neo: http://neo4j.com/developer/python/#_py2neo
.. _`Cypher: LOAD JSON from URL AS Data`: https://neo4j.com/blog/cypher-load-json-from-url/

Installation:
-------------

.. code-block:: console

   $ pip install offeneregister

Examples
--------

Extract data of city ``Gau Algesheim``

.. code-block:: console

  bunzip2 -c -d  data/raw/de_companies_ocdata.jsonl.bz2 | grep "Gau-Algesheim" | jq '.' | less

.. code-block:: python

 import os
 import requests
 from py2neo import neo4j

 # Connect to graph and add constraints.
 neo4jUrl = os.environ.get('NEO4J_URL',"http://localhost:7474/db/data/")
 graph = neo4j.GraphDatabaseService(neo4jUrl)

 # Add uniqueness constraints.
 neo4j.CypherQuery(graph, "CREATE CONSTRAINT ON (q:Question) ASSERT q.id IS UNIQUE;").run()

 # Build URL
 apiUrl = "https://api.stackexchange.com/2.2/questions...." % (tag,page,page_size)
 # Send GET request.
 json = requests.get(apiUrl, headers = {"accept":"application/json"}).json()

 # Build query
 query = """
 UNWIND {json} AS data ....
 """

 # Send Cypher query.
 neo4j.CypherQuery(graph, query).run(json=json)

Credits
-------

This package was created with Cookiecutter_ and the `monora/cookiecutter-pypackage-poetry`_ project
template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`monora/cookiecutter-pypackage-poetry`: https://github.com/monora/cookiecutter-pypackage-poetry
