def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group()
    app.session.logout()

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact()
    app.session.logout()
