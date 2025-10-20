from datetime import date

STAGES = ["novo"]

class BaseLead:
    def __init__(self, name: str, company: str, email: str, stage: str = "novo", created: str = None):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created = created if created else date.today().isoformat()

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created,
        }

class Lead(BaseLead):
    def __init__(self, name: str, company: str, email: str, stage: str = "novo", created: str = None):
        super().__init__(name, company, email, stage, created)
