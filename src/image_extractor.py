import fitz
import os


class ImageExtractor:

    def __init__(
        self,
        output_dir="data/figures",
        min_width=100,
        min_height=100
    ):

        self.output_dir = output_dir
        self.min_width = min_width
        self.min_height = min_height

        os.makedirs(self.output_dir, exist_ok=True)

    def extract_images(self, pdf_path):

        pdf = fitz.open(pdf_path)

        extracted_images = []

        for page_num in range(len(pdf)):

            page = pdf[page_num]

            images = page.get_images(full=True)

            print(
                f"Page {page_num + 1}: Found {len(images)} embedded image(s)"
            )

            # --------------------------------------------------
            # CASE 1: Embedded images exist
            # --------------------------------------------------
            if len(images) > 0:

                for img_index, img in enumerate(images):

                    try:

                        xref = img[0]

                        base_image = pdf.extract_image(xref)

                        image_bytes = base_image["image"]
                        image_ext = base_image["ext"]

                        width = base_image["width"]
                        height = base_image["height"]

                        # Skip tiny images
                        if (
                            width < self.min_width
                            or height < self.min_height
                        ):
                            continue

                        image_name = (
                            f"page_{page_num + 1}_img_{img_index + 1}.{image_ext}"
                        )

                        image_path = os.path.join(
                            self.output_dir,
                            image_name
                        )

                        with open(image_path, "wb") as image_file:
                            image_file.write(image_bytes)

                        extracted_images.append(
                            {
                                "page": page_num + 1,
                                "image_name": image_name,
                                "image_path": image_path,
                                "width": width,
                                "height": height,
                                "type": "embedded"
                            }
                        )

                    except Exception as e:

                        print(
                            f"Error extracting image on page "
                            f"{page_num + 1}: {e}"
                        )

            # --------------------------------------------------
            # CASE 2: No embedded images
            # Save entire page as image
            # --------------------------------------------------
            else:

                try:

                    pix = page.get_pixmap(
                        matrix=fitz.Matrix(2, 2)
                    )

                    image_name = (
                        f"page_{page_num + 1}_fullpage.png"
                    )

                    image_path = os.path.join(
                        self.output_dir,
                        image_name
                    )

                    pix.save(image_path)

                    extracted_images.append(
                        {
                            "page": page_num + 1,
                            "image_name": image_name,
                            "image_path": image_path,
                            "width": pix.width,
                            "height": pix.height,
                            "type": "rendered_page"
                        }
                    )

                    print(
                        f"Rendered page {page_num + 1} "
                        f"as image"
                    )

                except Exception as e:

                    print(
                        f"Error rendering page "
                        f"{page_num + 1}: {e}"
                    )

        pdf.close()

        return extracted_images