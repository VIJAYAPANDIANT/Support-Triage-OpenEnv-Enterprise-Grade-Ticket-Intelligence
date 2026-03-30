import random

def inject_noise(text: str) -> str:
    """Injects typos or irrelevant chitchat into the text."""
    typos = {"the": "teh", "account": "accnt", "locked": "lcked", "please": "plz", "software": "softwear"}
    words = text.split()
    
    # Randomly inject typos
    for i in range(len(words)):
        if words[i].lower() in typos and random.random() < 0.3:
            words[i] = typos[words[i].lower()]
            
    # Randomly prepend irrelevant chitchat
    chitchat = [
        "Hope you are having a good day! ",
        "Sent from my iPhone. ",
        "I'm really frustrated but anyway... ",
        "Quick question before we start. "
    ]
    if random.random() < 0.2:
        return random.choice(chitchat) + " ".join(words)
        
    return " ".join(words)

def simulate_user_reply(action_type: str, task: dict) -> Optional[str]:
    """Simulates a user response if the agent asks a question or responds."""
    if action_type != "respond":
        return None
        
    replies = task.get("user_replies", [])
    if replies and random.random() < 0.8:
        # For simplicity, return the first available reply if not used yet
        return random.choice(replies)
        
    return None
