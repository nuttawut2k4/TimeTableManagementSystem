import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from tkinter import messagebox
import sys
import os

from main import challenge

from unittest.mock import MagicMock

class TestChallengeFunction(unittest.TestCase):
    
    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.ttk.Combobox.get', return_value="Student")
    @patch('tkinter.messagebox.showwarning')
    def test_invalid_student_id(self, mock_showwarning, mock_combobox_get):
        challenge()
        self.assertEqual(mock_showwarning.call_count, 1)
        self.assertEqual(mock_showwarning.call_args[0][0], 'Bad id')
        self.assertEqual(mock_showwarning.call_args[0][1], 'No such user found!')

    @patch('tkinter.messagebox.showerror')
    def test_invalid_faculty_id(self, mock_showerror):
        challenge()
        self.assertEqual(mock_showerror.call_count, 1)
        self.assertEqual(mock_showerror.call_args[0][0], 'Bad id')
        self.assertEqual(mock_showerror.call_args[0][1], 'No such user found!')

    @patch('tkinter.messagebox.showerror')
    def test_invalid_admin_credentials(self, mock_showerror):
        challenge()
        self.assertEqual(mock_showerror.call_count, 1)
        self.assertEqual(mock_showerror.call_args[0][0], 'Bad Input')
        self.assertEqual(mock_showerror.call_args[0][1], 'Incorrect Username/Password!')

    @patch('os.system')
    def test_admin_login(self, mock_os_system):
        challenge()
        self.assertEqual(mock_os_system.call_count, 1)
        self.assertEqual(mock_os_system.call_args[0][0], 'python screens\\admin_screen.py')

    @patch('screens.timetable_stud.student_tt_frame')
    def test_valid_student_login(self, mock_student_tt_frame):
        challenge()
        self.assertEqual(mock_student_tt_frame.call_count, 1)
        self.assertTrue(isinstance(mock_student_tt_frame.call_args[0][0], tk.Tk))

    @patch('screens.timetable_fac.fac_tt_frame')
    def test_valid_faculty_login(self, mock_fac_tt_frame):
        challenge()
        self.assertEqual(mock_fac_tt_frame.call_count, 1)
        self.assertTrue(isinstance(mock_fac_tt_frame.call_args[0][0], tk.Tk))

if __name__ == '__main__':
    unittest.main()
