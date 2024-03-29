#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `offeneregister` package."""

import pytest

from click.testing import CliRunner

from offeneregister import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Import bzip2 jsonl' in help_result.output

def test_command_line_url():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--url', 'invalid-url'])
    assert help_result.exit_code == 2
