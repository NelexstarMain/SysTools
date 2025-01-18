import os
import json
import shutil
from typing import Dict, Any

class Parser:
    def __init__(self, path: str, removals_path: str, saving_path: str) -> None:
        self.path: str = path
        self.saving_path: str = saving_path
        self.removals_path: str = removals_path
        self.structure: Dict[str, Any] = {}
        self.removals: list = []

    def get_removals(self) -> None:
        """Wczytuje dane z pliku removals.json i zapisuje je do listy removals"""
        try:
            if os.path.exists(self.removals_path):
                with open(self.removals_path, "r") as removals:
                    self.removals = json.load(removals)
                    print(f"Successfully loaded removals: {self.removals}")
            else:
                print(f"File {self.removals_path} not found.")
                self.removals = []
        except PermissionError:
            print(f"Permission denied: cannot read {self.removals_path}")
            self.removals = []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {self.removals_path}: {e}")
            self.removals = []

    def save_to_json(self) -> None:
        """Zapisuje strukturę katalogów do pliku JSON"""
        try:
            with open(self.saving_path, "w") as f:
                json.dump(self.structure, f, indent=4)
            print(f"Structure saved in {self.saving_path}")
        except PermissionError:
            print(f"Permission denied: cannot write to {self.saving_path}")

    def scan_directory(self) -> Dict[str, Any]:
        """Przeszukuje katalogi, ignorując niepożądane foldery i pliki"""
        for root, dirs, files in os.walk(self.path, topdown=True):
            dirs[:] = [d for d in dirs if d not in self.removals]

            current_level = self.structure
            parts = os.path.relpath(root, self.path).split(os.sep)
            for part in parts:
                if part == '.':
                    continue
                current_level = current_level.setdefault(part, {})

            for file in files:
                if not file.startswith('.') and not file.endswith(('.pyc', '.pyo', '.git', '.DS_Store')):
                    current_level[file] = None

        return self.structure
