import csv
import os
from datetime import datetime


class FileManager:
    """A class to manage saving and loading scores to a CSV file."""

    file_path = "scores.csv"

    def save_score(self, player_name, score):
        file_exists = os.path.exists(self.file_path)
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["name", "score", "date"])
            writer.writerow([player_name, score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    def load_scores(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            scores = [row for row in reader]
            return  sorted(scores, key=lambda x: int(x['score']), reverse=True)