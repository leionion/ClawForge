class Cutter:
    def __init__(self, community="unknown", current_model="gpt"):
        self.community = community
        self.current_model = current_model
        self.prompt_path = f"prompts/{current_model}/main.txt"


    def parse_demand(self, human_demand, github_id="unknown"):
        return Demand(
            human_demand=human_demand,
            dc_github=github_id,
            community=self.community
        )
