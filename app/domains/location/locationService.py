from .locationDAO import LocationDAO
from .locationModel import LocationRequest, LocationResponse

class LocationService:

    def __init__(self):
        self.dao = LocationDAO()

    def create_location(self, location: LocationRequest) -> LocationResponse:
        return self.dao.create_location(location)

    def get_locations(self) -> list[LocationResponse]:
        return self.dao.get_locations()

    def get_location(self, location_id: int) -> LocationResponse:
        location = self.dao.get_location(location_id)
        if not location:
            raise ValueError(f"Location with id {location_id} not found")
        return location

    def close_connection(self):
        self.dao.close()
