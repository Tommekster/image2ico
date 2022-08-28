from PIL import Image

DEFAULT_ICON_SIZES = [(16, 16), (24, 24), (32, 32),
                      (48, 48), (64, 64), (128, 128), (255, 255)]


def convert(image_path: str, output_path: str, icon_sizes: list[tuple[int, int]] = DEFAULT_ICON_SIZES) -> None:
    with open(image_path, "rb") as f:
        img = Image.open(f)
        img.save(output_path, sizes=icon_sizes)
