from flask import Blueprint, request, jsonify
from database.models import PollingBooth

booth_bp = Blueprint('booth', __name__)

@booth_bp.route('/api/booth/find', methods=['POST'])
def find_booth():
    data = request.json
    pincode = data.get('pincode')
    
    if pincode:
        booths = PollingBooth.query.filter_by(pincode=pincode).all()
    else:
        # Just return some defaults if no pincode provided
        booths = PollingBooth.query.limit(5).all()
        
    result = []
    for b in booths:
        result.append({
            "booth_number": b.booth_number,
            "name": b.booth_name,
            "address": b.address,
            "blo_name": b.blo_name,
            "latitude": b.latitude,
            "longitude": b.longitude,
            "facilities": {
                "wheelchair": b.has_wheelchair_access,
                "water": b.has_water_facility,
                "shade": b.has_shade_facility
            }
        })
        
    return jsonify(result), 200
