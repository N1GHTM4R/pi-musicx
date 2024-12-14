import unittest
from unittest.mock import patch, MagicMock
import tkinter as Tk
import sys
import os

# Add the directory containing soundplayer.py to the Python path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), r'C:\Users\ceede\pi-musicx\src\main.py'))

from soundplayer import play_sound
import main

class TestMain(unittest.TestCase):

    @patch('main.play_sound')
    def test_button_clicked(self, mock_play_sound):
        # Simulate the button click
        main.button_clicked()
        
        # Check if play_sound was called with the correct argument
        mock_play_sound.assert_called_with("200hztest.wav")

    def test_tkinter_setup(self):
        # Check if the Tkinter root window is set up correctly
        self.assertEqual(main.root.geometry(), "400x400")
        self.assertEqual(main.root.title(), "Sound Tester")

        # Check if the button is created with the correct options
        button = main.button
        self.assertEqual(button.cget("text"), "test audio")
        self.assertEqual(button.cget("activebackground"), "blue")
        self.assertEqual(button.cget("activeforeground"), "white")
        self.assertEqual(button.cget("anchor"), "center")
        self.assertEqual(button.cget("bd"), 3)
        self.assertEqual(button.cget("bg"), "lightgray")
        self.assertEqual(button.cget("cursor"), "hand2")
        self.assertEqual(button.cget("disabledforeground"), "gray")
        self.assertEqual(button.cget("fg"), "black")
        self.assertEqual(button.cget("font"), ("Arial", 12))
        self.assertEqual(button.cget("height"), 2)

if __name__ == '__main__':
    unittest.main()