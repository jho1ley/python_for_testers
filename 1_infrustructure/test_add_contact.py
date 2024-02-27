# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="al", lastname="vs", nickname="jh", company="un", address="Z1B", home="2234",mobile="799999", email="asdf@asdf.e"))
    app.logout()

def test_add_blank_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", lastname="", nickname="", company="", address="", home="",mobile="", email=""))
    app.logout()