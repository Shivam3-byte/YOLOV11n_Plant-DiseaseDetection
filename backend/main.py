"""FastAPI backend for PlantGuard AI — Plant Disease Detection."""
import io
import json
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from pydantic import BaseModel

from remedies import get_remedy

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = FastAPI(title="PlantGuard AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Load chatbot knowledge base once at startup
# ---------------------------------------------------------------------------
_CHATBOT_DATA_PATH = Path(__file__).parent / "chatbot_data.json"
with open(_CHATBOT_DATA_PATH, encoding="utf-8") as _f:
    _CHATBOT_DATA = json.load(_f)


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@app.get("/")
@app.get("/health")
async def health_check():
    return {"status": "ok", "model": "YOLOv11n-cls PlantVillage"}


@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    """Accept an image upload and return disease prediction + remedy."""
    # Validate content type
    allowed_types = {"image/jpeg", "image/png", "image/webp"}
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{file.content_type}'. Use JPG, PNG, or WEBP.",
        )

    # Read and size-check
    contents = await file.read()
    if len(contents) > 10 * 1024 * 1024:  # 10 MB
        raise HTTPException(status_code=400, detail="File too large. Maximum size is 10 MB.")

    # Open image
    try:
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Could not open image file.")

    # Run inference (lazy model load)
    try:
        from model import predict as run_inference

        prediction = run_inference(image)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Inference error: {exc}")

    remedy = get_remedy(prediction["class_name"])

    return {
        "prediction": {
            "class": prediction["class_name"],
            "confidence": round(prediction["confidence"] * 100, 2),
            "top5": [
                {
                    "class": item["class"],
                    "confidence": round(item["confidence"] * 100, 2),
                }
                for item in prediction["top5"]
            ],
        },
        "result": remedy,
    }


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(request: ChatRequest):
    """Match user message to chatbot knowledge base and return best answer."""
    import re
    message_lower = request.message.lower().strip()
    # Strip punctuation for more flexible greeting/keyword matching
    message_clean = re.sub(r"[^\w\s]", "", message_lower)

    if not message_lower:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    # Check greetings
    greeting_patterns = _CHATBOT_DATA.get("greetings", {}).get("patterns", [])
    for pattern in greeting_patterns:
        if pattern in message_clean or pattern in message_lower:
            return {"response": _CHATBOT_DATA["greetings"]["response"]}

    # Match QA by keyword scoring
    best_entry = None
    best_score = 0
    for entry in _CHATBOT_DATA.get("qa", []):
        score = sum(1 for kw in entry.get("keywords", []) if kw in message_lower)
        if score > best_score:
            best_score = score
            best_entry = entry

    if best_entry and best_score > 0:
        return {"response": best_entry["answer"]}

    # Fallback
    return {"response": _CHATBOT_DATA.get("fallback", "I'm not sure about that. Please try another question.")}


@app.get("/chat/suggestions")
async def chat_suggestions():
    """Return the first 6 QA questions as suggestion chips."""
    qa_list = _CHATBOT_DATA.get("qa", [])
    suggestions = [entry["question"] for entry in qa_list[:6]]
    return {"suggestions": suggestions}
