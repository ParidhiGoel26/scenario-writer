"""
AI Prompts for Scenario Writer - Real-Life Version
Creates REAL workplace scenarios for ANY skill target
"""

SYSTEM_PROMPT = """You are an expert at creating REAL workplace scenarios that people actually face.

CRITICAL RULES:
- Create scenarios that feel like they happened to a real person yesterday
- Use REAL Indian cities (Bangalore, Mumbai, Delhi, Pune, Hyderabad, Chennai, Noida, Gurgaon)
- Use REAL job titles (Software Engineer, Delivery Partner, Customer Support Agent, Team Lead)
- Create REAL tension (specific complaints, deadlines, money concerns, career pressure)
- Give ACTIONABLE strategies (things people can actually DO)
- For ANY skill target, create a UNIQUE, RELEVANT scenario

OUTPUT: Valid JSON only. No explanations, no markdown."""

def build_user_prompt(icp_type, milestone_code, skill_target, language):
    """
    Creates REAL-LIFE scenarios for ANY skill target
    """
    
    # Difficulty mapping
    difficulty_config = {
        "M01": {"level": "Beginner", "scores": [70, 85], "stakes": "low"},
        "M02": {"level": "Developing", "scores": [65, 80], "stakes": "low-moderate"},
        "M03": {"level": "Intermediate", "scores": [55, 75], "stakes": "moderate"},
        "M04": {"level": "Proficient", "scores": [45, 65], "stakes": "moderate-high"},
        "M05": {"level": "Advanced", "scores": [35, 55], "stakes": "high"},
        "M06": {"level": "Expert", "scores": [25, 45], "stakes": "very high"},
        "M07": {"level": "Master", "scores": [15, 35], "stakes": "critical"}
    }
    diff = difficulty_config.get(milestone_code, difficulty_config["M03"])
    
    # Set roles and workplace based on ICP type
    if icp_type == "high_wage":
        roles = ["Engineering Manager", "Tech Lead", "Product Manager", "HR Manager"]
        workplace = "tech office, startup, or software company"
        cities = ["Bangalore", "Hyderabad", "Pune", "Gurgaon"]
    else:
        roles = ["Team Supervisor", "Senior Agent", "Hub Manager", "Customer Lead"]
        workplace = "customer support center, delivery hub, or retail store"
        cities = ["Delhi", "Mumbai", "Noida", "Chennai"]
    
    # Language instruction
    if language == "hi":
        lang_instruction = "OUTPUT IN HINDI (Devanagari script). Use simple, everyday Hindi."
    else:
        lang_instruction = "OUTPUT IN ENGLISH. Use simple, conversational English."
    
    # Get the actual skill the user wants to practice
    user_skill = skill_target.strip()
    
    # Build the prompt - this will work for ANY skill
    prompt = f"""Create a REAL-LIFE workplace scenario for someone practicing this skill: "{user_skill}"

USER TYPE: {icp_type} worker
WORKPLACE: {workplace}
LOCATION: {cities[0]} or {cities[1]}
DIFFICULTY: {diff['level']} - {diff['stakes']} stakes
OUTPUT LANGUAGE: {lang_instruction}

REQUIREMENTS FOR A REAL SCENARIO:
1. Use a REAL Indian city and specific location
2. Create a situation that ACTUALLY happens in workplaces
3. Make the antagonist line something a REAL person would say
4. Give strategies that people can ACTUALLY use
5. Make the success criteria MEASURABLE (not vague)

OUTPUT ONLY THIS JSON:

{{
  "scene": {{
    "setting": "specific location in {cities[0]} or {cities[1]} with exact place",
    "time": "exact time of day",
    "context": "2-3 sentences explaining what happened before this moment"
  }},
  "characters": [
    {{"name": "Indian name", "role": "{roles[0]}", "mood": "specific emotion"}},
    {{"name": "Indian name", "role": "{roles[1]}", "mood": "specific emotion"}}
  ],
  "antagonist_opening_line": "a real-sounding tense dialogue related to {user_skill}",
  "strategy_chips": [
    {{"id": "chip1", "label": "actionable strategy 1 for {user_skill}", "philosophy": "why this works in real life"}},
    {{"id": "chip2", "label": "actionable strategy 2 for {user_skill}", "philosophy": "different real-life reasoning"}},
    {{"id": "chip3", "label": "actionable strategy 3 for {user_skill}", "philosophy": "third practical approach"}}
  ],
  "success_criteria": [
    "specific measurable outcome 1",
    "specific measurable outcome 2",
    "specific measurable outcome 3"
  ],
  "rubric": {{
    "communication": {diff['scores'][0]},
    "composure": {diff['scores'][0] - 5},
    "clarity": {diff['scores'][0]},
    "strategy": {diff['scores'][0] - 10},
    "outcome": {diff['scores'][0] - 15}
  }},
  "transfer_targets": [
    "{user_skill}",
    "real workplace skill"
  ]
}}

Generate a REAL scenario for practicing "{user_skill}" now:"""
    
    return prompt


