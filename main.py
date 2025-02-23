import fitz  # PyMuPDF

def split_pdf_by_chapters(input_pdf_path):
    # Open the source PDF
    doc = fitz.open(input_pdf_path)

    # Access the table of contents (TOC)
    toc = doc.get_toc(simple=False)

    chapter_counter = 1

    # Loop through each entry in the TOC
    for index, entry in enumerate(toc):
        title, level, page_num = entry[1], entry[0], entry[2]

        print(f"Title: {title}, Level: {level}, Page: {page_num}")
        
        if title == "Preface":
            # Determine the start and end pages for the current chapter
            start_page = page_num -1

            end_page = toc[index + 2][2] - 1

            # Create a new PDF document for the chapter
            chapter_doc = fitz.open()

            chapter_doc.insert_pdf(doc, from_page=0, to_page=0)

            # Add pages from the source PDF to the new chapter PDF
            for page in range(start_page, end_page):
                chapter_doc.insert_pdf(doc, from_page=page, to_page=page)

            # Save the chapter PDF
            chapter_pdf_path = f"./chapters/CausalML_preface.pdf"
            chapter_doc.save(chapter_pdf_path)
            chapter_doc.close()
        elif "Sneak Peek:" in title:
            # Determine the start and end pages for the current chapter
            start_page = page_num -1

            end_page = toc[index + 2][2] - 2

            # Create a new PDF document for the chapter
            chapter_doc = fitz.open()
            chapter_doc.insert_pdf(doc, from_page=0, to_page=0)

            # Add pages from the source PDF to the new chapter PDF
            for page in range(start_page, end_page):
                chapter_doc.insert_pdf(doc, from_page=page, to_page=page)

            # Save the chapter PDF
            chapter_pdf_path = f"./chapters/CausalML_chap_0.pdf"
            chapter_doc.save(chapter_pdf_path)
            chapter_doc.close()
        elif level == 2:
            # Determine the start and end pages for the current chapter
            start_page = page_num -1

            index_end = index

            if chapter_counter == 18:
                end_page = len(doc) - 2
            else:
                while toc[index_end + 1][0] != 2:
                    index_end += 1

                end_page = toc[index_end + 2][2] - 2 

            # Create a new PDF document for the chapter
            chapter_doc = fitz.open()
            chapter_doc.insert_pdf(doc, from_page=0, to_page=0)

            # Add pages from the source PDF to the new chapter PDF
            for page in range(start_page, end_page):
                chapter_doc.insert_pdf(doc, from_page=page, to_page=page)

            # Save the chapter PDF
            chapter_pdf_path = f"./chapters/CausalML_chap_{chapter_counter}.pdf"
            chapter_doc.save(chapter_pdf_path)
            chapter_doc.close()

            chapter_counter += 1


    # Close the source document
    doc.close()

# Example usage
input_pdf_path = './CausalML_book.pdf'
split_pdf_by_chapters(input_pdf_path)