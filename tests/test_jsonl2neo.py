from offene_register.jsonl2neo import JsonlImporter, make_company_node, make_officer_node

from py2neo import Node, Relationship


def test_make_company_node(olly_company):
    node: Node = make_company_node(olly_company)
    assert isinstance(node, Node)
    assert node.labels == ['Company']
    assert node.get('name') == 'olly UG (haftungsbeschränkt)'
    assert node.get('federal_state') == 'Hamburg'
    assert node.get('registered_office') == 'Hamburg'
    assert node.get('registered_address') == 'Waidmannstraße 1, 22769 Hamburg.'
    assert node.get('company_number') == 'K1101R_HRB150148'


def test_make_officer_node(olly_company):
    node: Node = make_officer_node(olly_company['officers'][0])
    assert isinstance(node, Node)
    assert node.labels == ['Officer']
    assert node.get('name') == 'Oliver Keunecke'
    assert node.get('city') == 'Hamburg'


def test_import_file(importer: JsonlImporter, companies_jsonl_bz2):
    count = importer.import_offene_register_file(companies_jsonl_bz2)
    assert count == 5


def _test_import_all(importer: JsonlImporter):
    filename = './data/raw/de_companies_ocdata.jsonl.bz2'
    count = importer.import_offene_register_file(filename)
    print(count)

def _test_import_gaualgeheim(importer: JsonlImporter):
    filename = '/home/hd/projekte/offene-register/data/interim/gau-algesheim.jsonl.bz2'
    count = importer.import_offene_register_file(filename)
    print(count)