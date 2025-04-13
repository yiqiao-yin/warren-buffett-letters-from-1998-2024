# 🧠 Warren Buffett Letters Q&A Dataset Pipeline

This repository contains a Python-based pipeline that uses OCR and large language models (LLMs) to extract **questions**, **answers**, and **reasoning** from Warren Buffett's annual letters. It is structured to be modular, enabling clean data curation and publishing to the Hugging Face Hub.

---

## 📦 Project Structure

```bash
.
├── curate_data.py         # Extracts QAR triplets from OCR'd pages
├── helper.py              # Defines ChatBot class for LLM interaction
├── push_to_hf.py          # Loads and uploads dataset to Hugging Face
├── requirements.txt       # Python dependencies
└── wb_dataset/            # [Generated] Local folder storing the dataset
```

---

## 🛠 Requirements

Install dependencies into a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```

---

## 🔍 curate_data.py

This script performs the following steps:

1. **Downloads Warren Buffett letters (PDFs)**.
2. **Uses Mistral OCR** to extract text in Markdown format.
3. **Uses Together LLM API** to generate:
   - 1 insightful question from each paragraph.
   - 1 concise answer derived from the paragraph.
   - 1 clear explanation of how the answer can be inferred from the text.
4. **Appends the results into a Python list**.
5. **Saves the result using `datasets.Dataset.save_to_disk()`**, creating a local folder (`wb_dataset/`) with binary files.

```python
dataset = Dataset.from_list(results)
dataset.save_to_disk("wb_dataset")
```

The folder `wb_dataset/` is now your locally saved dataset.

---

## 💬 helper.py

This defines a `ChatBot` class which:

- Initializes a Together client.
- Appends messages to the chat history.
- Sends requests to the LLM API with parameters like `temperature`, `top_p`, etc.
- Handles streaming responses and collapses them into a final string.

Useful for programmatic LLM conversations with history and sampling.

---

## 💾 Local Dataset Storage

Using 🤗 `datasets`:

### Save

```python
dataset.save_to_disk("wb_dataset")
```

This creates a directory:

```
wb_dataset/
├── dataset_info.json
├── state.json
└── data-00000-of-00001.arrow
```

### Load

```python
from datasets import load_from_disk
dataset = load_from_disk("wb_dataset")
```

This reloads the same dataset in memory.

---

## ⬆️ push_to_hf.py

Uploads the local dataset to Hugging Face Hub.

1. Loads local dataset.
2. Wraps it in `DatasetDict`.
3. Saves again in HF-compatible format.
4. Pushes using `.push_to_hub()`.

```python
dataset_dict.push_to_hub("eagle0504/warren-buffett-letters-qna-r1-enhanced-1998-2024")
```

Once pushed, your dataset is available at:

📎 [https://huggingface.co/datasets/eagle0504/warren-buffett-letters-qna-r1-enhanced-1998-2024](https://huggingface.co/datasets/eagle0504/warren-buffett-letters-qna-r1-enhanced-1998-2024)

---

## ✍️ Notes

- API keys for Mistral, Together, and Hugging Face should be manually filled in each script.
- This modular setup enables automation and reuse across future updates.
- Data is stored efficiently using Apache Arrow and loads fast.

---

## 📬 Contact

Author: [Yiqiao Yin](https://github.com/eagle0504)  
Email: eagle0504@gmail.com  
```
