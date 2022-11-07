class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, variations):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(variations)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.f_name)
        self.change_field_value("middlename", contact.m_name)
        self.change_field_value("lastname", contact.l_name)
        self.change_field_value("nickname", contact.n_name)
        self.change_field_value("title", contact.user_title)
        self.change_field_value("company", contact.user_company)
        self.change_field_value("address", contact.user_address)
        self.change_field_value("home", contact.user_home)
        self.change_field_value("mobile", contact.user_mobile)
        self.change_field_value("work", contact.user_work)
        self.change_field_value("fax", contact.user_fax)
        self.change_field_value("email", contact.user_email)
        self.change_field_value("email2", contact.user_email2)
        self.change_field_value("email3", contact.user_email3)
        self.change_field_value("homepage", contact.user_homepage)
        self.change_field_value("address2", contact.user_addres2)
        self.change_field_value("phone2", contact.user_phone2)
        self.change_field_value("notes", contact.user_notes)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        #open home page
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #accept the deletion
        wd.switch_to.alert.accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        #open home page
        wd.get("http://localhost/addressbook/")
        self.select_first_contact()
        #open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill the modification
        self.fill_contact_form(new_contact_data)
        #submit modification
        wd.find_element_by_name("update").click()
        #return to home page
        wd.find_element_by_link_text("home page").click()



    def count(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        return len(wd.find_elements_by_name("selected[]"))








