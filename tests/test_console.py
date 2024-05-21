#!/usr/bin/env python3
"""
Unit tests for the HBNBCommand class.
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

class TestHBNBCommand(unittest.TestCase):
    """
    Unit tests for the HBNBCommand class.
    """

    def setUp(self):
        """Set up test environment"""
        storage.reset()  # Assuming storage has a reset method to clear data

    def tearDown(self):
        """Tear down test environment"""
        storage.reset()  # Clear data after each test

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)
            self.assertIn("BaseModel.{}".format(output), storage.all())

    def test_create_missing_class_name(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class_name(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show(self):
        """Test show command"""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(instance.id))
            output = f.getvalue().strip()
            self.assertIn(instance.id, output)

    def test_show_missing_class_name(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class_name(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_invalid_id(self):
        """Test show command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy(self):
        """Test destroy command"""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(instance.id))
            self.assertNotIn("BaseModel.{}".format(instance.id), storage.all())

    def test_destroy_missing_class_name(self):
        """Test destroy command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class_name(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_id(self):
        """Test destroy command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_all_with_class_name(self):
        """Test all command with class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_update(self):
        """Test update command"""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel {} name "test"'.format(instance.id))
            self.assertEqual(instance.name, "test")

    def test_update_missing_class_name(self):
        """Test update command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class_name(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_invalid_id(self):
        """Test update command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attribute_name(self):
        """Test update command with missing attribute name"""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel {}'.format(instance.id))
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

    def test_update_missing_value(self):
        """Test update command with missing value"""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel {} name'.format(instance.id))
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            self.assertTrue(int(f.getvalue().strip()) >= 0)

    def test_default_all(self):
        """Test <class name>.all() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_default_count(self):
        """Test <class name>.count() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertTrue(int(f.getvalue().strip()) >= 0)

    def test_default_show(self):
        """Test <class name>.show(<id>) command"""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(\"{}\")".format(instance.id))
            output = f.getvalue().strip()
            self.assertIn(instance.id, output)

    def test_default_destroy(self):
        """Test <class name>.destroy(<id>) command"""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(\"{}\")".format(instance.id))
            self.assertNotIn("BaseModel.{}".format(instance.id), storage.all())

    def test_default_update(self):
        """Test <class name>.update(<id>, <attribute name>, <attribute value>) command"""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("{}", "name", "test")'.format(instance.id))
            self.assertEqual(instance.name, "test")

    def test_default_update_dict(self):
        """Test <class name>.update(<id>, <dictionary representation>) command"""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("{}", {{"name": "test"}})'.format(instance.id))
            self.assertEqual(instance.name, "test")


if __name__ == "__main__":
    unittest.main()

