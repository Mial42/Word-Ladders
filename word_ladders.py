import time
import sys
from collections import deque

start = time.perf_counter()

letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
dictionary = {} #The plan: word:list of words one letter away #sys.argv[1] = dictionary.txt, sys.argv[2] = word_ladder_tests.txt


def create_set(filename):
    mywords = set()
    with open(filename) as f:
        for line in f:
            mywords.add(line.strip())
    return mywords


mywords = create_set(sys.argv[1])


def swap(word, index, letter):
    word = list(word)
    word[index] = letter
    return ''.join(word)


def generate_child_words(word):
    children = []
    for i in range(0, len(word)):
        for letter in letters:
            x = swap(word, i, letter)
            if x in mywords:
                children.append(x)
    return children


def create_dictionary():
    dictionary = {}
    for x in mywords:
        dictionary[x] = generate_child_words(x)
    return dictionary


dictionary = create_dictionary()

end = time.perf_counter()
time_to_make_data_structure = end - start

def bfs_shortest_path(start, goal):
    fringe = deque()
    visited = set()
    record = {start:None}  #State:Parent
    fringe.append(start)
    visited.add(start)
    while len(fringe) > 0:
        v = fringe.popleft()
        parent = v
        if v == goal:
            key = v
            path = []
            while key is not None:
                path.append(key)
                key = record[key]
            return len(path), path[::-1] #Return the length of the shortest path and the path, in that order
        children = dictionary[v]
        for child in children:
            if child is not None and child not in visited:
                fringe.append(child)
                visited.add(child)
                record[child] = parent #This is correct
    return None, None


def print_the_answers(filename):
    with open(filename) as f:
        x = 0
        for line in f:
            words = line.strip().split(' ')
            length, path = bfs_shortest_path(words[0], words[1])
            print("Line: " + str(x))
            if length is not None and path is not None:
                print("Length is: " + str(length))
                for state in path:
                    print(state)
                print()
            else:
                print("No solution!")
                print()
            x = x + 1


print("Time to create the data structure was: " + str(time_to_make_data_structure) + " seconds")
print("There are " + str(len(mywords)) + " words in this dict.")
print()
start = time.perf_counter()
print_the_answers(sys.argv[2])
end = time.perf_counter()
print("Time to solve all of these puzzles was: " + str(end - start) + " seconds")
