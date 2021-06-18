from django.test import TestCase
from .models import Activity

# Create your tests here.


class ActivityTest(TestCase):
    def setUp(self):
        self.type = Activity(title="New Activity")

    def test_typestring(self):
        self.assertEqual(str(self.type), "New Activity")

    def test_tablename(self):
        self.assertEqual(str(Activity._meta.db_table), "activity")
