import mycode


def test_add():
    '''Define a function add() that adds two numbers.'''
    assert mycode.add(2, 3) == 5
    assert mycode.add(-2, 2) == 0
    assert mycode.add(92, 8) == 100
    assert mycode.add(-5, -5) == -10


def test_rectangular_prism_area():
    '''Define a function rectangular_prism_area() that calculates the area
       of a rectangular prism given it's length, width, and height.'''
    assert mycode.rectangular_prism_area(1, 1, 1) == 1
    assert mycode.rectangular_prism_area(2, 2, 2) == 8
    assert mycode.rectangular_prism_area(2, 3, 4) == 24
    assert mycode.rectangular_prism_area(0.25, 4, 8) == 8


def test_sum():
    '''Define a variadic function that sums all given numbers.'''
    assert mycode.sum(1) == 1
    assert mycode.sum(2, 3) == 5
    assert mycode.sum(-2, 2, 4) == 4
    assert mycode.sum(-5, -2, -3) == -10
    assert mycode.sum(1, 1, 1, 1, 1, 1, 1, 1, 1, 1,) == 10


def test_sentence_sepearate():
    '''Define a function sentence_seperate() that seperates a string into
       an array of words. Leaving punctuation as part of a word is OK.'''
    assert mycode.sentence_seperate("This") == ["This"]
    assert mycode.sentence_seperate("This is a test.") == [
        "This", "is", "a", "test."]


def test_fibb():
    '''Define a function fibb() that calculates the nth (zero-indexed)
       fibbonaci number (eg. 1, 1, 2, 3, 5, 8, 13, ...).'''
    assert mycode.fibb(0) == 1
    assert mycode.fibb(1) == 1
    assert mycode.fibb(5) == 8
    assert mycode.fibb(15) == 987


def test_fibb_arr():
    '''Define a function fibb_arr(n) that generates a list of the fibonacci
    sequence up to (non inclusive) the nth (zero-indexed) element.'''
    assert mycode.fibb_arr(0) == []
    assert mycode.fibb_arr(2) == [1, 1]
    assert mycode.fibb_arr(9) == [1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fibb_gen():
    '''Define a function fibb() that returns a generator for the fibonacci
       sequence.'''
    gen = mycode.fibb_gen()

    a = []
    for i, x in enumerate(gen):
        a.append(x)
        if i > 10:
            return

    assert a == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_letter_count():
    '''Define a function letter_count() that counts the amount of letters in
       a given string and returns a map of those letters to their count.
       Uppercase and Lowercase letters should be counted under the lowercase
       letter.'''
    occurrence = mycode.letter_count("aaAbaZeEE")

    assert occurrence['a'] == 4
    assert occurrence['b'] == 1
    assert occurrence['z'] == 1
    assert occurrence['e'] == 3


def test_person():
    '''Define a class Person that accepts a first and last name, and an age.
       Define the following methods on that class: can_vote(), full_name(),
       and get_names(). See the behavior defined below for reference'''
    p = mycode.Person("Linus", "Torvalds", 18)

    assert p.can_vote() == True
    assert p.full_name() == "Linus Torvalds"

    first, last = p.get_names()

    assert first == "Linus"
    assert last == "Torvalds"

    p2 = mycode.Person("John", "Doe", 17)
    assert p2.can_vote() == False


def test_hsstudent():
    '''Define a class HSStudent that inherits Person but also takes grade, and
       has a method is_upper_classman() that returns whether the high school
       student is an upperclassman (junior or senior).'''
    p = mycode.HSStudent("John", "Doe", 15, 10)

    assert p.can_vote() == False
    assert p.full_name() == "John Doe"
    assert p.get_names() == ("John", "Doe")
    assert p.is_upper_classman() == False

    p2 = mycode.HSStudent("John", "Doe", 18, 11)

    assert p2.is_upper_classman() == True
