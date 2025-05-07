class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if not member.get("id"):
            member["id"] = self._generate_id()
        if not member.get("last_name"):
            member["last_name"] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

    def update_member(self, id, member):
        for i, family_member in enumerate(self._members):
            if family_member["id"] == id:
                member["id"] = id
                if not member.get("last_name"):
                    member["last_name"] = self.last_name
                self._members[i] = member
                return True
        return False

    def get_member(self, id):
        for family_member in self._members:
            if family_member["id"] == id:
                return {
                    "first_name": family_member["first_name"],
                    "id": family_member["id"],
                    "age": family_member["age"],
                    "lucky_numbers": family_member["lucky_numbers"]
                }
        return None

    def get_all_members(self):
        return self._members
