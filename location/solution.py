import json
from .processdata.query_api import query_overpass_api
# from process_data import processdata

def get_roadway_places(roadway_name):
    try:
        
        data = query_overpass_api(roadway_name)
        
        # Process the data
        # result = processdata(data, roadway_name)

        return data
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    print("__name__")
    print(__name__)
    roadway = "I 95"
    places = get_roadway_places(roadway)
    save_to_json(places, roadway.replace(' ', '_')+"_places.json")