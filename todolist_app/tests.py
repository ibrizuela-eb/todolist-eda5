from django.test import TestCase
from todolist_app.models import Priority, Todo
from django.contrib.auth.models import User

# Create your tests here.
class PriorityModelTest(TestCase):
    def test_description_label(self):
        priority = Priority.objects.get(id=1)
        field_label = priority._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
    
    def test_orden_label(self):
        priority = Priority.objects.get(id=1)
        field_label = priority._meta.get_field('order').verbose_name
        self.assertEqual(field_label, 'order')

    def test_priority_str(self):
        priority = Priority.objects.get(id=1)
        self.assertEqual(str(priority), 'Low')

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        p = Priority.objects.get(id=1)
        admin = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        Todo.objects.create(
            description='New task',
            done=False,
            priority=p,
            user_assigned=admin,
        )

    def test_description_label(self):
        todo = Todo.objects.get(id=1)
        field_label = todo._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
    
    def test_priority_label(self):
        todo = Todo.objects.get(id=1)
        field_label = todo._meta.get_field('priority').verbose_name
        self.assertEqual(field_label, 'priority')

    def test_todo_str(self):
        todo = Todo.objects.get(id=1)
        self.assertEqual(str(todo), 'New task')