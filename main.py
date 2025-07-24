import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple

try:
    import tkinter as tk
except ImportError:
    tk = None

AREA_NAMES = ["RATS", "RESUS", "MAJORS", "ACA", "CHILDREN'S ED", "UTC"]
AREA_LAYOUT = {
    "RATS": (10, 10, 130, 110),
    "RESUS": (150, 10, 270, 110),
    "MAJORS": (290, 10, 410, 110),
    "ACA": (430, 10, 550, 110),
    "CHILDREN'S ED": (10, 130, 130, 230),
    "UTC": (150, 130, 270, 230),
}

@dataclass
class Event:
    location: str
    time: datetime

@dataclass
class Patient:
    patient_id: str
    arrival: datetime
    events: List[Event]
    departure: datetime


def load_patients(path: str) -> List[Patient]:
    patients = []
    with open(path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            if not row:
                continue
            pid = row[0]
            arrival = datetime.fromisoformat(row[1])
            events: List[Event] = []
            # columns 2..-2 contain location/time pairs
            i = 2
            while i < len(row) - 1:
                loc = row[i]
                t = datetime.fromisoformat(row[i+1])
                events.append(Event(loc, t))
                i += 2
            departure = datetime.fromisoformat(row[-1])
            patients.append(Patient(pid, arrival, events, departure))
    return patients


def visualize(patients: List[Patient]):
    if tk is None:
        raise RuntimeError("tkinter not available")
    root = tk.Tk()
    root.title("Patient Flow Modeller")
    canvas = tk.Canvas(root, width=600, height=300, bg="white")
    canvas.pack()
    # draw areas
    for name, (x1, y1, x2, y2) in AREA_LAYOUT.items():
        canvas.create_rectangle(x1, y1, x2, y2, outline="black")
        canvas.create_text((x1+x2)//2, y1+10, text=name, anchor="n")

    patient_icons = {}
    for patient in patients:
        # start patient at arrival location (first event)
        if patient.events:
            loc = patient.events[0].location
        else:
            loc = AREA_NAMES[0]
        x1, y1, x2, y2 = AREA_LAYOUT.get(loc, (10,10,30,30))
        icon = canvas.create_oval(x1+5, y1+20, x1+15, y1+30, fill="blue")
        patient_icons[patient.patient_id] = icon

    root.mainloop()


def main():
    parser = argparse.ArgumentParser(description="Patient Flow Modeller")
    parser.add_argument("csv_file", help="Path to CSV containing patient events")
    parser.add_argument("--no-gui", action="store_true", help="Run without GUI")
    args = parser.parse_args()

    patients = load_patients(args.csv_file)
    if args.no_gui:
        print(f"Loaded {len(patients)} patients")
    else:
        visualize(patients)


if __name__ == "__main__":
    main()
