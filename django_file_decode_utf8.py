import chardet
from django.core.files.base import File as F

def conversion_utf8(content_raw):
    encoding = chardet.detect(content_raw)['encoding'] or 'utf8'
    content_utf8 = content_raw.decode(encoding, 'ignore').encode('utf8', 'ignore')
    return content_utf8


def file_conversion_utf8(file):
    uploaded_file = F(file)
    if hasattr(uploaded_file.file.file, 'getvalue'):
        content_raw = uploaded_file.file.file.getvalue()
    else:
        content_raw = uploaded_file.read()
    content_utf8 = conversion_utf8(content_raw)
    f = uploaded_file.open(mode="wb")
    f.write(content_utf8)
    return f

if __name__ == "__main__":
    def validate(self, attrs):
        file = attrs['file']
        attrs.update({"file": file_conversion_utf8(file)})
        return attrs