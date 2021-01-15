import pytest
from model.group import group
from fixture.application import Application

@pytest.fixture
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture

def test_login(app):
  app.open_home_page()
  app.login( group(username="admin", password="12345678"))
  app.open_dashboard_page()
  app.open_cards_page()
  app.open_users_dropdown()
  app.logout()
