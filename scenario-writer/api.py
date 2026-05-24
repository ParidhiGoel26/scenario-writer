from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scenario_writer import ScenarioWriter
import uvicorn

app = FastAPI(title="AI Scenario Writer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

writer = ScenarioWriter()

class ScenarioRequest(BaseModel):
    icp_type: str
    milestone_code: str
    skill_target: str
    language: str

@app.post("/generate-scenario")
async def generate_scenario(request: ScenarioRequest):
    try:
        input_data = {
            "icp_type": request.icp_type,
            "milestone_code": request.milestone_code,
            "skill_target": request.skill_target,
            "language": request.language
        }
        
        output = writer.generate_scenario(input_data)
        return {"success": True, "data": output}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)