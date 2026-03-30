from models.schema import Ticket

# Enhanced Tasks with multi-turn triggers
TASK_EASY = {
    "id": "easy_priority",
    "description": "Classify priority.",
    "ticket": Ticket(
        ticket_id="T-001",
        content="Locked out of my account!",
        sender="bob@example.com",
        timestamp="2026-03-30T10:00:00Z"
    ),
    "expected_priority": "high",
    "user_replies": ["Thank you for looking into this so quickly!"]
}

TASK_MEDIUM = {
    "id": "medium_route",
    "description": "Classify and route.",
    "ticket": Ticket(
        ticket_id="T-002",
        content="Overcharged by $50 on invoice INV-99.",
        sender="alice@example.com",
        timestamp="2026-03-30T10:05:00Z"
    ),
    "expected_priority": "medium",
    "expected_team": "billing",
    "user_replies": ["Do you need my account number?", "When can I expect a refund?"]
}

TASK_HARD = {
    "id": "hard_resolve",
    "description": "Full resolution with edge cases.",
    "ticket": Ticket(
        ticket_id="T-003",
        content="Software crashes on PDF export. Urgent!",
        sender="charlie@example.com",
        timestamp="2026-03-30T10:10:00Z"
    ),
    "expected_priority": "urgent",
    "expected_team": "technical",
    "user_replies": ["I've attached the crash logs to the email.", "Is there a workaround?"]
}

TASKS = [TASK_EASY, TASK_MEDIUM, TASK_HARD]
