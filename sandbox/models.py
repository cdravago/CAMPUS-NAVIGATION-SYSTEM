class Location:
    def __init__(self, building_id: int, name: str, category: str):
        self.building_id = building_id
        self.name = name
        self.category = category

    def display_info(self):
        return f"[{self.building_id}] - {self.name}"