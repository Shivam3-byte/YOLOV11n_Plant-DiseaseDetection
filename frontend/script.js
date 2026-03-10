/* jshint esversion: 6 */
const API_BASE = "http://localhost:8000";

// ============================================================
// Disease Detector
// ============================================================
const dropZone    = document.getElementById("dropZone");
const fileInput   = document.getElementById("fileInput");
const previewArea = document.getElementById("previewArea");
const previewImg  = document.getElementById("previewImage");
const analyseBtn  = document.getElementById("analyseBtn");
const clearBtn    = document.getElementById("clearBtn");
const loaderArea  = document.getElementById("loaderArea");
const statusBanner= document.getElementById("statusBanner");
const resultsGrid = document.getElementById("resultsGrid");
const remedyCard  = document.getElementById("remedyCard");
const remedyText  = document.getElementById("remedyText");
const top5Accordion=document.getElementById("top5Accordion");
const top5Btn     = document.getElementById("top5Btn");
const top5Content = document.getElementById("top5Content");
const top5List    = document.getElementById("top5List");
const accordionArrow=document.getElementById("accordionArrow");

let selectedFile = null;

// Drop zone events
dropZone.addEventListener("click", () => fileInput.click());

dropZone.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropZone.classList.add("drag-over");
});

dropZone.addEventListener("dragleave", () => {
  dropZone.classList.remove("drag-over");
});

dropZone.addEventListener("drop", (e) => {
  e.preventDefault();
  dropZone.classList.remove("drag-over");
  const file = e.dataTransfer.files[0];
  if (file) handleFile(file);
});

fileInput.addEventListener("change", () => {
  if (fileInput.files[0]) handleFile(fileInput.files[0]);
});

function handleFile(file) {
  const allowed = ["image/jpeg", "image/png", "image/webp"];
  if (!allowed.includes(file.type)) {
    alert("Unsupported file type. Please upload a JPG, PNG, or WEBP image.");
    return;
  }
  selectedFile = file;
  const reader = new FileReader();
  reader.onload = (e) => {
    previewImg.src = e.target.result;
    previewArea.style.display = "block";
    dropZone.style.display = "none";
    hideResults();
  };
  reader.readAsDataURL(file);
}

clearBtn.addEventListener("click", () => {
  selectedFile = null;
  fileInput.value = "";
  previewArea.style.display = "none";
  dropZone.style.display = "block";
  hideResults();
});

analyseBtn.addEventListener("click", async () => {
  if (!selectedFile) return;

  loaderArea.style.display = "block";
  hideResults();
  analyseBtn.disabled = true;

  const formData = new FormData();
  formData.append("file", selectedFile);

  try {
    const resp = await fetch(`${API_BASE}/predict`, {
      method: "POST",
      body: formData,
    });

    if (!resp.ok) {
      const err = await resp.json();
      throw new Error(err.detail || `Server error: ${resp.status}`);
    }

    const data = await resp.json();
    showResult(data);
  } catch (err) {
    statusBanner.style.display = "block";
    statusBanner.className = "status-banner status-diseased";
    statusBanner.textContent = `⚠️ Error: ${err.message}`;
  } finally {
    loaderArea.style.display = "none";
    analyseBtn.disabled = false;
  }
});

function showResult(data) {
  const { prediction, result } = data;
  const isHealthy = result.status === "healthy";

  // Status banner
  statusBanner.style.display = "block";
  statusBanner.className = `status-banner ${isHealthy ? "status-healthy" : "status-diseased"}`;
  statusBanner.textContent = isHealthy
    ? `✅ ${result.plant} plant looks healthy!`
    : `⚠️ Detected: ${result.disease} on ${result.plant}`;

  // Result cards
  document.getElementById("resPlant").textContent      = result.plant || "—";
  document.getElementById("resDisease").textContent    = result.disease || "—";
  document.getElementById("resConfidence").textContent = `${prediction.confidence}%`;
  resultsGrid.style.display = "grid";

  // Remedy
  remedyText.innerHTML = formatBotReply(result.remedy);
  remedyCard.style.display = "block";

  // Top-5 accordion
  top5List.innerHTML = "";
  prediction.top5.forEach((item) => {
    const li = document.createElement("li");
    li.innerHTML = `<span class="top5-class">${item.class.replace(/_/g, " ")}</span>
                    <span class="top5-conf">${item.confidence}%</span>`;
    top5List.appendChild(li);
  });
  top5Accordion.style.display = "block";
}

function hideResults() {
  statusBanner.style.display  = "none";
  resultsGrid.style.display   = "none";
  remedyCard.style.display    = "none";
  top5Accordion.style.display = "none";
  top5Content.style.display   = "none";
  accordionArrow.textContent  = "▼";
}

// Accordion toggle
top5Btn.addEventListener("click", () => {
  const isOpen = top5Content.style.display === "block";
  top5Content.style.display = isOpen ? "none" : "block";
  accordionArrow.textContent = isOpen ? "▼" : "▲";
});

// Chatbot nav link opens chatbot
document.getElementById("chatbot-nav-btn").addEventListener("click", (e) => {
  e.preventDefault();
  openChat();
});

// ============================================================
// Chatbot
// ============================================================
const chatbotToggle = document.getElementById("chatbotToggle");
const chatWindow    = document.getElementById("chatWindow");
const chatClose     = document.getElementById("chatClose");
const chatMessages  = document.getElementById("chatMessages");
const chatInput     = document.getElementById("chatInput");
const chatSend      = document.getElementById("chatSend");
const suggestionsRow= document.getElementById("suggestionsRow");

chatbotToggle.addEventListener("click", openChat);
chatClose.addEventListener("click", () => chatWindow.classList.remove("open"));

function openChat() {
  chatWindow.classList.add("open");
  chatInput.focus();
  if (suggestionsRow.childElementCount === 0) loadSuggestions();
}

async function loadSuggestions() {
  try {
    const resp = await fetch(`${API_BASE}/chat/suggestions`);
    if (!resp.ok) return;
    const data = await resp.json();
    data.suggestions.forEach((q) => {
      const chip = document.createElement("button");
      chip.className = "chip";
      chip.textContent = q;
      chip.addEventListener("click", () => sendChat(q));
      suggestionsRow.appendChild(chip);
    });
  } catch (_) {
    // Silently fail if backend not available
  }
}

chatSend.addEventListener("click", () => {
  const msg = chatInput.value.trim();
  if (msg) {
    sendChat(msg);
    chatInput.value = "";
  }
});

chatInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    const msg = chatInput.value.trim();
    if (msg) {
      sendChat(msg);
      chatInput.value = "";
    }
  }
});

async function sendChat(message) {
  // Show user bubble
  appendBubble(message, "user");

  // Typing indicator
  const typingBubble = appendBubble("⏳ Thinking…", "bot");

  try {
    const resp = await fetch(`${API_BASE}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    if (!resp.ok) throw new Error("Server error");
    const data = await resp.json();
    typingBubble.innerHTML = formatBotReply(data.response);
  } catch (err) {
    typingBubble.textContent = "⚠️ Unable to reach the assistant. Please check the backend is running.";
  }

  scrollToBottom();
}

function appendBubble(text, role) {
  const div = document.createElement("div");
  div.className = `chat-bubble ${role}`;
  div.textContent = text;
  chatMessages.appendChild(div);
  scrollToBottom();
  return div;
}

function scrollToBottom() {
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function formatBotReply(text) {
  // Convert **bold** → <strong>, newlines → <br/>
  return text
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(/\n/g, "<br/>");
}
