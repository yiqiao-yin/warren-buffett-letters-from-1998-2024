import os
from mistralai import Mistral
from datasets import Dataset
from helper import ChatBot
from typing import List, Dict

# === CONFIGURATION ===
MISTRAL_API_KEY = "xxx"
TOGETHER_API_KEY = "xxx"

list_of_letters = [
    "https://www.berkshirehathaway.com/letters/2024ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2023ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2022ltr.pdf", 
    "https://www.berkshirehathaway.com/letters/2021ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2020ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2019ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2018ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2017ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2016ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2015ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2014ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2013ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2012ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2011ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2010ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2009ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2008ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2007ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2006ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2005ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2004ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2003ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2002pdf.pdf",
    "https://www.berkshirehathaway.com/letters/2001pdf.pdf",
    "https://www.berkshirehathaway.com/letters/2000pdf.pdf",
    "https://www.berkshirehathaway.com/letters/1999pdf.pdf",
    "https://www.berkshirehathaway.com/letters/1998pdf.pdf"
]

print(f"Number of letters: {len(list_of_letters)}")

# === Step 1: OCR the first letter ===
# client = Mistral(api_key=MISTRAL_API_KEY)

# ocr_response = client.ocr.process(
#     model="mistral-ocr-latest",
#     document={"type": "document_url", "document_url": list_of_letters[0]},
#     include_image_base64=True
# )

# Start
array_of_pages = []

for i in range(len(list_of_letters)):
    try:
        # Define client
        client = Mistral(api_key=MISTRAL_API_KEY)

        # API call
        ocr_response = client.ocr.process(
            model="mistral-ocr-latest",
            document={
                "type": "document_url",
                "document_url": list_of_letters[i]
            },
            include_image_base64=True
        )

        # Append data
        array_of_pages.append(ocr_response.dict()['pages'])

        # Checkpoint
        print(f"--- finished with document: {i}, {list_of_letters[i]}")
    except:
        print(f"--- failed with document: {i}, {list_of_letters[i]}")
# End

# === Step 2: Run QAR generation ===
num_of_sampling = 20
results: List[Dict[str, str]] = []

for i in range(len(array_of_pages)):
    tmp_doc = array_of_pages[i]
    for j in range(len(tmp_doc)):
        tmp_page = tmp_doc[j]
        markdown_text = tmp_page.get("markdown", "")

        for k in range(num_of_sampling):
            try:
                bot = ChatBot(api_key=TOGETHER_API_KEY)
                bot.history = [{"role": "assistant", "content": f"Here is some paragraph written by investor Warren Buffett: {markdown_text}"}]

                bot.append_history(role="user", content="What is a good question worth being asked from this paragraph? Please only provide question.")
                question = bot.invoke_api(temperature=0.9)

                bot.append_history(role="user", content="What is a good answer that can be derived from above paragraph and question? Please only provide answer.")
                answer = bot.invoke_api(temperature=0.1)

                bot.append_history(role="user", content="Give me reasoning to show how to arrive with answer above from paragraph and question. Please only provide reasoning.")
                reasoning = bot.invoke_api(temperature=0.1)

                print(f"[{i}-{j}-{k}] ✅ Success\nQ: {question}\nA: {answer}\nR: {reasoning}\n")

                results.append({
                    "question": question.strip(),
                    "answer": answer.strip(),
                    "reasoning": reasoning.strip()
                })

            except Exception as e:
                print(f"[{i}-{j}-{k}] ❌ Failed - {e}")

# === Step 3: Save locally ===
dataset = Dataset.from_list(results)
output_data_test_name = "wb_dataset"
dataset.save_to_disk(output_data_test_name)
print(f"Dataset saved locally to: {output_data_test_name}")
