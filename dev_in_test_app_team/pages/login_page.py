from pages import Page
from credentials import LOGIN, PASSWORD


class LoginPage(Page):

    def __init__(self) -> None:
        super().__init__()

        self.login_input_id = 'authLoginEmail'
        self.password_input_id = 'authLoginPassword'
        self.login_button_id = 'authLogin'

    def login(self) -> None:
        login_input_xpath = self.get_input_field_xpath(self.login_input_id)
        login_input_field = self.find_element_by_xpath(login_input_xpath)
        self.send_keys(login_input_field, LOGIN)

        password_input_xpath = self.get_input_field_xpath(self.password_input_id)
        password_input_field = self.find_element_by_xpath(password_input_xpath)
        self.send_keys(password_input_field, PASSWORD)

        login_button = self.find_element_by_id(self.login_button_id)
        login_button.click()

    def get_input_field_xpath(self, resource_id: str) -> str:
        resource_id = self._get_resource_id(resource_id)
        return f'//android.widget.EditText[@resource-id="{resource_id}"]'
