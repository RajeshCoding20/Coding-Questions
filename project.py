import random

QUESTION_BANK = {
    "programming basics": {
        "python": [
            ("What keyword is used to define a function in Python?",
             ["func", "define", "def", "lambda"], "def"),
            ("Which data type is immutable?",
             ["List", "Dictionary", "Set", "Tuple"], "Tuple"),
            ("Which operator is used for exponent in Python?",
             ["^", "**", "//", "++"], "**")
        ],
        "java": [
            ("Which keyword is used to create an object?",
             ["new", "class", "init", "create"], "new"),
            ("Which data type is NOT primitive?",
             ["int", "float", "String", "char"], "String"),
            ("Which OOP concept allows multiple methods with same name?",
             ["Inheritance", "Overloading", "Interface", "Package"], "Overloading")
        ]
    },

    "oop concepts": {
        "python": [
            ("Which concept hides internal details from users?",
             ["Encapsulation", "Inheritance", "Abstraction", "Polymorphism"], "Abstraction"),
            ("__init__() is also called?",
             ["Destructor", "Initializer", "Constructor", "Invoker"], "Constructor"),
            ("Which OOP concept allows reusing parent class properties?",
             ["Encapsulation", "Inheritance", "Aggregation", "Overriding"], "Inheritance")
        ],
        "java": [
            ("Which OOP concept allows a subclass to use parent methods?",
             ["Abstraction", "Interface", "Inheritance", "Polymorphism"], "Inheritance"),
            ("What is runtime polymorphism in Java?",
             ["Method Overloading", "Method Overriding", "Constructor Calling", "Abstract Method"],
             "Method Overriding"),
            ("What keyword prevents overriding?",
             ["static", "const", "final", "override"], "final")
        ]
    }
}

def fuzzy_match(user_input, options):
    user_input = user_input.replace(" ", "").lower()
    for opt in options:
        simplified = opt.replace(" ", "").lower()
        if user_input in simplified:
            return opt
    return None

def generate_questions(category, language, count):
    questions = QUESTION_BANK[category][language]
    selected = random.sample(questions, min(count, len(questions)))
    output = []
    q_no = 1
    for q, options, answer in selected:
        random.shuffle(options)
        output.append(f"{q_no}. {q}")
        for i, opt in enumerate(options):
            output.append(f"   {chr(97+i)}) {opt}")
        output.append(f"   Correct Answer: {answer}\n")
        q_no += 1
    return "\n".join(output)

print("=== Automated Interview Question Generator ===")

available_categories = list(QUESTION_BANK.keys())
print("\nCategories Available:")
for c in available_categories:
    print("-", c.title())

category_input = input("\nSelect a category: ")
matched_category = fuzzy_match(category_input, available_categories)

if not matched_category:
    print("\nInvalid category!")
    exit()

available_languages = list(QUESTION_BANK[matched_category].keys())
print("\nLanguages Available:")
for l in available_languages:
    print("-", l.title())

language_input = input("\nSelect a language: ")
matched_language = fuzzy_match(language_input, available_languages)

if not matched_language:
    print("\nInvalid language!")
    exit()

count = int(input("\nHow many questions do you want ? "))

print("\nGenerated Interview Questions:\n")
print(generate_questions(matched_category, matched_language, count))
