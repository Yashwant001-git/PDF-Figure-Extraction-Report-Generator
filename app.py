# from src.image_extractor import ImageExtractor


# PDF_PATH = "data/uploads/Development_of_High-Current_Solid-State_Power_Cont.pdf"


# def main():

#     extractor = ImageExtractor()

#     extracted_images = extractor.extract_images(PDF_PATH)

#     print("\n" + "=" * 50)
#     print("EXTRACTION COMPLETE")
#     print("=" * 50)

#     print(f"\nTotal Images Extracted: {len(extracted_images)}\n")

#     for image in extracted_images:

#         print(
#             f"Page: {image['page']} | "
#             f"File: {image['image_name']}"
#         )


# if __name__ == "__main__":
#     main()



from src.image_extractor import ImageExtractor
from src.caption_extractor import CaptionExtractor
from src.figure_matcher import FigureMatcher
from src.report_generator import ReportGenerator


PDF_PATH = "data/uploads/Majorproject_Phase 3 _1RV24EPE01.pdf"


def main():

    extractor = ImageExtractor()

    images = extractor.extract_images(PDF_PATH)

    print("\n" + "=" * 50)

    print(f"Total Images Extracted: {len(images)}")

    print("=" * 50)

    for image in images:

        print(
            f"Page: {image['page']} | "
            f"Type: {image['type']} | "
            f"File: {image['image_name']}"
        )


if __name__ == "__main__":
    main()