def get_fallback_scenario(icp_type, skill_target, language):
    """Fallback that creates REAL scenarios for ANY skill"""
    
    skill = skill_target.replace("_", " ").title()
    seed = abs(hash(skill_target)) % 10
    
    # REAL settings based on ICP
    if icp_type == "high_wage":
        cities = ["Bangalore", "Hyderabad", "Pune", "Gurgaon"]
        offices = ["WeWork", "RMZ Ecospace", "Embassy Tech Village", "DLF Cyber City"]
        
        settings = [
            f"{offices[seed % len(offices)]}, {cities[seed % len(cities)]} - discussing {skill}",
            f"Conference room, {cities[seed % len(cities)]} tech park - {skill} review",
            f"HR cabin, {cities[seed % len(cities)]} - {skill} discussion"
        ]
        
        characters = [
            {"name": "Rajesh Kumar", "role": "Engineering Manager", "mood": "focused but fair"},
            {"name": "Priya Sharma", "role": "Senior Developer", "mood": "prepared and confident"}
        ]
        
        antagonist = f"We need to discuss your {skill} approach on the project. Walk me through your plan."
        
        strategies = [
            f"First, understand what {skill} really means in this context",
            f"Then, create a step-by-step {skill} execution plan",
            f"Finally, execute and adjust based on real-time feedback"
        ]
        
        philosophies = [
            f"Understanding requirements before acting prevents costly mistakes.",
            f"A clear plan ensures everyone is aligned on expectations and outcomes.",
            f"Decisive action builds credibility. You can always adjust based on results."
        ]
        
    else:
        cities = ["Delhi", "Mumbai", "Noida", "Chennai"]
        offices = ["Customer Support Center", "Delivery Hub", "Service Center"]
        
        settings = [
            f"{offices[seed % len(offices)]}, {cities[seed % len(cities)]} - {skill} situation",
            f"Team room, {cities[seed % len(cities)]} - handling {skill}",
            f"Manager's cabin, {cities[seed % len(cities)]} - {skill} discussion"
        ]
        
        characters = [
            {"name": "Sunita Verma", "role": "Team Supervisor", "mood": "supportive but firm"},
            {"name": "Arjun Yadav", "role": "Senior Agent", "mood": "ready and capable"}
        ]
        
        antagonist = f"This customer situation requires your {skill} expertise. How will you handle it?"
        
        strategies = [
            f"Listen carefully to understand the real {skill} need",
            f"Respond with empathy and a clear action plan",
            f"Follow up to ensure the {skill} issue is fully resolved"
        ]
        
        philosophies = [
            f"Understanding the real problem before acting is half the solution.",
            f"People need to feel heard before they can accept solutions.",
            f"Following up builds trust and ensures long-term satisfaction."
        ]
    
    scenario = {
        "scene": {
            "setting": settings[seed % len(settings)],
            "time": ["9:30 AM", "11:00 AM", "2:30 PM", "4:00 PM"][seed % 4],
            "context": f"A real situation has come up that requires your {skill} skills. Your response will determine the outcome."
        },
        "characters": characters,
        "antagonist_opening_line": antagonist,
        "strategy_chips": [
            {"id": "chip1", "label": strategies[0], "philosophy": philosophies[0]},
            {"id": "chip2", "label": strategies[1], "philosophy": philosophies[1]},
            {"id": "chip3", "label": strategies[2], "philosophy": philosophies[2]}
        ],
        "success_criteria": [
            f"Successfully demonstrate {skill} in this real situation",
            "Receive positive acknowledgment from the other person",
            "Learn something applicable to future situations"
        ],
        "rubric": {"communication": 70, "composure": 65, "clarity": 70, "strategy": 68, "outcome": 65},
        "transfer_targets": [skill, "Real Workplace Success"]
    }
    
    if language == "hi":
        scenario = _to_hindi(scenario)
    
    return scenario


def _to_hindi(scenario):
    """Convert scenario to Hindi"""
    return {
        "scene": {
            "setting": scenario["scene"]["setting"] + " (हिंदी)",
            "time": scenario["scene"]["time"],
            "context": scenario["scene"]["context"] + " यह एक वास्तविक कार्यस्थल स्थिति है।"
        },
        "characters": [
            {"name": c["name"], "role": c["role"] + " (हिंदी)", "mood": c["mood"]}
            for c in scenario["characters"]
        ],
        "antagonist_opening_line": scenario["antagonist_opening_line"] + " (हिंदी)",
        "strategy_chips": [
            {"id": chip["id"], "label": chip["label"] + " (हिंदी)", "philosophy": chip["philosophy"] + " (हिंदी)"}
            for chip in scenario["strategy_chips"]
        ],
        "success_criteria": [c + " (हिंदी)" for c in scenario["success_criteria"]],
        "rubric": scenario["rubric"],
        "transfer_targets": [t + " (हिंदी)" for t in scenario["transfer_targets"]]
    }


def build_test_prompt():
    """Simple test prompt"""
    return "Generate: {\"status\": \"ok\", \"message\": \"API ready\"}"


def build_user_prompt_old(icp_type, episode_title, milestone_code, skill_target, language):
    return build_user_prompt(icp_type, milestone_code, skill_target, language)