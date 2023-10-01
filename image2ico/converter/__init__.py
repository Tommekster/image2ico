from pathlib import Path
from PIL import Image

DEFAULT_ICON_SIZES = [
    (16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)
]


def convert(input_image: Path, output: Path, icon_sizes: list[tuple[int, int]] = DEFAULT_ICON_SIZES) -> None:
    img = Image.open(input_image)
    img.save(output, sizes=icon_sizes)
