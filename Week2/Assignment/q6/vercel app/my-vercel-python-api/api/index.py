import json
import os

def handler(request, response):
    response.headers['Access-Control-Allow-Origin'] = '*'

    # Get the absolute path to data.json
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, '..', 'data.json')

    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        return response.status(500).json({"error": f"Failed to load data: {str(e)}"})

    names = request.query.getlist("name")
    name_to_marks = {entry["name"]: entry["marks"] for entry in data}
    marks = [name_to_marks.get(name, None) for name in names]

    return response.json({"marks": marks})

