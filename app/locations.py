from dataclasses import dataclass
import unicodedata


@dataclass(frozen=True)
class Location:
    canonical_id: str
    navigation_anchor: str
    aliases: tuple[str, ...]


LOCATIONS: tuple[Location, ...] = (
    Location("Arte", "NAV_Arte", ("arte", "edificio de arte")),
    Location("CAI", "NAV_CAI", ("cai", "centro de acceso a la información", "centro de acceso a la informacion", "biblioteca", "biblioteca cai")),
    Location("CampusSchool", "NAV_CampusSchool", ("campus school", "escuela san germán interamericana", "escuela san german interamericana")),
    Location("CampusSchoolExtension", "NAV_CampusSchoolExtension", ("campus school extension", "extensión campus school", "extension campus school")),
    Location("CentroCuidoVeve", "NAV_CentroCuidoVeve", ("centro de cuido dr veve cottage", "veve cottage", "centro de cuido veve")),
    Location("CentroCuidoMountainView", "NAV_CentroCuidoMountainView", ("centro de cuido mountain view", "mountain view")),
    Location("CentroEstudiantes", "NAV_CentroEstudiantes", ("centro de estudiantes", "centro de estudiantes james r beverley", "james r beverley")),
    Location("CentroReligioso", "NAV_CentroReligioso", ("centro religioso", "capilla", "capilla paul a wolfe", "fellowship hall", "centro de consejería", "centro de consejeria")),
    Location("CIT", "NAV_CIT", ("cit", "centro de informática", "centro de informatica")),
    Location("CostelloHall", "NAV_CostelloHall", ("costello hall", "costello hall música", "costello hall musica")),
    Location("EscuelaEnfermeria", "NAV_EscuelaEnfermeria", ("escuela de enfermería", "escuela de enfermeria", "enfermería", "enfermeria")),
    Location("EscuelaGraduada", "NAV_EscuelaGraduada", ("escuela graduada", "estudios graduados", "escuela de estudios graduados")),
    Location("FigueroaMusica", "NAV_FigueroaMusica", ("figueroa música", "figueroa musica", "figueroa")),
    Location("GoodyearMusica", "NAV_GoodyearMusica", ("goodyear música", "goodyear musica", "goodyear")),
    Location("GuillespieCottage", "NAV_GuillespieCottage", ("guillespie cottage", "guillespie cottage música", "guillespie cottage musica")),
    Location("HarrisHall", "NAV_HarrisHall", ("harris hall",)),
    Location("InterTecHarrisHouse", "NAV_InterTecHarrisHouse", ("inter tec harris house", "intertec harris house", "harris house")),
    Location("InterTecBelleza", "NAV_InterTecBelleza", ("inter tec belleza", "intertec belleza", "belleza")),
    Location("InterTecRecordingStudio", "NAV_InterTecRecordingStudio", ("inter tec recording studio", "intertec recording studio", "recording studio")),
    Location("MarquisScienceHall", "NAV_MarquisScienceHall", ("marquis science hall", "edificio marquis", "marquis")),
    Location("PhrannerExtension", "NAV_PhrannerExtension", ("phranner extension", "extensión phranner", "extension phranner")),
    Location("PhrannerHall", "NAV_PhrannerHall", ("phranner hall", "phranner")),
    Location("PistaSambolin", "NAV_PistaSambolin", ("pista luis f sambolín", "pista luis f sambolin", "pista sambolín", "pista sambolin")),
    Location("PolydeportivoSambolin", "NAV_PolydeportivoSambolin", ("polydeportivo luis f sambolín", "polydeportivo luis f sambolin", "polydeportivo", "polideportivo")),
    Location("ProyectoCASA", "NAV_ProyectoCASA", ("proyecto casa",)),
    Location("ResidenciaDamas", "NAV_ResidenciaDamas", ("residencia de damas eunice white harris", "residencia de damas", "eunice white harris")),
    Location("ResidenciaVarones", "NAV_ResidenciaVarones", ("residencia de varones angel archilla cabrera", "residencia de varones", "angel archilla cabrera")),
    Location("SenadoAcademico", "NAV_SenadoAcademico", ("senado académico", "senado academico")),
    Location("SmithCottageSBTDC", "NAV_SmithCottageSBTDC", ("smith cottage sbtdc", "smith cottage", "sbtdc")),
    Location("EusebioLopezAdmin", "NAV_EusebioLopezAdmin", ("edificio eusebio lópez", "edificio eusebio lopez", "eusebio lópez", "eusebio lopez", "rectoría", "rectoria", "decanato académico", "decanato academico", "decanato de administración", "decanato de administracion", "tecnología médica", "tecnologia medica")),
    Location("TorresHall", "NAV_TorresHall", ("torres hall",)),
    Location("WilsonCottage", "NAV_WilsonCottage", ("wilson cottage", "wilson cottage música", "wilson cottage musica")),
)


def _normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return " ".join(value.strip().lower().replace("–", "-").split())


def resolve_location(value: str | None) -> Location | None:
    if not value:
        return None

    normalized = _normalize(value)
    for location in LOCATIONS:
        candidates = (location.canonical_id, location.navigation_anchor, *location.aliases)
        if normalized in {_normalize(candidate) for candidate in candidates}:
            return location
    return None
