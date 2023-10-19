# PSD to Backblaze Uploader

A simple Python script to automatically upload Photoshop (.psd) files from a specified folder to a Backblaze B2 bucket, with a set content-type of `image/vnd.adobe.photoshop`.

## Prerequisites

- Backblaze account
- Bucket created on Backblaze
- Backblaze `keyId` and `applicationKey`

## Dependencies

Install the required Python library using pip:

```bash
pip install b2sdk


Usage
Clone this repository to your local machine.
Navigate to the repository folder.
Replace your_key_id, your_application_key, and your_bucket_name in upload_psd.py with your Backblaze credentials and bucket name.
Place the upload_psd.py script in the same folder as the PSD files you want to upload.
Run the script:
bash
Copy code
python upload_psd.py
Your PSD files will be uploaded to the specified Backblaze B2 bucket with the content-type set to image/vnd.adobe.photoshop.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT




