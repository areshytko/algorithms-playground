
import sys
from copy import deepcopy
import json


def log(msg: str = '', include: list = None, exclude: list = None, values: dict = None, step: float = 1.0):
    tracer = AlgoTracer()
    if tracer.is_on:
        tracer.log(msg=msg, include=include, exclude=exclude, values=values, step=step)


class AlgoTracer:

    def __init__(self):
        self.now = 0.0
        self.trace = []
        self.is_on = True

    def step(self, increment: float = 1.0):
        self.now += increment

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False

    def log(self, msg: str = '', include: list = None, exclude: list = None, values: dict = None, step: float = 1.0):

        self.step(step)

        exclude = exclude or []
        variables = deepcopy(sys._getframe(1).f_locals)
        if include is not None:
            variables = {k: v for k, v in variables.items() if k in include}
        else:
            for x in exclude:
                variables.pop(x)
        if values:
            variables = {**variables, **values}

        self.trace.append({
            'step': self.now,
            'state': variables,
            'msg': msg
        })

    def save(self, filename: str):
        with open(filename, 'w') as wf:
            json.dump(self.trace, wf, indent=4)

    def print(self):
        print("Algorithm Trace: \n\n")
        for step in self.trace:
            print(f"step: {step['step']} \n")
            print(f"description: {step['msg']}")
            print(f"state: \n {json.dumps(step['state'], indent=4)}")
            print('\n')
