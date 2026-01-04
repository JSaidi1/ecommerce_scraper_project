from dataclasses import dataclass


@dataclass
class Author:
    """Representation of an author."""
    name: str
    bio: str = ""
    born_date: str = ""
    born_location: str = ""
    url: str = ""
    
    def to_dict(self) -> dict:
        """Convert to a dictionary for MongoDB."""
        return {
            "name": self.name,
            "bio": self.bio,
            "born_date": self.born_date,
            "born_location": self.born_location,
            "url": self.url
        }
