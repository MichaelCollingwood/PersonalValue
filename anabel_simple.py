import numpy as np
import pandas as pd
from utils import *


class AnabelSimple:
    def __init__(self, experience):
        self.trait_map = find_trait_map(experience)
        self.exp_names = list(experience.keys())
        self.exp_array = self.convert_to_array(experience)

    def convert_to_array(self, experience):
        exp_matrix = np.zeros((len(self.trait_map), len(experience)))
        for i, traits in enumerate(experience.values()):
            for trait in traits:
                exp_matrix[self.trait_map[trait], i] = 1

        return exp_matrix

    def find_relevant_experience(self, requirements):
        cross_section = np.zeros(len(self.trait_map))
        for requirement in requirements:
            cross_section[self.trait_map[requirement]] = 1

        values = np.matmul(cross_section, self.exp_array)
        return {name: value for name, value in zip(self.exp_names, values)}

    def visualise_experience(self):
        print(
            pd.DataFrame(
                self.exp_array,
                index=self.trait_map,
                columns=self.exp_names
            )
        )
