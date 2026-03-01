class Demand:
    def __init__(self, human_demand, dc_github, community):
        self.human_demand = human_demand
        self.dc_github = dc_github
        self.community = community
        self.decomposed_skills = []


    def to_markdown(self):
        return "# Decomposition Result\n" + self.human_demand
