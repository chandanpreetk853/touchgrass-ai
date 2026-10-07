# 🌿 TouchGrass AI

**TouchGrass AI** is a local AI-powered outdoor adventure generator designed to help people spend less time on screens and more time exploring the real world.

Instead of endlessly scrolling, the user chooses:

* ⏱️ Available time
* ⚡ Energy level
* 📍 Location type

To<img width="660" height="434" alt="Screenshot 2026-10-07 223024" src="https://github.com/user-attachments/assets/7e0fac51-e05c-4f31-8001-7422afa347d9" />
<img width="660" height="434" alt="Screenshot 2026-10-07 223024" src="https://github.com/user-attachments/assets/1e25ff44-0afc-4d8d-877d-456348c11359" />
uchGrass AI then uses a **local Gemma model through Ollama** to generate a personalized outdoor micro-adventure.

## ✨ Features

* 🤖 Local AI generation using Gemma
* 🔒 No cloud AI API required
* 🌱 Personalized outdoor quests
* ⏱️ Built-in adventure timer
* 📝 Post-adventure reflection
* 💾 Reflection and quest history stored locally
* 📱 Simple web interface
* ⚡ Lightweight Python backend

## 🧠 How It Works

```text
User
  ↓
TouchGrass Web App
  ↓
Python Server
  ↓
Ollama
  ↓
Gemma 3 1B
  ↓
Personalized Outdoor Quest
  ↓
User Goes Outside 🌿
```

## 🛠️ Tech Stack

* HTML
* CSS
* JavaScript
* Python
* Ollama
* Gemma 3 1B
* Web APIs
* LocalStorage

## 🚀 Run Locally

### 1. Install Ollama

Install Ollama and make sure a Gemma model is available.

Example:

```bash
ollama pull gemma3:1b
```

### 2. Clone the repository

```bash
git clone https://github.com/chandanpreetk853/touchgrass-ai.git
cd touchgrass-ai
```

### 3. Start Ollama

Make sure Ollama is running.

### 4. Start the Python server

```bash
python app.py
```

### 5. Open the application

Open:

```text
http://localhost:8000
```

## 🔐 Privacy

TouchGrass AI is designed around local processing.

The AI request is sent to a locally running Ollama server rather than a remote AI API.

Quest history and reflections are stored in the browser's local storage.

## 🌎 Why TouchGrass?

Modern life can keep us constantly connected to screens.

TouchGrass AI uses AI for a different purpose:

> **Use technology to help you step away from technology.**

The goal is simple:

**Generate → Go outside → Explore → Reflect 🌿**

## 📌 Project Status

This is an early learning project and prototype.

Future improvements could include:

* Weather-aware quests
* Location-based challenges
* More activity categories
* Better accessibility
* Quest difficulty levels
* Offline-first improvements
* Achievement system
* More local AI models

## 📄 License

This project is open source and available for learning and experimentation.Built with local AI using Ollama + Gemma 3 1B. 🌿
