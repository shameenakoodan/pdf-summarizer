# 📄 AI PDF Summarizer

An AI-powered web app that extracts and summarizes long PDF documents into concise, readable insights using modern LLMs.

---

## 🚀 Overview

The **AI PDF Summarizer** allows users to upload a PDF and instantly receive a structured summary. It handles long documents efficiently using **chunking and multi-step summarization**, making it ideal for research papers, reports, and large documents.

---

## ✨ Features

* 📥 Upload any PDF file
* 📄 Extracts text automatically
* 🧠 AI-powered summarization (LLMs)
* 🔄 Handles large PDFs with chunking
* 📌 Clean and readable summary output
* 📥 Download summary as a PDF
* ⚡ Simple and interactive UI using Streamlit

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **AI Model:** Groq (Llama 3.1)
* **Libraries Used:**

  * PyPDF / custom PDF reader
  * FPDF (for PDF generation)
  * LLM APIs (Groq)

---

## 📂 Project Structure

```bash id="n2f8ka"
.
├── app.py                # Main Streamlit app
├── pdf_reader.py        # Extracts text from PDFs
├── summarizer.py        # Handles AI summarization
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙️ How It Works

1. User uploads a PDF
2. Text is extracted using a PDF parser
3. Large text is split into chunks
4. Each chunk is summarized using an LLM
5. Summaries are combined into a final result
6. User can download the summary as a PDF

---

## 🧪 Installation & Setup

### 1. Clone the repository

```bash id="b3lf41"
git clone https://github.com/shameenakoodan/pdf-summarizer.git
cd pdf-summarizer
```

### 2. Install dependencies

```bash id="z0wq5p"
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file and add your API key:

```env id="h3t9mw"
GROQ_API_KEY=your_api_key_here
```

---

### 4. Run the app

```bash id="yz2rjk"
streamlit run app.py
```

---

## 📸 UI Preview

* Upload PDF
* Click **Summarize PDF**
* View summary
* Download summary as PDF

---

## 📦 Example Use Cases

* 📚 Research paper summaries
* 🧾 Business reports
* 📑 Legal documents
* 🎓 Study notes
* 📊 Data-heavy PDFs

---

## 🔐 Notes

* Works best with **text-based PDFs** (not scanned images)
* Large PDFs may take longer depending on API response time

---

<!-- ## 🚀 Future Improvements

* Add support for scanned PDFs (OCR)
* Multi-language summarization
* Highlight key insights / bullet summaries
* Add summary length control (short / medium / detailed)
* Save user history

--- -->

## 👤 Author

**Shameena Koodan**

* GitHub: https://github.com/shameenakoodan
* LinkedIn: https://www.linkedin.com/in/shameenakoodan

---

<!-- ## 📄 License

This project is licensed under the MIT License.

--- -->

> Built with ❤️ using AI + Streamlit
