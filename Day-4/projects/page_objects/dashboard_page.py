from base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self):
        super().__init__('Dashboard')
        self._widgets = ['overview', 'stats']

    def show_widgets(self):
        print('Widgets:', ','.join(self._widgets))
