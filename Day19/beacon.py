class Beacon:
    def __init__(self, scanner_id, x_coordinate, y_coordinate, z_coordinate) -> None:
        self.scanner_id = scanner_id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.z_coordinate = z_coordinate

    def get_offset_to_other_beacon(self, other: Beacon):
        return tuple(self.x_coordinate - other.x_coordinate, 
        self.y_coordinate - other.y_coordinate,
        self.z_coordinate - other.z_coordinate)
    
    def get_distance_to_other_beacon(self, other:Beacon):
        distance =  (self.x_coordinate - other.x_coordinate) ** 2 + (self.y_coordinate - other.y_coordinate) ** 2 
        +  (self.z_coordinate - other.z_coordinate) ** 2

        return distance
    
    
    

    

