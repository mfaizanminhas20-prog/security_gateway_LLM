from fastapi import FastAPI, HTTPException
from gateway_logic import process_security_pipeline
import uvicorn

app = FastAPI(title="Secure LLM Gateway")

@app.post("/analyze")
async def analyze_input(payload: dict):
    user_text = payload.get("text", "")
    if not user_text:
        raise HTTPException(status_code=400, detail="Empty text")
    return process_security_pipeline(user_text)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)