"""Secure Kaggle authentication helper.

Use Kaggle Secrets/environment variables. Never commit kaggle.json or an API key.
"""
import os

username = os.getenv("KAGGLE_USERNAME")
key = os.getenv("KAGGLE_KEY")
if not username or not key:
    raise RuntimeError(
        "Kaggle credentials are missing. Configure KAGGLE_USERNAME and KAGGLE_KEY "
        "through Kaggle Secrets/environment variables; do not put credentials in the notebook."
    )

print("Kaggle credentials detected from environment; secret value is not printed.")
