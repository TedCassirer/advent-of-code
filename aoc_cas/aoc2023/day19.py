import dataclasses
from typing import Callable, Iterator
import re

pattern = re.compile(r"(\w+){(.+?)}")

@dataclasses.dataclass()
class Component:
    x: int
    m: int
    a: int
    s: int

    def score(self) -> int:
        return self.x + self.m + self.a + self.s

@dataclasses.dataclass(frozen=True)
class Rule:
    dest: str
    lo_x: int = 0
    hi_x: int = 4001
    lo_m: int = 0
    hi_m: int = 4001
    lo_a: int = 0
    hi_a: int = 4001
    lo_s: int = 0
    hi_s: int = 4001

    def evaluate(self, component: Component) -> str | None:
        if self.lower < component.__getattribute__(self.attr) < self.upper:
            return self.dest
        return None

    def join(self, other: Rule) -> Rule:



@dataclasses.dataclass(frozen=True)
class WorkFlow:
    label: str
    rules: list[Rule]

    def process_component(self, component: Component) -> str:
        i = 0
        dest = None
        while dest == None:
            dest = self.rules[i].evaluate(component)
            i += 1
        return dest

def parse_workflows(data: str) -> dict[str, WorkFlow]:
    rules_part, _ = data.split("\n\n")
    workflows = {}
    for line in rules_part.splitlines():
        label, workflow_part = pattern.findall(line)[0]
        rules: list[Rule]  = []
        *rule_strings, default = workflow_part.split(",")
        for rule_str in rule_strings:
            pred_part, dest = rule_str.split(":")
            attr, op, val = pred_part[0], pred_part[1], int(pred_part[2:])
            match op:
                case "<":
                    rules.append(Rule(lower=0, upper=val, attr=attr, dest=dest))
                case ">":
                    rules.append(Rule(lower=val, upper=4001, attr=attr, dest=dest))
        rules.append(Rule(lower=0, upper=4001, attr="x", dest=default))
        workflows[label] = WorkFlow(label=label, rules=rules)

    return workflows

def parse_components(data: str) -> Iterator[Component]:
    _, components_part = data.split("\n\n")
    for line in components_part.splitlines():
        x_str, m_str, a_str, s_str = line[1:-1].split(",")
        yield Component(
            x=int(x_str[2:]),
            m=int(m_str[2:]),
            a=int(a_str[2:]),
            s=int(s_str[2:]),
        )

def process_component(component: Component, workflows: dict[str, WorkFlow]) -> bool:
    current_label = "in"
    while current_label != "A" and current_label != "R":
        current_label = workflows[current_label].process_component(component)
    return current_label == "A"


def part_a(data: str) -> int:
    workflows = parse_workflows(data)
    total = 0
    for component in parse_components(data):
        if process_component(component, workflows):
            total += component.score()
    return total

def search(component: Component, workflows: dict[str, WorkFlow], attr: str) -> tuple[int, int]:


    start_val = component.__getattribute__(attr)
    lo, hi = 0, start_val

    while lo < hi-1:
        mid = (lo + hi) // 2
        component.__setattr__(attr, mid)
        if not process_component(component, workflows):
            hi = mid
        else:
            lo = mid
    lower_bound = hi

    lo, hi = start_val, 4000

    while lo < hi-1:
        mid = (lo + hi) // 2
        component.__setattr__(attr, mid)
        if not process_component(component, workflows):
            lo = mid
        else:
            hi = mid
    upper_bound = hi

    return lower_bound, upper_bound


def part_b(data: str) -> int:
    workflows = parse_workflows(data)
    total = 0
    for passing_component in parse_components(data):
        if process_component(passing_component, workflows):
            break
    else:
        raise ValueError("Something went wrong")

    search(passing_component, workflows, "x")
    return total

if __name__ == "__main__":
    from aoc_cas.util import solve_with_examples

    solve_with_examples(year=2023, day=19)
