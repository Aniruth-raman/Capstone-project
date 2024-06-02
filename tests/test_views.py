from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemView
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Menu.objects.create(title="Malai Kofta Masala", price=390.40, inventory=5)
        Menu.objects.create(title="Paneer Butter Masala", price=280.00, inventory=4)

    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuSerializer(menuitems, many=True)
        request = self.factory.get("restaurant/menu/")
        response = MenuItemView.as_view()(request)
        self.assertEqual(response.data, serialized_menuitems.data)
