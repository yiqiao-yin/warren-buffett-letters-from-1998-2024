# 📄 Berkshire Hathaway Letters Processing

Welcome to the project for processing Warren Buffett's annual letters. In this README, you'll find the steps to access and process these historical documents with the Mistral AI API.

Index for `.jsonl` files:

Here is the markdown table for your list of URLs. Each entry has an index and its corresponding URL:

| Index | URL                                                |
|-------|----------------------------------------------------|
| 0     | [2024ltr](https://www.berkshirehathaway.com/letters/2024ltr.pdf)  |
| 1     | [2023ltr](https://www.berkshirehathaway.com/letters/2023ltr.pdf)  |
| 2     | [2022ltr](https://www.berkshirehathaway.com/letters/2022ltr.pdf)  |
| 3     | [2021ltr](https://www.berkshirehathaway.com/letters/2021ltr.pdf)  |
| 4     | [2020ltr](https://www.berkshirehathaway.com/letters/2020ltr.pdf)  |
| 5     | [2019ltr](https://www.berkshirehathaway.com/letters/2019ltr.pdf)  |
| 6     | [2018ltr](https://www.berkshirehathaway.com/letters/2018ltr.pdf)  |
| 7     | [2017ltr](https://www.berkshirehathaway.com/letters/2017ltr.pdf)  |
| 8     | [2016ltr](https://www.berkshirehathaway.com/letters/2016ltr.pdf)  |
| 9     | [2015ltr](https://www.berkshirehathaway.com/letters/2015ltr.pdf)  |
| 10    | [2014ltr](https://www.berkshirehathaway.com/letters/2014ltr.pdf)  |
| 11    | [2013ltr](https://www.berkshirehathaway.com/letters/2013ltr.pdf)  |
| 12    | [2012ltr](https://www.berkshirehathaway.com/letters/2012ltr.pdf)  |
| 13    | [2011ltr](https://www.berkshirehathaway.com/letters/2011ltr.pdf)  |
| 14    | [2010ltr](https://www.berkshirehathaway.com/letters/2010ltr.pdf)  |
| 15    | [2009ltr](https://www.berkshirehathaway.com/letters/2009ltr.pdf)  |
| 16    | [2008ltr](https://www.berkshirehathaway.com/letters/2008ltr.pdf)  |
| 17    | [2007ltr](https://www.berkshirehathaway.com/letters/2007ltr.pdf)  |
| 18    | [2006ltr](https://www.berkshirehathaway.com/letters/2006ltr.pdf)  |
| 19    | [2005ltr](https://www.berkshirehathaway.com/letters/2005ltr.pdf)  |
| 20    | [2004ltr](https://www.berkshirehathaway.com/letters/2004ltr.pdf)  |
| 21    | [2003ltr](https://www.berkshirehathaway.com/letters/2003ltr.pdf)  |
| 22    | [2002pdf](https://www.berkshirehathaway.com/letters/2002pdf.pdf)  |
| 23    | [2001pdf](https://www.berkshirehathaway.com/letters/2001pdf.pdf)  |
| 24    | [2000pdf](https://www.berkshirehathaway.com/letters/2000pdf.pdf)  |
| 25    | [1999pdf](https://www.berkshirehathaway.com/letters/1999pdf.pdf)  |
| 26    | [1998pdf](https://www.berkshirehathaway.com/letters/1998pdf.pdf)  |

Each URL is referenced by its year, making it easy to navigate directly from the table.

## 📚 URL Compilation

We have compiled a list of URLs from the Berkshire Hathaway website which point to Warren Buffett's annual letters.

```python
# A list of URLs for each year's letter in PDF format
list_of_letters = [
    "https://www.berkshirehathaway.com/letters/2024ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2023ltr.pdf",
    "https://www.berkshirehathaway.com/letters/2022ltr.pdf",
    # ... Remaining URLs ...
    "https://www.berkshirehathaway.com/letters/1998pdf.pdf"
]

# Output the total number of letters
print(f"Number of letters: {len(list_of_letters)}")
```

## 🔄 Processing Letters with Mistral AI

We loop through each URL to call the Mistral AI API, which processes the content into a more readable format.

```python
import os

# Initialize an empty list to store page data
array_of_pages = []

# Iterate through the list of URLs
for i in range(len(list_of_letters)):
    try:
        # 🎛️ Define the Mistral client with your API key
        client = Mistral(api_key=os.getenv('MISTRAL_API_KEY'))  # Make sure the API key is set in your environment

        # 🔗 Make API call to process the document
        # TODO: Complete the API call functionality

        # 📜 Append the processed data
        # TODO: Determine what data to append and its structure
        
        # Save processed output in JSONL format
        for j in range(len(ocr_response.pages)):
            # TODO: Further processing logic here
            # Aim to transform the output into the desired format

        # Attempt to save the document in JSONL format
        try:
            save_this_jsonl("filename.jsonl")  # Specify path and filename
        except:
            print(f"--- failed to save document: {i}, {list_of_letters[i]}")
        
        # Record progress
        print(f"--- finished with document: {i}, {list_of_letters[i]}")
    except Exception as e:
        # Capture and report errors during processing
        print(f"--- failed with document: {i}, {list_of_letters[i]}. Error: {e}")
```

## 📓 Additional Resources

A Jupyter notebook is available for creating the Warren Buffett letter dataset. Note that API calls may exceed the time limits in hosted environments like Colab. It is recommended to clone the repository and run it locally on your laptop.

[Access the notebook here](./ex__create_warren_buffett_letter_dataset_(1998_2024).ipynb)

---

### 🚀 Tips:
- 📥 Make sure your API key is securely stored and accessed when running the script.
- 🐍 Ensure Python and necessary packages are installed in your environment.
- ⚙️ Customize the logic in the placeholders (`TODO`) according to your data processing needs.

This documentation aims to guide you through setting up and executing the processing of Warren Buffett's annual letters efficiently. Enjoy the journey through his insights! 🏆