from model.group import Group
from model.contact import Contact

# def test_modify_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     app.group.modify_first_group(Group(name="New group"))

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(f_name="test"))
    app.contact.modify_first_contact(Contact(f_name="New test"))



