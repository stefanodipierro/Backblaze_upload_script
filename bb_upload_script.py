import os
from b2sdk.v1 import InMemoryAccountInfo
from b2sdk.v1 import B2Api

# Set up Backblaze credentials
key_id = 'your_key_id'
application_key = 'your_application_key'
bucket_name = 'your_bucket_name'

# Initialize B2 API
info = InMemoryAccountInfo()
b2_api = B2Api(info)
b2_api.authorize_account('production', key_id, application_key)
bucket = b2_api.get_bucket_by_name(bucket_name)

def upload_file(file_path):
    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        bucket.upload_file_contents(
            file_name=file_name,
            contents=f.read(),
            content_type='image/vnd.adobe.photoshop'
        )

if __name__ == '__main__':
    directory = os.path.dirname(os.path.abspath(__file__))
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.psd'):
                file_path = os.path.join(root, file)
                upload_file(file_path)
