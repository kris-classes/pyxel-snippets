#!/usr/bin/env python
"""
Simple autoreloader which can probably break in a million ways.

NOTE: Requires the module being run to define an App() class.
Useful for prototyping small pyxel apps or experimenting with snippets.

Usage:
    python autoreload.py 04_classes.py


Or if you're on Linux/MacOS, chmod+x then ./autoreload.py myfile.py
You can also add it to your PATH as a script called 'autoreload' if you like.

Currently only supports 1 file and the file must have a class named App.
Wrote this in ~30 minutes (after ~15 years of using Python) so it's probably
full of bugs and ways it can fail.


Kris Pritchard / @krisrp
"""
import datetime
import hashlib
import importlib
import logging
import multiprocessing
import signal
import sys
import time


# Uncomment to see debug output. Comment to silence debug output.
logging.basicConfig(level=logging.DEBUG)


def signal_handler(sig, frame):
    """Handles user exit via Ctrl-C"""
    logging.debug('Exiting')
    sys.exit(0)

# Setup the signal handler to catch Ctrl-C (SIGINT)
signal.signal(signal.SIGINT, signal_handler)


def watch(filename):
    """Watches a file for changes and runs the App() class within it."""

    # Starting with no existing process.
    process = None

    # Strip the .py extension to get the module name.
    module_name = filename.rstrip('.py')

    # Import the module, equivalent to 'import module_name'.
    imported_module = importlib.import_module(module_name, package=None)
    logging.debug(f'Imported {module_name}')

    # Starting with no file hash.
    previous_hash = None

    # Loop forever (or until Ctrl-C)
    while True:
        # Get the current date/time.
        now = datetime.datetime.now()

        # Convert it to a string.
        now_as_str = now.strftime('%H:%m:%S')

        # Open the file.
        with open(filename) as f:
            # Read each line of the file into a list.
            lines = f.readlines()

            # Join each line into a string.
            content = ''.join(lines)

            # Encode the string as UTF-8 for the hash function.
            encoded_content = content.encode('utf8')

            # Hash the file content.
            file_hash = hashlib.blake2b(encoded_content)

            # Get a hexdigest of the hash.
            digest = file_hash.hexdigest()

        # If the hash hasn't changed, just sleep for 1 second.
        if previous_hash == digest:
            time.sleep(1)

        # Otherwise it's changed, so let's do stuff.
        else:

            # Print the current time.
            logging.debug(f'{now_as_str} File changed. Reloading')

            # If the process is running, terminate it.
            if process:
                process.terminate()
                logging.debug(f'Killed process: {process.pid}')

            # Compare the old hash to the new (for debugging)
            logging.debug(f'Previous Hash: {previous_hash}')
            logging.debug(f'Current Hash: {digest}')
            previous_hash = digest

            # Create a new process with our App() class we want to instantiate.
            process = multiprocessing.Process(target=imported_module.App)
            logging.debug(f'Created new process: {process}')

            # Start the process, and begin the loop all over again.
            process.start()
            logging.debug(f'Process ID: {process.pid}')


if __name__ == '__main__':
    # Demonstrating how to use sys.argv for students.
    logging.debug(f'sys.argv: {sys.argv}')

    # Gets the filename to autoreload as the first argument.
    watch(sys.argv[1])
