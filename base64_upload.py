"""将本地图片文件编码为 Base64 字符串。"""

import base64
from pathlib import Path


def upload_picture(image_path: str | Path) -> str:
    """读取一张图片的绝对路径，并返回其 Base64 编码字符串。

    Args:
        image_path: 图片文件的绝对路径。

    Returns:
        不含 ``data:image/...;base64,`` 前缀的 Base64 字符串。

    Raises:
        ValueError: 路径不是绝对路径，或目标不是文件。
        FileNotFoundError: 图片路径不存在。
    """
    path = Path(image_path)
    if not path.is_absolute():
        raise ValueError("请传入图片的绝对路径")
    if not path.exists():
        raise FileNotFoundError(f"图片不存在: {path}")
    if not path.is_file():
        raise ValueError(f"路径不是文件: {path}")

    return base64.b64encode(path.read_bytes()).decode("utf-8")
