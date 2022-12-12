from dataclasses import dataclass
from typing import List
from functools import reduce

class Passing:
    divisble: int
    if_true: int
    if_false: int

    def __init__(self, inputs):
        split_divis = inputs[0].split()
        if_true = inputs[1].split()
        if_false = inputs[2].split()
        self.divisble = int(split_divis[-1])
        self.if_true = int(if_true[-1])
        self.if_false = int(if_false[-1])

    def check(self, item):
        check_passed = item % self.divisble
        return  self.if_true if check_passed == 0 else self.if_false

class Operation:
    sign: str
    use_old: bool
    value: int

    def __init__(self, input):
        split_input = input.split()
        self.sign = split_input[-2]
        if split_input[-1] == 'old':
            self.use_old = True
            self.value = 0
        else:
            self.use_old = False
            self.value = int(split_input[-1])

    def modulos(self, monkeys):
        return reduce(lambda x,y:x*y, [m.passing_op.divisble for m in monkeys])

    def perform(self, item, shrink, monkeys):
        value = item if self.use_old else self.value
        new_value = value
        if self.sign == '+':
            new_value = (item + value)
        if self.sign == '-':
            new_value = (item - value)
        if self.sign == '/':
            new_value = (item / value)
        if self.sign == '*':
            new_value = (item * value)
        
        return (new_value % self.modulos(monkeys)) if shrink else int(new_value / 3)

@dataclass
class Monkey:
    items: List[int]
    items_inspected = 0
    op: Operation
    passing_op: Passing

    def __init__(self, input):
        split_val = input[1].split(':')
        nums = split_val[1].replace(',', '')
        nums = nums.split()
        nums = list(map(int, nums))
        self.items = nums
        self.op = Operation(input[2])
        self.passing_op = Passing(input[3:])

    def add_item(self, item):
        self.items.append(item)

    def turn(self, monkey_list, shrink):
        new_monkeys = monkey_list
        # Inspect items in list 0...n
            # item_operations()
        for item in self.items:
            new_monkeys = self.item_operations(item, new_monkeys, shrink)
        else:
            self.items = []

        return new_monkeys

    def item_operations(self, item, monkey_list, shrink):
        new_item = self.op.perform(item, shrink, monkey_list)
        monkey_index = self.passing_op.check(new_item)
        new_list = monkey_list
        new_list[monkey_index].add_item(new_item)
        self.items_inspected += 1
        return new_list
