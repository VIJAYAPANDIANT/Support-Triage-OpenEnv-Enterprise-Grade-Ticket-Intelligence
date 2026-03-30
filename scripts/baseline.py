import os
import json
import openai
from env.triage_env import SupportTriageEnv
from models.schema import Action

# Setup OpenAI Client (Optional)
openai.api_key = os.getenv("OPENAI_API_KEY")

def run_baseline_v2():
    print("Starting Baseline Inference v2.0 (Realism & Memory)...")
    
    num_tasks = 3  # Default to 3 tasks (Easy, Medium, Hard)
    for i in range(num_tasks):
        print(f"\n--- Running Task {i+1} ---")
        env = SupportTriageEnv(task_idx=i, noise_enabled=True)
        obs = env.reset()
        done = False
        total_reward = 0
        memory = {} # Local memory for the LLM agent
        
        while not done:
            ticket_content = obs.current_ticket.content if obs.current_ticket else "No ticket"
            print(f"Ticket (Noisy): {ticket_content[:100]}...")
            
            if obs.error:
                print(f"SYSTEM ERROR DETECTED: {obs.error}")
            
            # Richer prompt including full history and memory
            history_summary = "\n".join([f"{h.role}: {h.content}" for h in obs.history[-5:]])
            prompt = f"""
            You are a customer support agent. 
            TICKET: {ticket_content}
            RECENT HISTORY:
            {history_summary}
            
            YOUR MEMORY: {obs.memory}
            
            COMMANDS:
            1. classify(priority='low'/'medium'/'high'/'urgent')
            2. route(team='billing'/'technical'/'general'/'sales')
            3. respond(response_text='...')
            4. close()
            
            Output JSON: {{"type": "...", "priority": "...", "team": "...", "response_text": "...", "memory_update": {{"key": "value"}}}}
            """
            
            try:
                if not openai.api_key:
                    # Mock logic for demo
                    last_agent_action = next((h for h in reversed(obs.history) if h.role == "agent"), None)
                    if not last_agent_action:
                        action_data = {"type": "classify", "priority": "high", "memory_update": {"phase": "started"}}
                    elif "classify" in last_agent_action.content and i > 0:
                        action_data = {"type": "route", "team": "billing" if i==1 else "technical"}
                    elif "route" in last_agent_action.content:
                        action_data = {"type": "respond", "response_text": "I am looking into this."}
                    else:
                        action_data = {"type": "close"}
                else:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    action_data = json.loads(response.choices[0].message.content)

                action = Action(**action_data)
                obs, reward, done, info = env.step(action)
                total_reward += reward.value
                print(f"Action: {action.type} | Reward: {reward.value:.2f} | Reason: {reward.reason}")
                
            except Exception as e:
                print(f"Error in step: {e}")
                break
                
        print(f"Task {i+1} Finished. Total Reward: {total_reward:.2f}")

if __name__ == "__main__":
    run_baseline_v2()
