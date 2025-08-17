import requests
import urllib.parse

def query_overpass_api(roadway_name):

    query = f"""
    [out:json];
    (
        way["highway"~"motorway|trunk|primary"]["ref"="{roadway_name}"];
        node["place"~"city|town"](around:500);
    );
    out center;
    """
    
    overpass_url = "https://overpass-api.de/api/interpreter"
    encoded_query = urllib.parse.quote(query)
    response = requests.get(f"{overpass_url}?data={encoded_query}")
    
    if response.status_code != 200:
        raise Exception(f"Overpass API request failed: {response.status_code}")
    
    return response.json()