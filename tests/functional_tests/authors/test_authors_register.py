import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import AuthorBaseTest


@pytest.mark.functional_test
class AuthorsRegisterTest(AuthorBaseTest):

    def fill_form_dummy_data(self, form):

        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' '*20)

    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/div/form'
        )

    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('dummy@email.com')

        callback(form)
        return form

    def test_empty_frist_name_message(self):
        def callback(form):
            first_name_field = self.get_by_placeholder(form, 'Ex.: John')
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your first name', form.text)

        self.form_field_test_with_callback(callback)

    def test_empty_frist_last_name_message(self):
        def callback(form):
            last_name_field = self.get_by_placeholder(form, 'Ex.: Doe')
            last_name_field.send_keys(' ')
            last_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your last name', form.text)

        self.form_field_test_with_callback(callback)

    def test_empty_username_message(self):
        def callback(form):
            username_field = self   .get_by_placeholder(
                form, 'Your username here')
            username_field.send_keys(' ')
            username_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('This field must not be empty', form.text)

        self.form_field_test_with_callback(callback)
