from dataclasses import dataclass

@dataclass
class Competition:
    external_id: int
    name: str
    logo: str
    country_name: str
    country_code: str
    country_logo: str
    footballdata_code: str