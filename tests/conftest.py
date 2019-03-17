#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    conftest.py for offene_register.

    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

# noinspection PyPackageRequirements
from pathlib import Path

import pytest
import json_lines
import bz2

from src.offene_register.jsonl2neo import JsonlImporter


def first_item(file):
    with open(file, 'rb') as f:
        for item in json_lines.reader(f):
            return item


def first_item_bz2(file):
    with bz2.BZ2File(file, 'rb') as f:
        for item in json_lines.reader(f):
            return item


@pytest.fixture()
def companies_jsonl(shared_datadir) -> Path:
    return shared_datadir / '5_de_companies.jsonl'


@pytest.fixture()
def companies_jsonl_bz2(shared_datadir) -> Path:
    return shared_datadir / '5_de_companies.jsonl.bz2'


@pytest.fixture()
def olly_company(companies_jsonl: Path) -> dict:
    return first_item(companies_jsonl)


@pytest.fixture()
def importer():
    return JsonlImporter(url=None)