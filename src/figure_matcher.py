class FigureMatcher:

    def match(self, images, captions):

        matched_figures = []

        pages = {}

        # Group images by page
        for image in images:

            page = image["page"]

            if page not in pages:
                pages[page] = {
                    "images": [],
                    "captions": []
                }

            pages[page]["images"].append(image)

        # Group captions by page
        for caption in captions:

            page = caption["page"]

            if page not in pages:
                pages[page] = {
                    "images": [],
                    "captions": []
                }

            pages[page]["captions"].append(caption)

        # Match image-caption pairs
        for page, data in pages.items():

            images_list = data["images"]
            captions_list = data["captions"]

            num_matches = min(
                len(images_list),
                len(captions_list)
            )

            for i in range(num_matches):

                matched_figures.append(
                    {
                        "page": page,
                        "image_path": images_list[i]["image_path"],
                        "caption": captions_list[i]["caption"]
                    }
                )

        return matched_figures