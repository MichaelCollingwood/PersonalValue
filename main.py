from anabel_simple import AnabelSimple

x = {
    'Chai AI Optimisation project': ['machine learning', 'instance optimisation', 'self motivated'],
    'Cover Letter Optimisation': ['machine learning', 'instance optimisation', 'self motivated'],
    '4th Yr Project': ['machine learning', 'optimisation', 'self motivated', 'production',
                       'machine learning integration', 'signal analysis', 'statistical inference',
                       'boosted decision trees', 'pca']
}

# Simple model
r_simple = ['machine learning', 'self motivated', 'machine learning integration']

anabel = AnabelSimple(x)
anabel.visualise_experience()
anabel.find_relevant_experience(r_simple)

# Clever model
r_clever = ['artificial intelligence', 'self-motivation', 'optimization']

"""
use requirement distances from tags in word embedding space to rank experience relevancy
"""

# Brilliant model
r_brill = "You must be able to do artificial intelligence, it's integration and principle component analysis"

"""
find a sequence to fixed-length-vector mapping (transformers?) and compare to tag embeddings
"""
