#!/usr/bin/env python

from lib.user import User

import random
import ipdb

class Teacher(User):

    KNOWLEDGE = [
        "a String is a data type in Python",
        "programming is hard, but it's worth it",
        "javascript async web request",
        "Python function call definition",
        "object oriented dog cat class instance",
        "programming computers hacking learning terminal",
        "pipenv shell",
        "pytest -x flag to fail fast",
    ]    

    def teach(self):
        i = random.randrange(len(self.KNOWLEDGE))
        return self.KNOWLEDGE[i]
