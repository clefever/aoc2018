from collections import defaultdict
from pathlib import Path

class Node:

    def __init__(self, num_child_nodes, num_metadata_entries, metadata_entries, child_nodes):
        self.num_child_nodes = num_child_nodes
        self.num_metadata_entries = num_metadata_entries
        self.metadata_entries = metadata_entries
        self.child_nodes = child_nodes

def parse_entries(arr):
    nodes = []
    if not arr:
        return nodes
    num_child_nodes = arr.pop(0)
    num_metadata_entries = arr.pop(0)
    metadata_entries = []
    if (num_child_nodes == 0):
        for j in range(num_metadata_entries):
            metadata_entries.append(arr.pop(0))
        node = Node(num_child_nodes, num_metadata_entries, metadata_entries, [])
        return [node]
    else:
        child_nodes = []
        for i in range(num_child_nodes):
            sub_nodes = parse_entries(arr)
            child_nodes.extend(sub_nodes)
            nodes.extend(sub_nodes)
        for j in range(num_metadata_entries):
            metadata_entries.append(arr.pop(0))
        for n in nodes:
            for c in n.child_nodes:
                if c in child_nodes:
                    child_nodes.remove(c)
        node = Node(num_child_nodes, num_metadata_entries, metadata_entries, child_nodes)
        nodes.append(node)
        return nodes

def calc_node_value(node):
    if (node.num_child_nodes == 0):
        return sum(node.metadata_entries)
    s = 0
    for index in node.metadata_entries:
        if index > 0 and index <= node.num_child_nodes:
            s += calc_node_value(node.child_nodes[index - 1])
    return s

def part1(input_str):
    entries = [int(s) for s in input_str.split(' ')]
    all_nodes = parse_entries(entries)
    s = 0
    for n in all_nodes:
        s += sum([int(m) for m in n.metadata_entries])
    print(s)

def part2(input_str):
    entries = [int(s) for s in input_str.split(' ')]
    all_nodes = parse_entries(entries)
    head = all_nodes[-1]
    print(calc_node_value(head))

def main():
    input_str = Path("input").read_text()
    part1(input_str)
    part2(input_str)

if __name__ == "__main__":
    main()
