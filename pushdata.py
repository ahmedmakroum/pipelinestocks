from google.cloud import storage

# GCP Bucket and File Info
bucket_name = 'financedata2'  # Updated bucket name
csv_file_path = 'stocks.csv'
destination_blob_name = 'stocks.csv'  # Name of the file in the bucket

# Initialize GCP client
client = storage.Client()
bucket = client.get_bucket(bucket_name)

# Upload the file
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(csv_file_path)

print(f"File {csv_file_path} uploaded to {bucket_name}/{destination_blob_name}.")

