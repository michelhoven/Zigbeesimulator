
import random

class AdaptiveAI:
    def __init__(self):
        self.history = []
        self.scenarios = [
            "Wake-up routine with light and music",
            "Fall detection alert",
            "Medication reminder",
            "Night orientation light",
            "Relaxation mode",
            "Hydration alert",
            "Visitor notification",
            "Sleep monitoring",
            "Day planning with light cues",
            "Emergency alert"
        ]

    def get_next_scenario(self):
        if self.history:
            return max(set(self.history), key=self.history.count)
        scenario = random.choice(self.scenarios)
        self.history.append(scenario)
        return scenario

    def process_command(self, command):
        self.history.append(command)
        return f"Processed command: {command}"
