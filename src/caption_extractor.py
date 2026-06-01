import fitz
import re


class CaptionExtractor:

    def __init__(self):

        self.patterns = [
            r"Figure\s+\d+[:.]?\s*.*",
            r"FIGURE\s+\d+[:.]?\s*.*",
            r"Fig\.\s*\d+[:.]?\s*.*",
        ]

    def extract_captions(self, pdf_path):

        pdf = fitz.open(pdf_path)

        captions = []

        for page_num in range(len(pdf)):

            page = pdf[page_num]

            text = page.get_text()

            lines = text.split("\n")

            for i, line in enumerate(lines):

                line = line.strip()

                for pattern in self.patterns:

                    if re.match(pattern, line, re.IGNORECASE):

                        caption = line

                        j = i + 1

                        max_caption_lines = 2
                        lines_added = 0

                        while (
                            j < len(lines)
                            and lines_added < max_caption_lines
                        ):

                            next_line = lines[j].strip()

                            if not next_line:
                                break

                            if re.match(
                                r"(Figure|FIGURE|Fig\.)\s+\d+",
                                next_line,
                                re.IGNORECASE
                            ):
                                break

                            caption += " " + next_line

                            lines_added += 1
                            j += 1

                        captions.append(
                            {
                                "page": page_num + 1,
                                "caption": caption
                            }
                        )

                        break

        pdf.close()

        return captions