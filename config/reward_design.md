# Supporting Documentation: Reward Function Design

The reward system in `SupportTriageEnv` is designed to provide dense feedback to the agent, encouraging efficiency and accuracy while penalizing errors.

## Reward Logic Breakdown

### 1. Per-Step Feedback
- **Base Step Reward**: `+0.1` for every valid action taken. This encourages the agent to interact with the environment.
- **Efficiency Penalty**: Since there is a step limit (5), the cumulative step reward is small compared to the goal reward, incentivizing the agent to reach `close` quickly.

### 2. Penalties
- **Repeated Actions**: `-0.5` penalty if the agent repeats the exact same action (e.g., classifying as "high" twice). This prevents infinite loops and redundant computation.
- **Step Limit Pressure**: While not a direct penalty in every step, the reward for finishing early is higher than finishing late (e.g., timed out tasks get `grade * 5` instead of `grade * 10`).

### 3. Goal-Oriented Rewards (Deterministic)
The final reward is assigned when the `close` action is called or the step limit is reached, based on the **Task Grader**:
- **Binary Success**: `1.0` if all criteria are met.
- **Partial Credit**:
    - **Easy Task**: `0.2` for any classification, `1.0` for correct priority.
    - **Medium Task**: `0.5` for correct priority, `0.5` for correct team routing.
    - **Hard Task**: `0.3` for correct priority, `0.3` for correct team routing, `0.4` for valid response keywords.

### 4. Reward Scaling
- Successful completion via `close`: `10.0 * grade`.
- Completion via timeout: `5.0 * grade`.

This structure Ensures that even agents that fail to complete the task perfectly still receive feedback on what they got right.
