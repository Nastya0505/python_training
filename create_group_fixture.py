# -*- coding: utf-8 -*-
import pytest
from group import Group
from application_for_create_group import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="group", header="1", footer="1"))
    app.logout()

def test_add_empty(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

