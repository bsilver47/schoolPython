import random

def main():
    quantities = [1, 2]
    quantity = random.choice(quantities)
    tenses = ["past", "present", "future"]
    tense = random.choice(tenses)
    sentence_a = get_sentence(quantities[0], tenses[0])
    sentence_b = get_sentence(quantities[0], tenses[1])
    sentence_c = get_sentence(quantities[0], tenses[2])
    sentence_d = get_sentence(quantities[1], tenses[0])
    sentence_e = get_sentence(quantities[1], tenses[1])
    sentence_f = get_sentence(quantities[1], tenses[2])
    sentence_r = get_sentence(quantity, tense)
    print(sentence_a)
    print(sentence_b)
    print(sentence_c)
    print(sentence_d)
    print(sentence_e)
    print(sentence_f)
    print(sentence_r)

def get_sentence(quantity, tense):
    article = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = (article + " " + noun + " " + verb + " " + prepositional_phrase + ".").capitalize()

    return sentence

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["dog", "food", "beast", "man", "boy", "woman", "girl", "rock", "book", "sword", "bird", "car", "cat", "child", "rabbit"]
    else:
        words = ["dogs", "foods", "beasts", "men", "boys", "women", "girls", "rocks", "books", "swords", "birds", "cars", "cats", "children", "rabbits"]
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense.find("future") != -1:
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    elif tense.find("present") != -1:
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    
    word = random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = [
        "about", "above", "across", "after", "along", \
        "around", "at", "before", "behind", "below", \
        "beyond", "by", "despite", "except", "for", \
        "from", "in", "into", "near", "of", \
        "off", "on", "onto", "out", "over", \
        "past", "to", "under", "with", "without"
    ]
    prep = random.choice(prepositions)
    return prep

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    prep = get_preposition()
    prep_det = get_determiner(quantity)
    direct_object = get_noun(quantity)

    prep_phrase = prep + " " + prep_det + " " + direct_object
    return prep_phrase

if __name__ == "__main__":
    main()