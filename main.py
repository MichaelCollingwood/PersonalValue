# Assist cover letter writing by linking experiences with requirements for job

experience = [
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Chai AI Optimisation project', ['machine learning', 'instance optimisation', 'self motivated']),
    ('Cover Letter Optimisation', ['machine learning', 'instance optimisation', 'self motivated']),
    ('4th Yr Project', ['machine learning', 'optimisation', 'self motivated', 'production', 'machine learning integration', 'signal analysis', 'statistical inference', 'boosted decision trees', 'pca'])
]


def find_traits():
    traits = []

    for exp in experience:
        traits = list(set(traits + exp[1]))

    return traits


def find_relevant_experience(requirements):
    relevant_experience = []

    for exp in experience:
        if exp[1] in requirements:
            if (exp[0] in relevant_experience):
                relevant_experience[exp[0]] += 1
            else:
                relevant_experience[exp[0]] = 1

    return relevant_experience


def table_experiences_traits():
    max_name_len = 20
    margin = 30
    assert max_name_len <= margin

    traits = find_traits()
    exp_names = [exp[0] for exp in experience]
    grid = [[trait in exp[1] for trait in traits] for exp in experience]

    # print
    grid_strings = [' | '.join([f"{str(element)}{''.join([' ']*(max_name_len-len(str(element))))}" for element in row]) + " |" for row in grid]

    traits_strings = [f"{trait[:max_name_len] + ''.join([' ']*(max_name_len-len(trait[:max_name_len])))}" for trait in traits]
    header_string = "| " + f"{''.join([' ']*margin)}| " + ' | '.join(traits_strings) + " |"

    entry_strings = ["| " + f"{name[:max_name_len]}{''.join([' ']*(margin-len(name[:max_name_len])))}| " for name in exp_names]
    entry_strings = [entry + row_string for entry, row_string in zip(entry_strings, grid_strings)]

    print(''.join(['-']*(len(header_string))))
    print(header_string)
    print(''.join(['-']*len(header_string)))
    for row_string in entry_strings:
        print(row_string)
    print(''.join(['-'] * len(header_string)))

# table_experiences_traits()
