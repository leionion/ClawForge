import json
import time


class EvolutionRecorder:
    def __init__(self, data_path="data/evolution.json"):
        self.data_path = data_path


    def log(self, model, community, contributor_github, change):
        entry = {
            "timestamp": int(time.time()),
            "model": model,
            "community": community,
            "contributor_github": contributor_github,
            "change": change
        }
        try:
            with open(self.data_path, "r") as f:
                data = json.load(f)
        except:
            data = []
        data.append(entry)
        with open(self.data_path, "w") as f:
            json.dump(data, f, indent=2)
