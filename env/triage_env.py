import random
from typing import Any, Dict, List, Tuple, Optional
from models.schema import Observation, Action, Reward, Ticket, Interaction
from tasks.registry import TASKS
from graders.logic import grade_easy, grade_medium, grade_hard
from .utils import inject_noise, simulate_user_reply

class SupportTriageEnv:
    """
    Enhanced OpenEnv for Customer Support Triage v2.0.
    Features: Noisy inputs, Multi-turn conversations, Agent Memory, and Edge Cases.
    """
    def __init__(self, task_idx: int = 0, noise_enabled: bool = True):
        self.task_idx = task_idx % len(TASKS)
        self.noise_enabled = noise_enabled
        self.max_steps = 10  # Increased for multi-turn
        self.reset()

    def reset(self) -> Observation:
        self.current_task = TASKS[self.task_idx].copy()
        
        # Apply noise to initial ticket if enabled
        if self.noise_enabled:
            self.current_task["ticket"].content = inject_noise(self.current_task["ticket"].content)
            
        self.history: List[Interaction] = []
        self.memory: Dict[str, Any] = {}
        self.steps = 0
        self.done = False
        return self._get_obs()

    def state(self) -> Dict[str, Any]:
        return {
            "task_id": self.current_task["id"],
            "steps": self.steps,
            "memory": self.memory,
            "done": self.done
        }

    def _get_obs(self, error: Optional[str] = None) -> Observation:
        return Observation(
            current_ticket=self.current_task["ticket"],
            history=self.history,
            memory=self.memory,
            remaining_tickets=len(TASKS) - self.task_idx - 1,
            error=error
        )

    def step(self, action: Action) -> Tuple[Observation, Reward, bool, Dict[str, Any]]:
        """Executes one environment step."""
        if self.done:
            return self._get_obs(), Reward(value=0, reason="Done"), True, {}

        self.steps += 1
        
        # 1. Update Agent Memory
        if action.memory_update:
            self.memory.update(action.memory_update)

        # 2. Record Agent Action
        self.history.append(Interaction(
            role="agent", 
            action_type=action.type, 
            content=str(action.dict(exclude_none=True))
        ))

        # 3. Simulate Edge Case (System Error)
        error = None
        if random.random() < 0.05:  # 5% chance of system failure
            error = "CRITICAL: Database connection timeout. Action may not have persisted."
            return self._get_obs(error), Reward(value=-1, reason="System failure"), False, {}

        # 4. Reward Shaping & Logic
        reward_val, reason = self._calculate_reward(action)

        # 5. Simulate Multi-turn User Reply
        user_reply = simulate_user_reply(action.type, self.current_task)
        if user_reply:
            self.history.append(Interaction(
                role="user",
                action_type="reply",
                content=user_reply
            ))
            reward_val += 0.5  # Bonus for engaging the user
            reason += " | User replied to agent response."

        # 6. Termination Logic
        if action.type == "close" or self.steps >= self.max_steps:
            self.done = True
            grade = self._grade_task()
            multiplier = 10 if action.type == "close" else 5
            reward_val += grade * multiplier
            reason += f" | Final Grade: {grade}"

        obs = self._get_obs(error)
        reward = Reward(value=reward_val, reason=reason, is_terminal=self.done)
        
        return obs, reward, self.done, {}

    def _calculate_reward(self, action: Action) -> Tuple[float, str]:
        # Efficiency and validity rewards
        reward = 0.1
        reason = "Valid step"
        
        # Penalize redundant actions in history
        agent_actions = [h for h in self.history if h.role == "agent"]
        if len(agent_actions) > 1 and agent_actions[-1].content == agent_actions[-2].content:
            reward -= 1.0
            reason = "Redundant action penalty"
            
        return reward, reason

    def _grade_task(self) -> float:
        # Extract plain string history for legacy graders or refactor them
        history_strs = [h.content for h in self.history if h.role == "agent"]
        if self.task_idx == 0: return grade_easy(history_strs)
        if self.task_idx == 1: return grade_medium(history_strs)
        return grade_hard(history_strs)
