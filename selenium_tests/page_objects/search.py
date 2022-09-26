# -*- coding: utf-8 -*-
import time
from typing import NoReturn, Final
from .base import BasePage


class SearchPage(BasePage):

    page_uri: Final = "controller=search"
    specific_title = "Search"
    empty_search = False

    def __init__(self, driver,empty_search=False):
        super(SearchPage, self).__init__(driver)
        self.empty_search=empty_search

    # XPATH locators
    _results_counter_text_locator = "//div[@id='result-stats']"
    _error_notification_text_locator = "//div[@class='card-section']"

    # Web elements
    @property
    def results_counter_text(self) -> int:
        """
        Returns the number of results of the search
        :return: the number of results of the search as an integer
        """
        try:
            time.sleep(1)
            message = self._get_element(self._results_counter_text_locator).text.strip()
            print(message)
            return int(message.split(" ")[1])
        except Exception as e:
            print(self.empty_search)
            if self.empty_search is True:
                return 0
            else:
                raise (Exception(e))

    @property
    def error_notification_text(self) -> str:
        return self._get_element(self._error_notification_text_locator).text.strip()

    # Methods
    def wait_for_page_to_load(self) -> NoReturn:
        """
        Wait for some web elements to show up on the screen
        :return:
        """
        super(SearchPage, self).wait_for_page_to_load()
        self.results_counter_text
