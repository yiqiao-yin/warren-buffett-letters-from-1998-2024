from datasets import load_from_disk, DatasetDict

# Hugging Face token and repo details
HF_TOKEN = "hf_xxx"                                            # HuggingFace key
user_name = "eagle0504"                                        # HuggingFace username
repo_name = "warren-buffett-letters-qna-r1-enhanced-1998-2024" # new repo ID you want to create

# Load your local dataset
output_data_test_name = "wb_dataset" # After running `curate_data.py` script, it will save a folder. This should be that folder name.
aug_data = load_from_disk(output_data_test_name)

# Wrap it in a DatasetDict
dataset_dict = DatasetDict({"train": aug_data})

# Save locally (optional)
dataset_dict.save_to_disk(f"{output_data_test_name}-correct-format")

# Push to HF Hub (pass token explicitly)
dataset_dict.push_to_hub(f"{user_name}/{repo_name}", token=HF_TOKEN)

print(f"Dataset pushed to: https://huggingface.co/datasets/{user_name}/{repo_name}")
