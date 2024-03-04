from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest

def test_get_determiner():
    single_determ = ["a", "one", "the"]
    plural_determ = ["some", "many", "the"]

    for x in range(4):
        determ = get_determiner(1)
        assert determ in single_determ
    
    for x in range(4):
        determ = get_determiner(2)
        assert determ in plural_determ

def test_get_noun():
    single_noun = ["dog", "food", "beast", "man", "boy", "woman", "girl", "rock", "book", "sword", "bird", "car", "cat", "child", "rabbit"]
    plural_noun = ["dogs", "foods", "beasts", "men", "boys", "women", "girls", "rocks", "books", "swords", "birds", "cars", "cats", "children", "rabbits"]

    for x in range(4):
        noun = get_noun(1)
        assert noun in single_noun
    
    for x in range(4):
        noun = get_noun(2)
        assert noun in plural_noun

def test_get_verb():
    verb_past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    single_verb_present = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    plural_verb_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    verb_future = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    for x in range(4):
        verb = get_verb(1, "past")
        assert verb in verb_past

    for x in range(4):
        verb = get_verb(1, "present")
        assert verb in single_verb_present

    for x in range(4):
        verb = get_verb(2, "present")
        assert verb in plural_verb_present

    for x in range(4):
        verb = get_verb(2, "future")
        assert verb in verb_future

def test_get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along", \
        "around", "at", "before", "behind", "below", \
        "beyond", "by", "despite", "except", "for", \
        "from", "in", "into", "near", "of", \
        "off", "on", "onto", "out", "over", \
        "past", "to", "under", "with", "without"
    ]
    for x in range(4):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():
    prepositions = [
        "about", "above", "across", "after", "along", \
        "around", "at", "before", "behind", "below", \
        "beyond", "by", "despite", "except", "for", \
        "from", "in", "into", "near", "of", \
        "off", "on", "onto", "out", "over", \
        "past", "to", "under", "with", "without"
    ]

    single_determiner = ["a", "one", "the"]
    plural_determiner = ["some", "many", "the"]

    single_noun = ["dog", "food", "beast", "man", "boy", "woman", "girl", "rock", "book", "sword", "bird", "car", "cat", "child", "rabbit"]
    plural_noun = ["dogs", "foods", "beasts", "men", "boys", "women", "girls", "rocks", "books", "swords", "birds", "cars", "cats", "children", "rabbits"]


    for x in range(4):
        prep_phrase = (get_prepositional_phrase(1)).split(" ")
        assert prep_phrase[0] in prepositions
        assert prep_phrase[1] in single_determiner
        assert prep_phrase[2] in single_noun
    
    for x in range(4):
        prep_phrase = (get_prepositional_phrase(2)).split(" ")
        assert prep_phrase[0] in prepositions
        assert prep_phrase[1] in plural_determiner
        assert prep_phrase[2] in plural_noun

    


pytest.main(["-v", "--tb=line", "-rN", __file__])