import pytest
import os.path
import jsonpickle
import importlib
import pandas as pd
from fixture.application import Application
from model.group import Group


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("D:\\Torrents\\work\\ИСУ\\8. Automation training\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("excel_"):
            testdata = load_from_excel(fixture[6:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def load_from_excel(file):
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "%s.xlsx" % file)
    data = pd.read_excel(f)
    list = data['Name'].tolist()
    groups = [Group(name=x) for x in list]
    return groups
