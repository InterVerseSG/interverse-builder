from dataclasses import dataclass


@dataclass(frozen=True)
class CatalogItem:
    blueprint_class: str
    max_quantity: int
    destructive: bool = False


CATALOG: dict[str, CatalogItem] = {
    "wall": CatalogItem("BP_Wall", 50),
    "floor": CatalogItem("BP_Floor", 20),
    "door": CatalogItem("BP_DoorInteractive", 20),
    "window": CatalogItem("BP_Window", 40),
    "chair": CatalogItem("BP_FurnitureChair", 100),
    "desk": CatalogItem("BP_FurnitureDesk", 50),
    "screen": CatalogItem("BP_InteractiveScreen", 10),
    "sign": CatalogItem("BP_InformationSign", 25),
    "tree": CatalogItem("BP_Tree", 100),
    "light": CatalogItem("BP_QuestLight", 50),
    "navigation_point": CatalogItem("BP_NavigationPoint", 50),
}

ALLOWED_ACTIONS = {
    "answer",
    "navigate",
    "create_object",
    "move_object",
    "delete_object",
    "open_panel",
}
