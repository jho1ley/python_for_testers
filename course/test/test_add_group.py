# -*- coding: utf-8 -*-
from course.model.group import Group

def test_create_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="zalupa", header="asdf", footer="fefef"))
    app.session.logout()

def test_create_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()