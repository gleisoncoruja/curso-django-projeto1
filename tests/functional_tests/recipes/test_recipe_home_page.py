
from selenium.webdriver.common.by import By

from base import RacipeBaseFunctionalTest


class RecipeHomePageFunctionalTest(RacipeBaseFunctionalTest):
    def test_recipe_home_page_without_recipes_not_found_messages(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')

        self.assertIn('Ainda não há receitas cadastradas', body.text)
