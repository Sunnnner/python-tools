from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def compress_image(photo):
    if int(photo.size)/1024 > 2024:
        image_temporary = Image.open(photo)
        image_temporary = image_temporary.convert("RGB")
        width_sm =320 / image_temporary.size[0]
        height_sm = 240 / image_temporary.size[1]
        output_io_stream = BytesIO()
        image_temporary = image_temporary.resize((round(image_temporary.size[0] * width_sm), round(image_temporary.size[1] * height_sm)), Image.ANTIALIAS)
        image_temporary.save(output_io_stream, "JPEG")
        output_io_stream.seek(0)
        photo = InMemoryUploadedFile(output_io_stream, 'ImageField', f"{photo.name.split('.')[0]}.{photo.name.split('.')[1]}",
                                     f"image/{photo.name.split('.')[1]}", getsizeof(output_io_stream), None)
    return photo

if __name__ == "__main__":
    def validate(self, attrs):
        attrs['primeval'] = attrs['image']
        attrs.update({'image': compress_image(attrs['image'])})
        return attrs