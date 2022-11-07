def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="new group", header="new header", footer="new footer"))
    app.session.logout()

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(f_name="new", m_name="new", l_name="new", n_name="new", user_title="new", user_company="new", user_address="new", user_home="new", user_mobile="new",
                               user_work="new", user_fax="new", user_email="new", user_email2="new", user_email3="new",
                               user_homepage="new", user_addres2="new", user_phone2="new", user_notes="new"))
    app.session.logout()

