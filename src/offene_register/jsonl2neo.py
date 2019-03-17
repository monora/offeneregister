import bz2

import json_lines
from py2neo import Node, Graph, Relationship


# from typing import Iterable


def make_company_node(c: dict) -> Node:
    """Create new Company node for dict
    """

    all_attributes = c.get('all_attributes', {})
    return Node('Company',
                name=c['name'],
                company_number=c['company_number'],
                federal_state=all_attributes.get('federal_state'),
                registered_office=all_attributes.get('registered_office'),
                registered_address=c.get('registered_address')
                )


def make_officer_node(o: dict) -> Node:
    """Create new Officer node for dict
    """

    return Node('Officer',
                name=o['name'],
                city=o.get('other_attributes', {}).get('city'),
                type=o.get('type')
                )


class JsonlImporter:
    def __init__(self, url="http://localhost:7474/db/data/"):

        if url:
            self.graph = Graph(url, bolt=False)
        else:
            self.graph = Graph()

    def import_offene_register_file(self, filename: str, erase=True) -> None:
        """Import all companies from file in jsonl format

        :param filename: bzip2 compressed file with
        :param erase: if True erase all Companies in database before importing
        :return: Number of companies imported
        """
        if erase:
            self.delete_all()

        with bz2.BZ2File(filename, 'rb') as f:
            for item in json_lines.reader(f):
                company_node = make_company_node(item)
                self.graph.merge(company_node,
                                 'Company',
                                 'company_number')
                for officer in item.get('officers', {}):
                    officer = make_officer_node(officer)
                    self.graph.merge(officer,
                                     'Officer',
                                     'name')
                    rel = Relationship(officer, 'WORKS_FOR', company_node,
                                       position=officer['position'],
                                       start_date=officer.get('start_date'),
                                       end_date=officer.get('end_date')
                                       )
                    self.graph.create(rel)

        return self.no_of_companies()

    def count_label(self, label: str):
        query = "MATCH (c:{}) return count(c)".format(label)
        return self.graph.run(query).evaluate()

    def no_of_companies(self):
        return self.count_label("Company")

    def delete_all(self):
        self.graph.evaluate("MATCH (c:Company) DETACH DELETE c")
        self.graph.evaluate("CREATE CONSTRAINT ON (c:Company) ASSERT c.company_number IS UNIQUE")

        self.graph.evaluate("MATCH (c:Officer) DETACH DELETE c")
        self.graph.evaluate("CREATE CONSTRAINT ON (c:Officer) ASSERT c.name IS UNIQUE")
