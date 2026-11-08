"""
A online learning platform offer two courses:
Python Programming or Cybersecurity.
The students enrolled in each course and store in two sets.

python = {'Rob', 'Peter', 'Harry'}
cyber_security = {'Peter', 'Walter', 'Jim', 'Rob'}

Using these sets to perform the following tasks:

Q1. Find the students enrolled in both fthe courses ?
Q2. Find the students who enrolled in only python ?
Q3. Find the students who enrolled in only cyber security ?
Q4. Print the list of all the students ?
"""

python = {'Rob', 'Peter', 'Harry'}
cyber_security = {'Peter', 'Walter', 'Jim', 'Rob'}

# Answer 1 
print(python.intersection(cyber_security))
# Shortcut of Answer 1
print(python & cyber_security)

# Answer 2
print(python.difference(cyber_security))
# Shortcut of Answer 2
print(python - cyber_security)

# Answer 3
print(cyber_security.difference(python))
# Shortcut of Answer 3
print(cyber_security - python)

# Answer 4
print(python.union(cyber_security))
# Shortcut of Answer 4
print(python | cyber_security)