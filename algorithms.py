import os
from PIL import Image


def bytes_to_megabytes(bytes_size):
    """Конвертирует размер из байтов в мегабайты."""
    return bytes_size / (1024 * 1024)


def compress_image(input_path, output_path, quality, output_format, resize_ratio):
    try:
        with Image.open(input_path) as img:
            original_resolution = img.size  # Исходное разрешение
            # Уменьшение разрешения изображения
            if resize_ratio < 1.0:
                new_size = (int(img.width * resize_ratio), int(img.height * resize_ratio))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
            final_resolution = img.size  # Конечное разрешение

            if output_format == "JPEG":
                img.save(output_path, format="JPEG", quality=quality, optimize=True)
            elif output_format == "PNG":
                img = img.convert("P", palette=Image.ADAPTIVE, colors=64)  # Уменьшаем до 64 цветов
                img.save(output_path, format="PNG", optimize=True)
            elif output_format == "WEBP":
                img.save(output_path, format="WEBP", quality=quality)
            else:
                return False, "Неподдерживаемый формат файла."

            # Получаем размер файла до и после сжатия
            original_size = os.path.getsize(input_path)
            compressed_size = os.path.getsize(output_path)

            # Конвертируем размеры в мегабайты
            original_size_mb = bytes_to_megabytes(original_size)
            compressed_size_mb = bytes_to_megabytes(compressed_size)

            # Возвращаем результат
            return True, {
                "original_size_mb": original_size_mb,
                "compressed_size_mb": compressed_size_mb,
                "compression_ratio": ((original_size - compressed_size) / original_size) * 100,
                "original_resolution": original_resolution,
                "final_resolution": final_resolution,
            }
    except Exception as e:
        return False, f"Произошла ошибка: {e}"