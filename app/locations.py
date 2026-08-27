from dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    canonical_id: str
    navigation_anchor: str
    aliases: tuple[str, ...]


LOCATIONS: tuple[Location, ...] = (
    Location(
        canonical_id="Entrance",
        navigation_anchor="NAV_Entrance",
        aliases=("entrada", "entrada principal", "entrance"),
    ),
    Location(
        canonical_id="Reception",
        navigation_anchor="NAV_Reception",
        aliases=("recepción", "recepcion", "reception"),
    ),
    Location(
        canonical_id="NorthHallway",
        navigation_anchor="NAV_NorthHallway",
        aliases=("pasillo norte", "north hallway", "north corridor"),
    ),
    Location(
        canonical_id="Classroom101",
        navigation_anchor="NAV_Classroom101",
        aliases=(
            "salón 101",
            "salon 101",
            "salón101",
            "salon101",
            "classroom 101",
            "classroom101",
        ),
    ),
)


def _normalize(value: str) -> str:
    return " ".join(value.strip().lower().split())


def resolve_location(value: str | None) -> Location | None:
    if not value:
        return None

    normalized = _normalize(value)
    for location in LOCATIONS:
        candidates = (location.canonical_id, location.navigation_anchor, *location.aliases)
        if normalized in {_normalize(candidate) for candidate in candidates}:
            return location
    return None
