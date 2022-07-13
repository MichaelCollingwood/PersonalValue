def find_trait_map(experience):
    all_traits = []
    for traits in experience.values():
        all_traits += traits
    return {trait: i for i, trait in enumerate(set(all_traits))}