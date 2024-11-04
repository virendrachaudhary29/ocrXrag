# ocr_app/views.py

from django.shortcuts import render
from .utils import handle_uploaded_file, clean_up_file, extract_text_with_easyocr


def upload_pdf_view(request):
    if request.method == "POST":
        pdf_file = request.FILES.get("pdf_file")

        if not pdf_file:
            return render(
                request, "upload_pdf.html", {"error": "Please upload a PDF file."}
            )

        try:
            # Save the uploaded file
            file_path = handle_uploaded_file(pdf_file)

            # Extract text using EasyOCR
            extracted_text = extract_text_with_easyocr(file_path)
        except Exception as e:
            extracted_text = f"An error occurred: {str(e)}"
        finally:
            # Clean up the uploaded file
            clean_up_file(file_path)

        return render(request, "result.html", {"extracted_text": extracted_text})

    return render(request, "upload_pdf.html")
