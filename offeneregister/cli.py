# -*- coding: utf-8 -*-

"""Console script for offeneregister."""
import sys
import click
from offeneregister.jsonl2neo import JsonlImporter


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--delete',
              is_flag=True,
              help='Delete nodes and relationships before importing')
@click.option('--url',
              default="http://localhost:7474/db/data/",
              show_default=True,
              help='Connect string to neo4j database')
def main(filename: str, delete: bool, url):
    """Import bzip2 jsonl <FILENAME> into neo4j database"""
    importer = JsonlImporter(url)
    click.echo('Connected to %s' % importer.graph.database.uri)
    n_companies, n_officers = importer.import_offene_register_file(filename, delete)
    msg = 'Imported {} companies and {} officers into graph database.'
    click.echo(msg.format(n_companies, n_officers))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
