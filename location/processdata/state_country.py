import overpy
import sys


def get_state_country( lat, lon):
    api = overpy.Overpass()
    ql = f"""
    [out:json];
    node(around:50, {lat}, {lon});
    is_in;
    area._["admin_level"~"2|4"];
    out body;
    """
    try:
        res = api.query(ql)
        country = None
        state = None
        for area in res.areas:
            level = area.tags.get("admin_level")
            name = area.tags.get("name")
            if level == "2":
                country = name
            elif level == "4":
                state = name        
        return state, country
    except Exception as e:
        print(f"Error getting admin: {e}", file=sys.stderr)
        return None, None