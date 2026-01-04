from dataclasses import dataclass, field


@dataclass
class Quote:
    """Representation of a quotation."""
    text: str
    author: str
    author_url: str
    tags: list[str] = field(default_factory=list)
    
    def to_dict(self) -> dict:
        """Convert to a dictionary for MongoDB."""
        return {
            "text": self.text,
            "author": self.author,
            "author_url": self.author_url,
            "tags": self.tags
        }
