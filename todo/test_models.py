from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    """test models"""

    def test_defaults_to_false(self):
        item = Item.objects.create(name="Test Item")
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name="Test Item")
        self.assertEqual(str(item), "Test Item")
