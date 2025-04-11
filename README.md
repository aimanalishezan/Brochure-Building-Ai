
---

```markdown
# 🕸️ Web Scraping + Brochure Generator with Ollama

A Python-based automation tool that scrapes company websites, intelligently identifies important pages like **About**, **Careers**, and **Company**, extracts their content, and uses a local LLM (via Ollama) to generate a **polished company brochure**.

---

## 📌 Features

- 🌐 URL scraping and content extraction
- 🔗 Smart link filtering using LLM (e.g., picks relevant links like "About", "Jobs", "Team", etc.)
- 🧠 Local LLM-powered summarization with [llama3.1](https://ollama.com/)
- 📰 Auto-generation of clean, markdown-formatted company brochures
- ⚙️ Easy to run, no frontend needed  

---

## ⚙️ Setup

### 🔧 Prerequisites

- Python 3.9 or newer
- [Ollama](https://ollama.com/) installed and running locally
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `ollama`

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/web-brochure-ollama.git
cd web-brochure-ollama

# Install dependencies
pip install -r requirements.txt
```

---
## 🧭 Workflow

![brochure llm](https://github.com/user-attachments/assets/1555d70d-534b-42ef-ae57-09c7ad1bc8f2)

1. **Input URL**: Provide any company landing page  
2. **Link Discovery**: LLM picks out relevant subpages (like About, Careers)  
3. **Content Scraping**: Scrapes text from each relevant page  
4. **Brochure Creation**: LLM composes a structured brochure in markdown

## 🚀 Usage

To generate a brochure for any website:

```python
create_brochure("Company Name", "https://example.com")
```

Example:

```python
create_brochure("Aiman", "https://aiman-portfolio-mu.vercel.app/")
```

The function will:
- Scrape the landing page
- Analyze all links
- Use Ollama's LLM to summarize relevant content
- Print out a markdown-formatted brochure

---

## 🧠 How It Works (Under the Hood)

- The `Website` class scrapes and extracts clean text from a webpage
- All links on the homepage are passed to the LLM, asking which are brochure-worthy
- The LLM responds with a list of page types and URLs
- Each page is scraped, and the combined content is passed to the LLM again
- The LLM generates a markdown summary acting as a **mini company brochure**

---

## 📁 File Structure

```
web-brochure-ollama/
├── app.py                    # Main script (your provided code)
├── requirements.txt          # Dependencies
├── workflow_diagram.png      # Workflow image (drop it here)
└── README.md                 # This file
```

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute!

---

## 👨‍💻 Author

**MD AIMAN ALI SHEZAN**  
📫 [aimanalishezanbusiness@gmail.com](mailto:aimanalishezanbusiness@gmail.com)

---

## 💡 Tip

Want to convert the markdown brochure to PDF or styled HTML?  
Use any markdown converter like **Markdown to PDF** extensions or `pandoc`.

---

🌟 _If you find this project useful, feel free to star it and share it!_
```

---

Let me know if you want:
- The `requirements.txt` generated
- PDF export of brochures
- Docker support

Or I can even help you deploy this as a **web tool**.
