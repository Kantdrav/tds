from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

students_data = []
with open("q-fastapi.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row["studentId"] = int(row["studentId"])
        students_data.append(row)

@app.get("/api")
def get_students(class_: List[str] = Query(None, alias="class")):
    if class_:
        filtered = [s for s in students_data if s["class"] in class_]
        return {"students": filtered}
    return {"students": students_data}

