import argparse
import json

from  .solution import get_roadway_places
from  .process_data import processdata

parser = argparse.ArgumentParser()
parser.add_argument("--l","--location", 
                    help="location argument must be provided", type=str)
args = parser.parse_args()
if args.l == None:
    print("Provide loction (--l)")
else:
   location = args.l

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    print("Geospatial data for roadway and nearby cities/towns within 500 meters of the roadway: ", location)
    places = get_roadway_places(location)
    places_processed = processdata(places,location )
    save_to_json(places_processed, location.replace(' ', '_')+"_places.json")

