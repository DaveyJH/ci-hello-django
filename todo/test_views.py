from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    """Test views"""

    def test_get_todo_list(self):
        """test home page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/todo_list.html")

    def test_get_add_item(self):
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/add_item.html")

    def test_get_edit_item(self):
        item = Item.objects.create(name="Test item")
        response = self.client.get(f"/edit/{item.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/edit_item.html")

    def test_can_add_item(self):
        response = self.client.post("/add", {"name": "Test item"})
        self.assertRedirects(response, "/")

    def test_can_delete_item(self):
        item = Item.objects.create(name="Test item")
        response = self.client.get(f"/delete/{item.id}")
        self.assertRedirects(response, "/")
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name="Test item", done=True)
        response = self.client.get(f"/toggle/{item.id}")
        self.assertRedirects(response, "/")
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
