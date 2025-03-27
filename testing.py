import boto3

s3_client = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin"
)

s3_client.download_file("mlops-hotel-reservation-system", "Hotel_Reservations.csv", "raw.csv")
