# Week 4 – Tokenizer Comparison

This practical compares three pretrained subword tokenizers using the same English, Telugu, and Hindi sentences.

## Tokenizers used

- BPE: GPT-2 (`gpt2`)
- WordPiece: Multilingual BERT (`bert-base-multilingual-cased`)
- SentencePiece: XLM-R (`xlm-roberta-base`)

## Setup

Activate your existing lab virtual environment, then install the packages:

```powershell
python -m pip install -r requirements.txt
```

The first run needs internet access because Hugging Face downloads the pretrained tokenizer files.

## Run

```powershell
python tokenizer_comparison.py
```

For each language and tokenizer, the program prints the token pieces, token IDs, and token count.

## Important comparison note

These are real pretrained tokenizers with different vocabularies and training data, not three algorithms trained on identical data. GPT-2 is primarily English-trained, while multilingual BERT and XLM-R are multilingual. Therefore, token-count differences reflect both tokenizer design and model training.

SentencePiece is a tokenizer framework; XLM-R uses SentencePiece with a BPE model. A lower token count alone does not prove a tokenizer is better.
