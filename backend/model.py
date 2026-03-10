"""YOLOv11n-cls model loading and inference."""
from pathlib import Path
from PIL import Image

_model = None
WEIGHTS_PATH = Path(__file__).parent / "weights" / "best.pt"
INFERENCE_IMG_SIZE = 224


def _load_model():
    global _model
    if _model is None:
        if not WEIGHTS_PATH.exists():
            raise FileNotFoundError(
                f"Model weights not found at {WEIGHTS_PATH}. "
                "Please train the model on Google Colab and place best.pt in backend/weights/."
            )
        from ultralytics import YOLO
        _model = YOLO(str(WEIGHTS_PATH))
    return _model


def predict(image: Image.Image) -> dict:
    """Run YOLOv11n-cls inference on a PIL image.

    Returns a dict with keys: class_name, confidence, top5.
    """
    model = _load_model()
    results = model.predict(image, imgsz=INFERENCE_IMG_SIZE, verbose=False)
    result = results[0]

    # Classification results
    probs = result.probs
    top1_idx = int(probs.top1)
    class_name = result.names[top1_idx]
    confidence = float(probs.top1conf)

    top5_indices = probs.top5
    top5 = [
        {
            "class": result.names[int(idx)],
            "confidence": float(probs.data[int(idx)]),
        }
        for idx in top5_indices
    ]

    return {
        "class_name": class_name,
        "confidence": confidence,
        "top5": top5,
    }
