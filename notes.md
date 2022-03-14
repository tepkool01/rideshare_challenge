1. make sure src is your project root

- Need to use python 3.9?
- No concept of 'tuple in JSON', hence choice for array data type

- Seeing ahead and predicting best actual route
- Multiple requests with same name, same location, same time, would need unique IDs\

----
Should I have used the visitor pattern here? In hindsight this seems like a good fit.

performance considerations with loops, optimization would be better suited for keys

would need to add more tests, bounds checking, better algorithms, etc. What about negative grid coordinates?

Loading in the JSON could've been it's own function and not incorperated the aspect of time

----
testing
pip install coverage
python -m unittest
coverage run -m unittest
coverage report -m
specific test: python -m unittest test.test_passenger

running
python src/main.py


