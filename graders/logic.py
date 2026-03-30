from typing import List

def grade_easy(history: List[str]) -> float:
    score = 0.0
    for content in history:
        if "'type': 'classify'" in content and "'priority': 'high'" in content:
            score = 1.0
        elif "'type': 'classify'" in content:
            score = 0.2
    return score

def grade_medium(history: List[str]) -> float:
    has_priority = False
    has_team = False
    for content in history:
        if "'type': 'classify'" in content and "'priority': 'medium'" in content:
            has_priority = True
        if "'type': 'route'" in content and "'team': 'billing'" in content:
            has_team = True
    
    score = 0.0
    if has_priority: score += 0.5
    if has_team: score += 0.5
    return score

def grade_hard(history: List[str]) -> float:
    has_priority = False
    has_team = False
    has_good_response = False
    
    for content in history:
        if "'type': 'classify'" in content and "'priority': 'urgent'" in content:
            has_priority = True
        if "'type': 'route'" in content and "'team': 'technical'" in content:
            has_team = True
        if "'type': 'respond'" in content:
            low_content = content.lower()
            if any(kw in low_content for kw in ["sorry", "investigating", "attached"]):
                has_good_response = True
                
    score = 0.0
    if has_priority: score += 0.3
    if has_team: score += 0.3
    if has_good_response: score += 0.4
    return score
