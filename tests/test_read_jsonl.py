#!/usr/bin/env python
# -*- coding: utf-8 -*-

from offene_register.skeleton import fib


def test_read_json(olly_company):
    item: dict = olly_company

    assert item['all_attributes']['federal_state'] == 'Hamburg'
    assert item['name'] == 'olly UG (haftungsbeschränkt)'
    assert item['company_number'] == 'K1101R_HRB150148'

    officer: dict = item['officers'][0]
    assert officer['type'] == "person"
    assert officer['position'] == "Geschäftsführer"

    officer_attr: dict = officer["other_attributes"]
    assert officer_attr['city'] == 'Hamburg'
    assert officer_attr['firstname'] == 'Oliver'