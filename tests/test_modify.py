from model.group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New group"))

# def test_modify_first_contact(app):
#     app.contact.modify_first_contact()

