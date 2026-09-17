from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}


class AnalyzeRequest(BaseModel):
    text: str


@app.get("/api/profile")
def get_profile():
    return profile


@app.post("/api/analyze")
def analyze(req: AnalyzeRequest):
    return JSONResponse(
        content={
            "text": req.text,
            "score": 0.5,
            "label": "偏平静",
            "pinyin": "（模块 6 再说）",
        },
        media_type="application/json; charset=utf-8",
    )
