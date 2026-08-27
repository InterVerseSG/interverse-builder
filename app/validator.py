from app.catalog import CATALOG
from app.locations import resolve_location
from app.schemas import BuildCommand, UnrealInstruction


def validate_command(command: BuildCommand) -> UnrealInstruction:
    if command.action == "navigate":
        destination = resolve_location(command.target)
        if destination is None:
            return UnrealInstruction(
                accepted=False,
                action=command.action,
                message=f"Unknown or unregistered navigation target: {command.target}",
                target=command.target,
                location=command.location,
            )

        return UnrealInstruction(
            accepted=True,
            action=command.action,
            message=command.response or "Navigation command accepted.",
            target=destination.canonical_id,
            navigation_anchor=destination.navigation_anchor,
            location=command.location,
            requires_confirmation=False,
        )

    if command.action in {"answer", "open_panel"}:
        return UnrealInstruction(
            accepted=True,
            action=command.action,
            message=command.response or "Command accepted.",
            target=command.target,
            location=command.location,
            requires_confirmation=command.requires_confirmation,
        )

    if not command.object_type:
        return UnrealInstruction(
            accepted=False,
            action=command.action,
            message="object_type is required for scene object actions.",
            target=command.target,
            location=command.location,
        )

    item = CATALOG.get(command.object_type)
    if item is None:
        return UnrealInstruction(
            accepted=False,
            action=command.action,
            message=f"Unsupported object type: {command.object_type}",
            target=command.target,
            location=command.location,
        )

    quantity = command.quantity or 1
    if quantity > item.max_quantity:
        return UnrealInstruction(
            accepted=False,
            action=command.action,
            message=(
                f"Requested quantity {quantity} exceeds the safe limit "
                f"of {item.max_quantity} for {command.object_type}."
            ),
            target=command.target,
            blueprint_class=item.blueprint_class,
            quantity=quantity,
            location=command.location,
        )

    requires_confirmation = command.requires_confirmation
    if command.action == "delete_object":
        requires_confirmation = True

    return UnrealInstruction(
        accepted=True,
        action=command.action,
        message=command.response or "Command validated for Unreal Engine.",
        target=command.target,
        blueprint_class=item.blueprint_class,
        quantity=quantity,
        location=command.location,
        requires_confirmation=requires_confirmation,
    )
