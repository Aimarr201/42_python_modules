
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from typing import List, Any


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)

    crew: List[CrewMember] = Field(min_length=1, max_length=12)

    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_leadership = False
        experienced_count = 0
        total_crew = len(self.crew)

        for member in self.crew:
            if not member.is_active:
                raise ValueError(f"All crew members must be active. "
                                 f"{member.name} is inactive.")

            if member.rank in [Rank.captain, Rank.commander]:
                has_leadership = True

            if member.years_experience >= 5:
                experienced_count += 1

        if not has_leadership:
            raise ValueError("Mission must have at least one "
                             "Commander or Captain.")

        if self.duration_days > 365:
            percentage_experienced = experienced_count / total_crew
            if percentage_experienced < 0.5:
                raise ValueError("Long missions (> 365 days) require at least "
                                 "50% of crew to have 5+ years of experience.")

        return self


def print_mission(mission: dict[str, Any]) -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission:     {mission['mission_name']}")
    print(f"ID:          {mission['mission_id']}")
    print(f"Destination: {mission['destination']}")
    print(f"Duration:    {mission['duration_days']} days")
    print(f"Budget:      ${mission['budget_millions']}M")
    print(f"Crew size:   {len(mission['crew'])}")
    print("Crew members:")

    for member in mission['crew']:
        print(f"  - {member['name']} ({member['rank'].value}) - "
              f"{member['specialization']}")

    print("\n=========================================")


def main() -> None:
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 15, 10, 30, 00),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C01",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=38,
                    specialization="Mission Command",
                    years_experience=12,
                    is_active=True
                ),
                CrewMember(
                    member_id="C02",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=32,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="C03",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=29,
                    specialization="Engineering",
                    years_experience=4,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )

        print_mission(valid_mission.model_dump())

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))

    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 15, 10, 30, 0),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C01",
                    name="Sarah Connor",
                    rank=Rank.lieutenant,
                    age=38,
                    specialization="Mission Command",
                    years_experience=12,
                    is_active=True
                ),
                CrewMember(
                    member_id="C02",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=32,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )
        print_mission(invalid_mission.model_dump())
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
