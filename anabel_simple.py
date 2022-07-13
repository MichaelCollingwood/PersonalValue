import numpy as np
import pandas as pd
from utils import *


class AnabelSimple:
    def __init__(self, experience):
        self.tag_map = find_tag_map(experience)
        self.exp_names = list(experience.keys())
        self.exp_array = self.convert_to_array(experience)

    def convert_to_array(self, experience):
        exp_matrix = np.zeros((len(self.tag_map), len(experience)))
        for i, tags in enumerate(experience.values()):
            for tag in tags:
                exp_matrix[self.tag_map[tag], i] = 1

        return exp_matrix

    def find_relevant_experience(self, requirements):
        cross_section = np.zeros(len(self.tag_map))
        for requirement in requirements:
            cross_section[self.tag_map[requirement]] = 1

        values = np.matmul(cross_section, self.exp_array)
        return {name: value for name, value in zip(self.exp_names, values)}

    def visualise_experience(self):
        print(
            pd.DataFrame(
                self.exp_array,
                index=self.tag_map,
                columns=self.exp_names
            )
        )
