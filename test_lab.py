# test_students.py
import unittest
import importlib
import os

class TestStudentLabs(unittest.TestCase):
    def test_student_labs(self):
        students = [filename[:-3] for filename in os.listdir('student_labs') if filename.endswith('.py')]

        for student in students:
            mod = importlib.import_module(f'student_labs.{student}')
            add = getattr(mod, 'add', None)
            
            self.assertIsNotNone(add, f"add function does not exist in {student}'s file")
            
            self.assertEqual(add(2, 3), 5, f"{student}'s output is wrong")

if __name__ == "__main__":
    unittest.main()