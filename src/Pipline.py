""" Main pipeline script:
 1. OCR & parse PDFs 
 2. Extract structured JSON via LLM 
 3. Save outputs 
 Usage: python pipeline.py  --input data/raw/your_doc.pdf """ 

import argparse, json, pathlib 
from ocr_extractor import extract_text 
from llm import extract_entities 
def run_pipeline(input_path: str): 
    text = extract_text(input_path) 
    entities = extract_entities(text) 
    out_file = pathlib.Path("data/processed") / (pathlib.Path(input_path).stem + ".json") 
    out_file.write_text(json.dumps(entities, indent=2)) 
    print(f"[ ✓ ] Saved structured output to {out_file}") 
    if __name__ == "__main__": 
        parser = argparse.ArgumentParser() 
        parser.add_argument("--input", required=True, help="Path to PDF/image document") 
        args = parser.parse_args() 
        run_pipeline(args.input)