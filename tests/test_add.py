# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact


def test_new_contact(app):
    app.contact.create(Contact(f_name="name1", m_name="middle1", l_name="last1", n_name="nick1", user_title="title1", user_company="comp1", user_address="address1", user_home="01", user_mobile="02",
                               user_work="03", user_fax="04", user_email="email1@gmail.com", user_email2="email2@gmail.com", user_email3="email3@gmail.com",
                               user_homepage="email4@gmail.com", user_addres2="address_sec", user_phone2="home_my", user_notes="notes"))

def test_new_empty_contact(app):
    app.contact.create(Contact(f_name="", m_name="", l_name="", n_name="", user_title="", user_company="", user_address="", user_home="", user_mobile="",
                               user_work="", user_fax="", user_email="", user_email2="", user_email3="",
                               user_homepage="", user_addres2="", user_phone2="", user_notes=""))

def test_add_group(app):
    app.group.create(Group(name="group", header="1", footer="1"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

