"""Runner to execute all examples for Week-2 Day-4.

This runner executes each example script using `runpy.run_path` so
filenames starting with digits or dots are handled safely.
"""
import os
import runpy

here = os.path.dirname(__file__)

examples = [
	os.path.join(here, 'examples', '01_waits_demo.py'),
	os.path.join(here, 'examples', '02_dynamic_ui_handling.py'),
	os.path.join(here, 'examples', '03_flaky_test_causes.py'),
]

for ex in examples:
	print('\n=== Running', os.path.basename(ex), '===')
	runpy.run_path(ex, run_name='__main__')
