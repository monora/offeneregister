# -*- coding: utf-8 -*-

"""Console script for offeneregister."""
import sys
import click
from offeneregister.jsonl2neo import JsonlImporter


@click.command()
@click.argument('filename',
                type=click.STRING)
def main(filename: str):
    """Import bzip2 jsonl <FILENAME> into neo4j database"""
    importer = JsonlImporter()
    n_companies, n_officers = importer.import_offene_register_file(filename, False)
    click.echo('Imported {} companies and {} officers into graph database.'.format(n_companies, n_officers))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
