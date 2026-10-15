
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def print_station(station: dict[str, str]) -> None:
    print("Space Station Data Validation")
    print("========================================")
    print(f"ID:     {station["station_id"]}")
    print(f"Name:   {station["name"]}")
    print(f"Crew:   {station["crew_size"]} people")
    print(f"Power:  {station["power_level"]}%")
    print(f"Oxygen: {station["oxygen_level"]}%")

    if station["is_operational"]:
        print("Status: Operational")
    else:
        print("Status: Not operational")

    print("\n========================================")


def main() -> None:
    try:
        valid_station = SpaceStation(
            station_id="ST-Alpha",
            name="Orbital Outpost 1",
            crew_size=5,
            power_level=98.5,
            oxygen_level=99.1,
            last_maintenance=datetime(2023, 10, 24, 14, 30)
        )
        print_station(valid_station.model_dump())
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error["loc"][0]}: {error["msg"]}")

    try:
        invalid_station = SpaceStation(
            station_id="ST-Alpha",
            name="Orbital Outpost 1",
            crew_size=0,
            power_level=98.5,
            oxygen_level=99.1,
            last_maintenance=datetime(2023, 10, 24, 14, 30)
        )
        print_station(invalid_station.model_dump())
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error["loc"][0]}: {error["msg"]}")


if __name__ == "__main__":
    main()
