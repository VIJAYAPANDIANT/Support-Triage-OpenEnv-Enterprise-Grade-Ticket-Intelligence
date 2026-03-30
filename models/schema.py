from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field

class Ticket(BaseModel):
    ticket_id: str = Field(..., description="Unique identifier for the ticket")
    content: str = Field(..., description="Content of the customer support ticket")
    sender: str = Field(..., description="Email or ID of the customer")
    timestamp: str = Field(..., description="ISO 8601 timestamp")

class Interaction(BaseModel):
    role: Literal["agent", "user", "system"] = Field(..., description="Who performed the action")
    action_type: str = Field(..., description="Type of action taken")
    content: str = Field(..., description="Text content or description of the action")

class Observation(BaseModel):
    current_ticket: Optional[Ticket] = Field(None, description="The ticket currently being triaged")
    history: List[Interaction] = Field(default_factory=list, description="Rich history of interactions")
    memory: Dict[str, Any] = Field(default_factory=dict, description="Agent-managed persistent memory")
    remaining_tickets: int = Field(0, description="Number of tickets pending in the queue")
    error: Optional[str] = Field(None, description="System error message (e.g. 'DB Timeout')")

class Action(BaseModel):
    type: Literal["classify", "route", "respond", "close"] = Field(..., description="Type of action to perform")
    priority: Optional[Literal["low", "medium", "high", "urgent"]] = Field(None, description="Priority level")
    team: Optional[Literal["billing", "technical", "general", "sales"]] = Field(None, description="Team to route to")
    response_text: Optional[str] = Field(None, description="Text response to the customer")
    memory_update: Optional[Dict[str, Any]] = Field(None, description="Updates to the agent's internal memory")

class Reward(BaseModel):
    value: float = Field(..., description="Numerical reward value")
    reason: str = Field(..., description="Explanation for the reward")
    is_terminal: bool = Field(False, description="Whether this marks the end of a task")
