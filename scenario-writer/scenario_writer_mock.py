import google.generativeai as genai
import json
import re
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    print("✅ Gemini API configured successfully")
else:
    print("⚠️ No Gemini API key found. Please add GEMINI_API_KEY to .env file")

class ScenarioWriter:
    """TRUE INTELLIGENT Scenario Writer - Uses Gemini API for dynamic generation"""
    
    def __init__(self):
        print("✅ Intelligent Scenario Writer initialized with Gemini API")
        self.model = None
        
        if GEMINI_API_KEY:
            # Configure Gemini model
            self.generation_config = {
                "temperature": 0.8,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
            }
            
            self.model = genai.GenerativeModel(
                'gemini-1.5-pro',
                generation_config=self.generation_config
            )
            print("✅ Gemini model ready")
        else:
            print("⚠️ Running in fallback mode (no Gemini API)")
    
    def generate_scenario(self, input_data):
        icp_type = input_data.get("icp_type", "high_wage")
        skill_target = input_data.get("skill_target", "communication")
        language = input_data.get("language", "en")
        milestone_code = input_data.get("milestone_code", "M03")
        
        print(f"🎯 Generating INTELLIGENT scenario for: {skill_target}")
        
        # Use Gemini API if available
        if self.model and GEMINI_API_KEY:
            return self._generate_with_gemini(icp_type, skill_target, language, milestone_code)
        else:
            # Fallback to mock if no API key
            return self._generate_fallback(icp_type, skill_target, language, milestone_code)
    
    def _generate_with_gemini(self, icp_type, skill_target, language, milestone_code):
        """Generate scenario using actual Gemini API"""
        
        # Build the prompt
        prompt = self._build_intelligent_prompt(icp_type, skill_target, language, milestone_code)
        
        try:
            # Call Gemini API
            response = self.model.generate_content(prompt)
            
            # Extract JSON from response
            response_text = response.text
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            
            if json_match:
                scenario = json.loads(json_match.group())
                print("✅ Gemini generated intelligent scenario")
                return scenario
            else:
                print("⚠️ Gemini returned invalid JSON, using fallback")
                return self._generate_fallback(icp_type, skill_target, language, milestone_code)
                
        except Exception as e:
            print(f"❌ Gemini API error: {e}")
            return self._generate_fallback(icp_type, skill_target, language, milestone_code)
    
    def _build_intelligent_prompt(self, icp_type, skill_target, language, milestone_code):
        """Build intelligent prompt for Gemini"""
        
        # Difficulty level
        difficulty_map = {
            "M01": "Beginner (very easy, basic scenario)",
            "M02": "Developing (slightly challenging)",
            "M03": "Intermediate (moderate difficulty)",
            "M04": "Proficient (quite challenging)",
            "M05": "Advanced (very challenging)",
            "M06": "Expert (extremely challenging)",
            "M07": "Master (expert level, high pressure)"
        }
        difficulty = difficulty_map.get(milestone_code, "Intermediate (moderate difficulty)")
        
        # Language instruction
        if language == "hi":
            lang_instruction = "OUTPUT IN HINDI (Devanagari script). All text fields must be in Hindi."
        else:
            lang_instruction = "OUTPUT IN ENGLISH"
        
        # ICP-specific instructions
        if icp_type == "high_wage":
            icp_context = """
            USER TYPE: High Wage (Tech Professional)
            - Setting: Tech office, startup, software company, IT department
            - Characters: Engineers, Tech Leads, Product Managers, CTO, HR
            - Tension: Deadlines, code quality, technical debt, client pressure, career growth
            - Language style: Professional, technical (but not overly jargon-heavy)
            - Salary context: ₹15-50 LPA range, stock options, bonuses
            """
        else:
            icp_context = """
            USER TYPE: Low Wage (Service/Gig Worker)
            - Setting: Customer support center, delivery hub, warehouse, retail store, small office
            - Characters: Supervisors, team leads, customers, delivery partners, support agents
            - Tension: Customer complaints, performance pressure, shift management, time constraints
            - Language style: Simple, accessible, practical, encouraging
            - Salary context: ₹15,000-40,000 per month, overtime pay, performance incentives
            """
        
        prompt = f"""You are an expert workplace scenario writer. Create a realistic, detailed, and PRACTICAL scenario based on the following:

{icp_context}

SKILL TO PRACTICE: "{skill_target}"
DIFFICULTY LEVEL: {difficulty}
OUTPUT LANGUAGE: {lang_instruction}

CRITICAL REQUIREMENTS:
1. The scenario MUST be SPECIFICALLY about practicing "{skill_target}"
2. The antagonist opening line must create REAL tension (not generic like "I'm unhappy")
3. The 3 strategy chips must be TRULY DIFFERENT approaches
4. Each strategy chip's philosophy must explain WHY it works
5. Rubric scores must be REALISTIC (not all 50s, vary based on difficulty)
6. The scenario should feel REAL and RELATABLE to the user type

OUTPUT ONLY VALID JSON (no markdown, no extra text). Use this exact schema:

{{
  "scene": {{
    "setting": "specific workplace location",
    "time": "time of day",
    "context": "rich background description of what led to this moment"
  }},
  "characters": [
    {{"name": "Indian name", "role": "job title", "mood": "emotional state"}},
    {{"name": "Indian name", "role": "job title", "mood": "emotional state"}}
  ],
  "antagonist_opening_line": "specific, tense, realistic dialogue that creates pressure",
  "strategy_chips": [
    {{"id": "chip1", "label": "action label", "philosophy": "why this strategy works psychologically"}},
    {{"id": "chip2", "label": "different action label", "philosophy": "different reasoning"}},
    {{"id": "chip3", "label": "third action label", "philosophy": "third reasoning"}}
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
    "real-world skill 1",
    "real-world skill 2",
    "real-world skill 3"
  ]
}}

Generate a HIGH-QUALITY, REALISTIC scenario now. Make it specific, practical, and directly relevant to practicing "{skill_target}" for a {icp_type} user at {difficulty} level.
"""
        
        return prompt
    
    def _generate_fallback(self, icp_type, skill_target, language, milestone_code):
        """Fallback intelligent generation without API"""
        
        skill_clean = skill_target.replace("_", " ").title()
        
        if icp_type == "high_wage":
            # High wage fallback
            if "negotiation" in skill_target.lower():
                return {
                    "scene": {
                        "setting": "HR office, tech company headquarters",
                        "time": "2:30 PM",
                        "context": f"You've been at the company for 2 years and have consistently exceeded expectations. You requested a meeting with HR to discuss your compensation."
                    },
                    "characters": [
                        {"name": "Neeta Sharma", "role": "HR Business Partner", "mood": "professional but guarded"},
                        {"name": "Vikram Singh", "role": "Senior Software Engineer", "mood": "confident and prepared"}
                    ],
                    "antagonist_opening_line": f"Vikram, I've reviewed your request. The budget for this quarter is already allocated. You're asking for a 30% raise when the standard is 10%. Tell me why this is justified.",
                    "strategy_chips": [
                        {"id": "chip1", "label": f"Present market data and your achievements", "philosophy": "Data-driven arguments are harder to dismiss. Show industry salary benchmarks and quantify your specific contributions to the company's revenue or cost savings."},
                        {"id": "chip2", "label": f"Focus on future value, not past performance", "philosophy": "HR cares about what you'll do next. Present a clear plan for how you'll deliver more value in the coming year with the raise."},
                        {"id": "chip3", "label": f"Negotiate total package, not just salary", "philosophy": "If salary is fixed, shift to bonus, stock options, extra vacation, or title change. Sometimes non-salary benefits are easier to get approval for."}
                    ],
                    "success_criteria": [
                        f"Secure at least a 15% salary increase",
                        "Get a clear roadmap for promotion in next 6 months",
                        "Establish yourself as someone who advocates for their worth professionally"
                    ],
                    "rubric": {"communication": 85, "composure": 88, "clarity": 82, "strategy": 90, "outcome": 78},
                    "transfer_targets": ["Salary Negotiation", "Self-Advocacy", "Career Growth Strategy"]
                }
            elif "leadership" in skill_target.lower() or "team" in skill_target.lower():
                return {
                    "scene": {
                        "setting": "Team meeting room, post-mortem meeting",
                        "time": "9:30 AM",
                        "context": f"Your team just missed a critical deadline. The client is angry. Three team members look defeated, two are blaming each other, and one has been silent for an hour."
                    },
                    "characters": [
                        {"name": "Rajesh Mehra", "role": "Engineering Manager", "mood": "disappointed but composed"},
                        {"name": "Priya Iyer", "role": "Senior Developer", "mood": "frustrated and defensive"}
                    ],
                    "antagonist_opening_line": f"The project is 2 weeks behind. The client is threatening to cancel. Your team is falling apart. How are you going to lead them out of this crisis?",
                    "strategy_chips": [
                        {"id": "chip1", "label": f"Own the failure publicly", "philosophy": "Great leaders take responsibility. Say 'The failure is mine, the success is ours.' This builds trust and removes defensiveness."},
                        {"id": "chip2", "label": f"Acknowledge emotions before problem-solving", "philosophy": "People can't think clearly when they're emotional. Acknowledge frustration, fear, and blame before moving to solutions."},
                        {"id": "chip3", "label": f"Create small, achievable next steps", "philosophy": "Rebuild confidence through small wins. Break down recovery into 2-hour tasks that people can succeed at immediately."}
                    ],
                    "success_criteria": [
                        "Team members stop blaming and start collaborating",
                        "Clear recovery plan with owners and deadlines",
                        "Client agrees to one more chance"
                    ],
                    "rubric": {"communication": 88, "composure": 92, "clarity": 85, "strategy": 86, "outcome": 75},
                    "transfer_targets": ["Crisis Leadership", "Team Motivation", "Conflict Resolution"]
                }
            else:
                return {
                    "scene": {
                        "setting": "Modern tech office, open workspace",
                        "time": "11:00 AM",
                        "context": f"You're in the middle of your workday when a challenging {skill_clean} situation arises."
                    },
                    "characters": [
                        {"name": "Arjun Nair", "role": "Tech Lead", "mood": "expectant"},
                        {"name": "Meera Kulkarni", "role": "Product Manager", "mood": "observant"}
                    ],
                    "antagonist_opening_line": f"We need to assess your {skill_clean} skills. Here's a real situation - how would you handle it?",
                    "strategy_chips": [
                        {"id": "chip1", "label": f"Analyze the {skill_clean} situation first", "philosophy": "Understanding the problem deeply before acting prevents mistakes."},
                        {"id": "chip2", "label": f"Apply best practices for {skill_clean}", "philosophy": "Use proven frameworks rather than reinventing solutions."},
                        {"id": "chip3", "label": f"Get feedback and iterate", "philosophy": "Great results come from continuous improvement based on input."}
                    ],
                    "success_criteria": [
                        f"Successfully demonstrate {skill_clean}",
                        "Receive positive acknowledgment",
                        "Learn something applicable to future situations"
                    ],
                    "rubric": {"communication": 78, "composure": 75, "clarity": 80, "strategy": 76, "outcome": 72},
                    "transfer_targets": [skill_clean, "Professional Development", "Workplace Success"]
                }
        else:
            # Low wage fallback
            if "customer" in skill_target.lower() or "complaint" in skill_target.lower():
                return {
                    "scene": {
                        "setting": "Busy customer support center, Noida",
                        "time": "6:45 PM",
                        "context": f"A customer has been on hold for 15 minutes. They've called 4 times in the last week about the same issue. Your supervisor is listening to this call."
                    },
                    "characters": [
                        {"name": "Mr. Agarwal", "role": "Customer", "mood": "extremely angry and frustrated"},
                        {"name": "Sunita Verma", "role": "Senior Support Agent", "mood": "nervous but trained"}
                    ],
                    "antagonist_opening_line": f"This is the 4th time I'm calling! My order was supposed to arrive 10 days ago! No one has helped me! Fix it NOW or I'm going to consumer court and writing bad reviews everywhere!",
                    "strategy_chips": [
                        {"id": "chip1", "label": f"Apologize sincerely without excuses", "philosophy": "A genuine 'I'm truly sorry for your experience' reduces anger by 50%. Don't say 'but' - just apologize."},
                        {"id": "chip2", "label": f"Listen and acknowledge their frustration", "philosophy": "Let them vent completely. Say 'You're right to be upset, I understand.' Validation calms angry customers faster than solutions."},
                        {"id": "chip3", "label": f"Offer immediate, specific solution", "philosophy": "Don't say 'I'll look into it.' Say 'I will refund ₹500 now, and your order will arrive by 6 PM tomorrow.' Specifics build trust."}
                    ],
                    "success_criteria": [
                        "Customer's tone changes from angry to calm",
                        "Customer accepts the proposed solution",
                        "Customer does not escalate to supervisor"
                    ],
                    "rubric": {"communication": 82, "composure": 70, "clarity": 78, "strategy": 80, "outcome": 75},
                    "transfer_targets": ["Customer Service", "Complaint Resolution", "De-escalation Skills"]
                }
            else:
                return {
                    "scene": {
                        "setting": "Service center work area",
                        "time": "2:00 PM",
                        "context": f"A situation requiring your {skill_clean} skills has just come up."
                    },
                    "characters": [
                        {"name": "Ramesh Kumar", "role": "Supervisor", "mood": "observant"},
                        {"name": "Priya Sharma", "role": "Team Member", "mood": "ready"}
                    ],
                    "antagonist_opening_line": f"Show me your {skill_clean} skills. Here's a real situation - how would you handle it?",
                    "strategy_chips": [
                        {"id": "chip1", "label": f"Listen carefully first", "philosophy": "Understanding the real need before acting is crucial."},
                        {"id": "chip2", "label": f"Respond with respect and patience", "philosophy": "How you say things matters as much as what you say."},
                        {"id": "chip3", "label": f"Focus on solving the problem", "philosophy": "Don't dwell on what went wrong, focus on making it right."}
                    ],
                    "success_criteria": [
                        f"Demonstrate {skill_clean} effectively",
                        "Customer or supervisor satisfied with response",
                        "Learn from the experience"
                    ],
                    "rubric": {"communication": 75, "composure": 72, "clarity": 75, "strategy": 70, "outcome": 68},
                    "transfer_targets": [skill_clean, "Job Success", "Customer Satisfaction"]
                }


CachedScenarioWriter = ScenarioWriter
TemplateScenarioWriter = ScenarioWriter