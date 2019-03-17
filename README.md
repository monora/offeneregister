offene-register
===============

Story on the rise and fall of civilisation

Refer to:

- https://offeneregister.de/daten
- https://github.com/openc/openc-schema/blob/master/schemas/company-schema.json
- https://github.com/Julian/jsonschema in Python


- https://neo4j.com/blog/cypher-load-json-from-url/

```python
import os
import requests
from py2neo import neo4j

# Connect to graph and add constraints.
neo4jUrl = os.environ.get('NEO4J_URL',"http://localhost:7474/db/data/")
graph = neo4j.GraphDatabaseService(neo4jUrl)

# Add uniqueness constraints.
neo4j.CypherQuery(graph, "CREATE CONSTRAINT ON (q:Question) ASSERT q.id IS UNIQUE;").run()

# Build URL.
apiUrl = "https://api.stackexchange.com/2.2/questions...." % (tag,page,page_size)
# Send GET request.
json = requests.get(apiUrl, headers = {"accept":"application/json"}).json()

# Build query.
query = """
UNWIND {json} AS data ....
"""

# Send Cypher query.
neo4j.CypherQuery(graph, query).run(json=json)
```

## Examples

```
bunzip2 -c -d  data/raw/de_companies_ocdata.jsonl.bz2 | grep "Gau-Algesheim" | jq '.'|less
```

----

This data driven journalism repository was generated with [`Cookiecutter`](https://github.com/audreyr/cookiecutter
) along with [`@JAStark`](https://github.com/JAStark)'s [`cookiecutter-data-driven-journalism`](https://github.com/JAStark/cookiecutter-data-driven-journalism) template.

## Install

```shell
sudo conda install pyscaffold
sudo conda install -c conda-forge cookiecutter
putup --cookiecutter https://github.com/jastark/cookiecutter-data-driven-journalism offene-register
conda create --name offene-register
conda install -n offene-register scipy
conda activate offene-register
```

### Setup IDEA

- Use existing conda environment as project SDK
- pip install jupyter to use ipython as python console
- Set _pytest_ as _default test runner_ in Settings - Tools - Python Integrated Tools


## License
This work is published under the [Creative Commons ShareAlike 4.0 International License](/LICENSE)
