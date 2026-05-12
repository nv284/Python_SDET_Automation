from login_page import LoginPage
from dashboard_page import DashboardPage

print('=== Page Object Demo Runner ===')
lp = LoginPage()
lp.open()
lp.enter_username('admin')
lp.enter_password('pass')
ok = lp.submit()
lp.close()

if ok:
    dp = DashboardPage()
    dp.open()
    dp.show_widgets()
    dp.close()
else:
    print('Login failed; stopping flow')
