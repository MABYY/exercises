from  .processdata.state_country import get_state_country
# from  processdata.state_country import get_state_country

def processdata(data, roadway_name):
    output = []
    
    roadway = None
    for element in data['elements']:
        if element['type'] == 'way' and 'ref' in element['tags']:
            roadway = element['tags']['ref']
            break
    
    if not roadway:
        return output  
    
    for element in data['elements']:
        if element['type'] == 'node' and 'place' in element['tags']:
            place_tags = element['tags']
            place_type = place_tags.get('place', '')
            
            if place_type in ['city', 'town']:
           
                state, country = get_state_country(element.get('lat', 0.0), element.get('lon', 0.0))
                
                place_data = {
                    "roadway": roadway_name,
                    "placename": place_tags.get('name', ''),
                    "placename_ascii": place_tags.get('name', ''),
                    "placename_en": place_tags.get('name:en', place_tags.get('name', '')),
                    "placetag": place_type,
                    "latitude": element.get('lat', 0.0),
                    "longitude": element.get('lon', 0.0),
                    "state/province": state,
                    "state/province-ascii": state,
                    "country": country
                }
                output.append(place_data)
    
    return output