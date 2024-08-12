import mimetypes
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

def validate_image_or_video(file):
    """Validator for both image and video files"""
    mime_type, _ = mimetypes.guess_type(file.name)
    if not mime_type:
        raise ValidationError("File type could not be determined.")

    if mime_type.startswith('image/'):
        # Validate image file
        try:
            width, height = get_image_dimensions(file)
            if width > 5000 or height > 5000:
                raise ValidationError("Image dimensions exceed the maximum allowed size.")
        except Exception as e:
            raise ValidationError(f"Image validation error: {str(e)}")
    elif mime_type.startswith('video/'):
        # Validate video file
        max_size = 50 * 1024 * 1024  # 50MB
        if file.size > max_size:
            raise ValidationError("Video file size exceeds the maximum allowed size of 50MB.")
    else:
        raise ValidationError("File is not a valid image or video.")
