import copy


def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


class Workflow:
    def __init__(self, name, line):
        self.name = name
        # print(line)
        conditions = line.split(',')
        # print(conditions)
        self.conditions = []
        self.outcomes = {}
        for condition in conditions:
            *c, v = condition.split(':')
            self.conditions.append(c[0] if c else None)
            self.outcomes[c[0] if c else None] = v
        # print(self.conditions)
        # print(self.outcomes)

    def __repr__(self):
        return repr(self.outcomes)


class Part:
    def __init__(self, line):
        assert line[0] == '{' and line[-1] == '}'
        line = line[1:-1]
        ratings = line.split(',')
        self.values = {}
        for rating in ratings:
            letter, value = rating.split('=')
            value = int(value)
            self.values[letter] = value
        self.state = 'in'

    def __repr__(self):
        return repr(self.values)

    @property
    def total(self):
        return sum(self.values.values())

    def process(self, workflows):
        while self.state not in ('R', 'A'):
            workflow = workflows[self.state]
            for condition in workflow.conditions:
                if condition is None:
                    self.state = workflow.outcomes[condition]
                    break
                letter, fn = parse_condition(condition)
                if fn(self.values[letter]):
                    self.state = workflow.outcomes[condition]
                    break
        # print(self, self.state)
        return self


def parse_condition(string):
    assert string[0] in 'xmas' and string[1] in '><'
    letter = string[0]
    fn = "lambda x: x" + string[1:]
    return letter, eval(fn)


def part_one(data):
    workflows = {}
    for i, line in enumerate(data):
        if not line:
            break
        name, line = line.split('{')
        assert line[-1] == '}'
        line = line[:-1]
        workflows[name] = Workflow(name, line)
    parts = [Part(line) for line in data[i+1:]]
    parts = [part.process(workflows) for part in parts]
    print(sum(part.total for part in parts if part.state == 'A'))


class PartsGroup:
    def __init__(self, state, **values):
        self.state = state
        self.values = values

    def __repr__(self):
        return f"{repr(self.values)}: {self.state}"

    @property
    def x(self):
        return self.values['x']

    @property
    def m(self):
        return self.values['m']

    @property
    def a(self):
        return self.values['a']

    @property
    def s(self):
        return self.values['s']

    @staticmethod
    def size_range(tpl):
        assert len(tpl) == 2
        return tpl[1] - tpl[0] + 1

    @property
    def combinations(self):
        return self.size_range(self.x) * self.size_range(self.m) * \
            self.size_range(self.a) * self.size_range(self.s)


def parse_condition2(string):
    assert string[0] in 'xmas' and string[1] in '><'
    a, b, *c = string
    return a, b, int(''.join(c))


def split_groups(parts_group, workflow):
    processed_groups = []
    for condition in workflow.conditions:
        if condition is None:
            parts_group.state = workflow.outcomes[condition]
            processed_groups.append(parts_group)
            break
        letter, ineq, value = parse_condition2(condition)
        lo, hi = parts_group.values[letter]
        if value not in range(lo, hi + 1):
            continue
        # clone group
        finished_group = copy.deepcopy(parts_group)
        if ineq == '<':
            finished_group.values[letter] = lo, value - 1
            finished_group.state = workflow.outcomes[condition]
            parts_group.values[letter] = value, hi
        elif ineq == '>':
            finished_group.values[letter] = value + 1, hi
            finished_group.state = workflow.outcomes[condition]
            parts_group.values[letter] = lo, value
        else:
            raise ValueError
        processed_groups.append(finished_group)
    return processed_groups


def part_two(data):
    workflows = {}
    for i, line in enumerate(data):
        if not line:
            break
        name, line = line.split('{')
        assert line[-1] == '}'
        line = line[:-1]
        workflows[name] = Workflow(name, line)

    groups = [PartsGroup(state='in', x=(1, 4000), m=(1, 4000), a=(1, 4000), s=(1, 4000))]

    while any(group.state not in ('R', 'A') for group in groups):
        temp_groups = []
        for group in groups:
            if group.state in ('R', 'A'):
                temp_groups.append(group)
            else:
                new_groups = split_groups(group, workflows[group.state])
                temp_groups += new_groups
        groups = temp_groups

    print(sum(group.combinations for group in groups if group.state == 'A'))


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
