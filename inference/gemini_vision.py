"""
Please refer to https://ai.google.dev/tutorials/python_quickstart to get the API key

Install with `pip install -q -U google-generativeai`,
Then `python gemini_vision.py --priviq_path /path/to/privIQ --google_api_key YOUR_API_KEY`
"""

import os
import time
from pathlib import Path
import google.generativeai as genai
import argparse
from utils import evaluate_on_priviq

class Gemini:
    def __init__(self, model="gemini-1.5-flash"):
        self.model = genai.GenerativeModel(model)

    def get_response(self, image_path, prompt) -> str:
        # Query the model
        text = ""
        while len(text) < 1:
            try:
                image_path = Path(image_path)
                image = {
                    'mime_type': f'image/{image_path.suffix[1:].replace("jpg", "jpeg")}',
                    'data': image_path.read_bytes()
                }
                response = self.model.generate_content(
                    [
                        # Add an example image
                        image,
                        # Add an example query
                        prompt,
                    ]
                )
                try:
                    text = response.text
                except:
                    text = " "
            except Exception as error:
                print(error)
                print('Sleeping for 10 seconds')
                time.sleep(10)
        return text.strip()


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--priviq_path",
        type=str,
        default="/path/to/privIQ",
        help="Download privIQ.zip and `unzip privIQ.zip` and change the path here",
    )
    parser.add_argument(
        "--result_path",
        type=str,
        default="results",
    )
    parser.add_argument(
        "--google_api_key", type=str, default=None,
        help="refer to https://ai.google.dev/tutorials/python_quickstart"
    )
    parser.add_argument(
        "--model_name",
        type=str,
        default="gemini-1.5-flash",
        help="Gemini model name",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = arg_parser()

    # prepare the model
    if args.google_api_key:
        GOOGLE_API_KEY = args.google_api_key
    else:
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    if GOOGLE_API_KEY is None:
        raise ValueError("Please set the GOOGLE_API_KEY environment variable or pass it as an argument")

    genai.configure(api_key=GOOGLE_API_KEY)
    model = Gemini(model=args.model_name)

    # evaluate on privIQ
    evaluate_on_priviq(args, model)
