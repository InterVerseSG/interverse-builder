from typing import Literal

from pydantic import BaseModel, Field


Action = Literal[
    "answer",
    "navigate",
    "create_object",
    "move_object",
    "delete_object",
    "open_panel",
]


class BuildCommand(BaseModel):
    action: Action
    response: str = ""
    target: str | None = None
    object_type: str | None = None
    quantity: int | None = Field(default=None, ge=1)
    location: str | None = None
    requires_confirmation: bool = False


class UnrealInstruction(BaseModel):
    accepted: bool
    action: Action
    message: str
    target: str | None = None
    blueprint_class: str | None = None
    quantity: int | None = None
    location: str | None = None
    requires_confirmation: bool = False
