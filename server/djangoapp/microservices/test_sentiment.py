#!/usr/bin/env python3
import sys
import urllib.parse
import requests

BASE_URL = "http://localhost:5000/analyze/"


def analyze(text: str):
    encoded = urllib.parse.quote(text)
    url = BASE_URL + encoded
    print(f"\n>>> Sending: {text!r}")
    print(f"URL: {url}")
    resp = requests.get(url)
    print("Status:", resp.status_code)
    try:
        print("Response JSON:", resp.json())
    except Exception:
        print("Raw response:", resp.text)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Text from command line: python test_sentiment.py "my text here"
        phrase = " ".join(sys.argv[1:])
        analyze(phrase)
    else:
        # No args: run a few predefined test reviews
        test_phrases = [
            "Amazing ship, smooth flight and very fast hyperdrive. I’m extremely happy with my purchase.",
            "Great value, comfortable cabin, and the engine is reliable. I would definitely buy here again.",
            "Terrible quality, the reactor failed on the second trip. I’m very disappointed.",
            "The ship is slow, noisy, and overpriced. I regret buying it.",
        ]
        for phrase in test_phrases:
            analyze(phrase)
