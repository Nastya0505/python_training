from model.group import Group
from model.contact import Contact

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(f_name="test"))
    app.contact.delete_first_contact()


