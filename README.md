# 🌿 PlantGuard AI — Plant Disease Detection

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![YOLOv11](https://img.shields.io/badge/YOLOv11n-cls-brightgreen)
![PlantVillage](https://img.shields.io/badge/Dataset-PlantVillage-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Detect plant diseases in seconds using **YOLOv11n** trained on the **PlantVillage** dataset (38 disease classes). Includes a **FastAPI** backend, a modern web frontend, and a **Kisan Assistant** chatbot for agriculture Q&A.

---

## 🏗️ Architecture

```
Browser (GitHub Pages frontend)
      │
      │  API calls (fetch)
      ▼
Render (FastAPI backend)
      │  uses
      ├──► best.pt  (trained on Google Colab)
      └──► chatbot_data.json (knowledge base)
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| AI Model | YOLOv11n-cls (Ultralytics) |
| Backend | FastAPI + Uvicorn |
| Dataset | PlantVillage (via TensorFlow Datasets) |
| Frontend | HTML5 / CSS3 / Vanilla JS |
| Deployment | Docker (Render) + GitHub Pages |

---

## 📂 Project Structure

```
├── backend/
│   ├── main.py              # FastAPI server
│   ├── model.py             # YOLOv11n model loading & inference
│   ├── remedies.py          # Disease → remedy mapping (38 classes)
│   ├── chatbot_data.json    # Kisan Assistant knowledge base
│   ├── requirements.txt
│   ├── Dockerfile
│   └── weights/
│       └── .gitkeep         # Place best.pt here after Colab training
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── docs/                    # GitHub Pages deployment (copy of frontend)
│   ├── index.html
│   ├── style.css
│   └── script.js
└── .devcontainer/
    └── devcontainer.json
```

---

## 🚀 Step 1: Train on Google Colab

Open a new Colab notebook and run the following cells in order.

### Cell 1 — Install dependencies
```python
!pip install ultralytics tensorflow-datasets -q
```

### Cell 2 — Download PlantVillage and prepare YOLO dataset
```python
import tensorflow_datasets as tfds
import shutil, os
from PIL import Image
import numpy as np

# Download PlantVillage
ds, info = tfds.load("plant_village", split="train", with_info=True, as_supervised=True)
class_names = info.features["label"].names
print(f"Classes: {len(class_names)}")

# Create YOLO classification directory structure
BASE = "/content/datasets"
for split in ["train", "val"]:
    for name in class_names:
        os.makedirs(f"{BASE}/{split}/{name}", exist_ok=True)

# Split 80/20
all_samples = list(ds)
np.random.shuffle(all_samples)
split_idx = int(len(all_samples) * 0.8)
train_samples = all_samples[:split_idx]
val_samples   = all_samples[split_idx:]

def save_samples(samples, split):
    counters = {}
    for img_tensor, label in samples:
        name = class_names[label.numpy()]
        counters[name] = counters.get(name, 0) + 1
        img = Image.fromarray(img_tensor.numpy().astype("uint8"))
        img.save(f"{BASE}/{split}/{name}/{counters[name]}.jpg")

save_samples(train_samples, "train")
save_samples(val_samples, "val")
print("Dataset prepared!")
```

### Cell 3 — Train YOLOv11n-cls
```python
from ultralytics import YOLO
model = YOLO("yolo11n-cls.pt")
results = model.train(
    data="/content/datasets",
    epochs=30,
    imgsz=224,
    batch=64,
    project="/content/runs",
    name="plantguard",
)
```

### Cell 4 — Verify on a random val image
```python
import glob, random
from PIL import Image

val_images = glob.glob("/content/datasets/val/**/*.jpg", recursive=True)
img_path = random.choice(val_images)
img = Image.open(img_path)

best_model = YOLO("/content/runs/plantguard/weights/best.pt")
result = best_model.predict(img, imgsz=224, verbose=True)
print("Prediction:", result[0].names[result[0].probs.top1])
img.show()
```

### Cell 5 — Download best.pt
```python
from google.colab import files
files.download("/content/runs/plantguard/weights/best.pt")
```

---

## 🖥️ Step 2: Setup in Codespace / Local Dev

```bash
# 1. Clone the repository
git clone https://github.com/Shivam3-byte/YOLOV11n_Plant-DiseaseDetection.git
cd YOLOV11n_Plant-DiseaseDetection

# 2. Place your trained weights
cp /path/to/best.pt backend/weights/best.pt

# 3. Install Python dependencies
cd backend
pip install -r requirements.txt

# Fix OpenCV headless conflict if needed
pip uninstall opencv-python -y
pip install opencv-python-headless

# 4. Start the backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 5. Open frontend/index.html in a browser (or use Live Server in VS Code)
```

---

## ☁️ Step 3: Deploy Backend on Render

1. Push your code (with `backend/weights/best.pt`) to GitHub.
2. Go to [render.com](https://render.com) → **New → Web Service**.
3. Connect your GitHub repository.
4. Set **Root Directory** to `backend`.
5. Set **Runtime** to `Docker`.
6. Set **Health Check Path** to `/health`.
7. Click **Deploy**.

---

## 🌐 Step 4: Deploy Frontend on GitHub Pages

1. Update `API_BASE` in `docs/script.js` to your Render URL:
   ```js
   const API_BASE = "https://your-app.onrender.com";
   ```
2. Commit and push the change.
3. In GitHub repo → **Settings → Pages** → Source: **Deploy from a branch** → Branch: `main`, Folder: `/docs`.
4. Your frontend is now live at `https://<username>.github.io/<repo>/`.

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/`      | Root / health check |
| `GET`  | `/health` | Health check — `{"status":"ok"}` |
| `POST` | `/predict` | Upload image → disease prediction + remedy |
| `POST` | `/chat`   | Send message → Kisan Assistant reply |
| `GET`  | `/chat/suggestions` | Get 6 suggestion chips |

### `/predict` request
```
Content-Type: multipart/form-data
file: <image file>  (JPG / PNG / WEBP, max 10 MB)
```

### `/predict` response
```json
{
  "prediction": {
    "class": "Tomato___Early_blight",
    "confidence": 94.7,
    "top5": [
      {"class": "Tomato___Early_blight", "confidence": 94.7},
      ...
    ]
  },
  "result": {
    "plant": "Tomato",
    "disease": "Early Blight",
    "status": "diseased",
    "remedy": "**Tomato Early Blight Treatment:**\n..."
  }
}
```

---

## ✅ Final Checklist

| Step | Task | Status |
|------|------|--------|
| 1 | Train YOLOv11n on Colab | ⬜ Manual step |
| 2 | Download `best.pt` to `backend/weights/` | ⬜ Manual step |
| 3 | Test locally with `uvicorn main:app --reload` | ⬜ Manual step |
| 4 | Deploy backend to Render | ⬜ Manual step |
| 5 | Update `API_BASE` in `docs/script.js` | ⬜ Manual step |
| 6 | Enable GitHub Pages from `/docs` | ⬜ Manual step |
| 7 | All 38 disease classes covered in `remedies.py` | ✅ Done |
| 8 | Kisan Assistant chatbot with 12+ Q&A entries | ✅ Done |
| 9 | Responsive UI with modern green theme | ✅ Done |
