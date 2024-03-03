# -*- coding: utf-8 -*-
from course.model.contact import Contact
from course.fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="al", lastname="vs", nickname="jh", company="un", address="Z1B", home="2234",mobile="799999", email="asdf@asdf.e"))
    app.session.logout()

def test_add_blank_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", nickname="", company="", address="", home="",mobile="", email=""))
    app.session.logout()