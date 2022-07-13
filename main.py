from anabel_simple import AnabelSimple

x = {
    'Chai AI Optimisation project': ['machine learning', 'instance optimisation', 'self motivated'],
    'Cover Letter Optimisation': ['machine learning', 'instance optimisation', 'self motivated'],
    '4th Yr Project': ['machine learning', 'optimisation', 'self motivated', 'production',
                       'machine learning integration', 'signal analysis', 'statistical inference',
                       'boosted decision trees', 'pca']
}

r = ['machine learning', 'pca', 'machine learning integration']

# Simple model
anabel = AnabelSimple(x)
anabel.visualise_experience()
anabel.find_relevant_experience(r)

# Less simple model

