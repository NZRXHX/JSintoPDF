import sys
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import DictionaryObject, NameObject, createStringObject

def embed_js(input_pdf_path, js_code, output_pdf_path):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Copy all pages
    for page in reader.pages:
        writer.add_page(page)

    # Create JS action dictionary
    js_action = DictionaryObject()
    js_action.update({
        NameObject("/S"): NameObject("/JavaScript"),
        NameObject("/JS"): createStringObject(js_code),
    })

    # Add JS action as indirect object
    js_action_ref = writer._add_object(js_action)

    # Copy original root catalog dictionary keys to writer's root object
    orig_root = reader.trailer["/Root"]
    for key, value in orig_root.items():
        if key not in writer._root_object:
            writer._root_object[NameObject(key)] = value

    # Set OpenAction to JS action
    writer._root_object[NameObject("/OpenAction")] = js_action_ref

    # Write output PDF
    with open(output_pdf_path, "wb") as out_file:
        writer.write(out_file)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python embed_js.py input.pdf script.js output.pdf")
        sys.exit(1)

    input_pdf = sys.argv[1]
    js_file = sys.argv[2]
    output_pdf = sys.argv[3]

    with open(js_file, "r", encoding="utf-8") as f:
        js_code = f.read()

    embed_js(input_pdf, js_code, output_pdf)
    print(f"JavaScript embedded into {output_pdf}")
