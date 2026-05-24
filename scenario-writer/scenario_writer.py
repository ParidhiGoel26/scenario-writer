import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class ScenarioWriter:
    """REAL AI Scenario Writer using Groq API (Fast, Free, Intelligent)"""
    
    def __init__(self):
        print("🚀 Initializing REAL AI Scenario Writer...")
        
        self.api_key = os.getenv("GROQ_API_KEY")
        
        if not self.api_key:
            print("❌ No GROQ_API_KEY found in .env file!")
            print("⚠️ Please add: GROQ_API_KEY=gsk_your_key_here")
            print("⚠️ Get free key from: https://console.groq.com/keys")
            self.client = None
            return
        
        try:
            self.client = Groq(api_key=self.api_key)
            print("✅ Groq API connected successfully!")
            print("🎯 AI is ready to generate intelligent scenarios")
        except Exception as e:
            print(f"❌ Failed to connect: {e}")
            self.client = None
    
    def generate_scenario(self, input_data):
        icp_type = input_data.get("icp_type", "high_wage")
        skill_target = input_data.get("skill_target", "communication")
        language = input_data.get("language", "en")
        milestone_code = input_data.get("milestone_code", "M03")
        
        print(f"\n🤖 AI Processing: '{skill_target}'")
        
        if not self.client:
            print("⚠️ No API key - cannot generate intelligent scenario")
            return self._error_scenario()
        
        # Build intelligent prompt
        prompt = self._build_prompt(icp_type, skill_target, language, milestone_code)
        
        try:
            # Call REAL AI (Groq)
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",  # Fast, free, intelligent
                messages=[
                    {"role": "system", "content": "You are an expert workplace scenario generator. Create realistic, specific, practical scenarios. Output ONLY valid JSON, no other text."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=2000
            )
            
            ai_response = response.choices[0].message.content
            print(f"✅ AI generated response successfully")
            
            # Extract JSON
            json_match = re.search(r'\{[\s\S]*\}', ai_response)
            if json_match:
                scenario = json.loads(json_match.group())
                return scenario
            else:
                print("⚠️ AI didn't return valid JSON")
                return self._fallback_scenario(icp_type, skill_target, language)
                
        except Exception as e:
            print(f"❌ AI Error: {e}")
            return self._fallback_scenario(icp_type, skill_target, language)
    
    def _build_prompt(self, icp_type, skill_target, language, milestone_code):
        """Build intelligent prompt for AI"""
        
        difficulty_map = {
            "M01": "Beginner - simple scenario",
            "M02": "Developing - moderate challenge",
            "M03": "Intermediate - real pressure",
            "M04": "Proficient - high stakes",
            "M05": "Advanced - very challenging",
            "M06": "Expert - extreme pressure",
            "M07": "Master - career-defining moment"
        }
        difficulty = difficulty_map.get(milestone_code, "Intermediate")
        
        if icp_type == "high_wage":
            user_context = """
            USER: High Wage Professional (Software Engineer, Tech Worker)
            - Works in: Tech office, startup, software company
            - Colleagues: Tech Leads, Product Managers, CTO
            - Typical concerns: Deadlines, code quality, career growth
            """
        else:
            user_context = """
            USER: Low Wage Worker (Customer Support, Delivery Partner)
            - Works in: Call center, delivery hub, retail store
            - Colleagues: Supervisors, Team Leads, Customers
            - Typical concerns: Customer satisfaction, performance, shift management
            """
        
        lang_instruction = "Hindi (Devanagari script)" if language == "hi" else "English"
        
        return f"""Create a realistic workplace scenario for someone to practice this skill: "{skill_target}"

{user_context}

DIFFICULTY: {difficulty}
OUTPUT LANGUAGE: {lang_instruction}

REQUIREMENTS:
1. The scenario MUST be specifically about practicing "{skill_target}"
2. Create real tension - make it feel urgent and important
3. The antagonist line should sound like a real person speaking
4. Each strategy chip must be a different approach
5. The philosophy must explain WHY that strategy works

OUTPUT ONLY VALID JSON with this exact structure:

{{
  "scene": {{
    "setting": "specific workplace location with details",
    "time": "time of day",
    "context": "rich background description of the situation"
  }},
  "characters": [
    {{"name": "Indian name", "role": "job title", "mood": "emotional state"}},
    {{"name": "Indian name", "role": "job title", "mood": "emotional state"}}
  ],
  "antagonist_opening_line": "a tense, realistic dialogue line that creates pressure",
  "strategy_chips": [
    {{"id": "chip1", "label": "first action strategy", "philosophy": "explanation of why this approach works"}},
    {{"id": "chip2", "label": "second different strategy", "philosophy": "different reasoning for this approach"}},
    {{"id": "chip3", "label": "third unique strategy", "philosophy": "third unique reasoning"}}
  ],
  "success_criteria": [
    "measurable outcome 1",
    "measurable outcome 2",
    "measurable outcome 3"
  ],
  "rubric": {{
    "communication": 0-100,
    "composure": 0-100,
    "clarity": 0-100,
    "strategy": 0-100,
    "outcome": 0-100
  }},
  "transfer_targets": [
    "real-world skill related to {skill_target}",
    "another related professional skill"
  ]
}}

Generate a HIGH-QUALITY, REALISTIC scenario for practicing "{skill_target}" now:"""
    
    def _fallback_scenario(self, icp_type, skill_target, language):
        """Fallback if AI fails"""
        skill = skill_target.replace("_", " ").title()
        
        return {
            "scene": {
                "setting": "Workplace office" if icp_type == "high_wage" else "Customer service center",
                "time": "2:30 PM",
                "context": f"You need to demonstrate your {skill} skills in this situation."
            },
            "characters": [
                {"name": "Rajesh", "role": "Manager", "mood": "focused"},
                {"name": "Priya", "role": "Employee", "mood": "prepared"}
            ],
            "antagonist_opening_line": f"Show me how you handle {skill} in this critical situation.",
            "strategy_chips": [
                {"id": "chip1", "label": f"Analyze the {skill} situation", "philosophy": "Understanding needs before acting is crucial."},
                {"id": "chip2", "label": f"Apply proven {skill} methods", "philosophy": "Using established techniques increases success."},
                {"id": "chip3", "label": f"Get feedback and improve", "philosophy": "Continuous improvement leads to mastery."}
            ],
            "success_criteria": [f"Demonstrate {skill}", "Receive positive feedback", "Identify improvements"],
            "rubric": {"communication": 70, "composure": 65, "clarity": 70, "strategy": 68, "outcome": 65},
            "transfer_targets": [skill, "Professional Development"]
        }
    
    def _error_scenario(self):
        """Error scenario when no API key"""
        return {
            "scene": {
                "setting": "Setup Required",
                "time": "Now",
                "context": "No AI API key configured. Please add GROQ_API_KEY to .env file"
            },
            "characters": [
                {"name": "System", "role": "Setup", "mood": "Waiting"},
                {"name": "User", "role": "Administrator", "mood": "Action Needed"}
            ],
            "antagonist_opening_line": "API key missing! Get free key from https://console.groq.com/keys",
            "strategy_chips": [
                {"id": "chip1", "label": "Get Groq API key", "philosophy": "Free and fast AI provider"},
                {"id": "chip2", "label": "Add to .env file", "philosophy": "GROQ_API_KEY=your_key_here"},
                {"id": "chip3", "label": "Restart application", "philosophy": "AI will work after restart"}
            ],
            "success_criteria": ["API key configured", "AI working", "Intelligent scenarios"],
            "rubric": {"communication": 0, "composure": 0, "clarity": 0, "strategy": 0, "outcome": 0},
            "transfer_targets": ["Setup", "Configuration", "AI Integration"]
        }


CachedScenarioWriter = ScenarioWriter
TemplateScenarioWriter = ScenarioWriter