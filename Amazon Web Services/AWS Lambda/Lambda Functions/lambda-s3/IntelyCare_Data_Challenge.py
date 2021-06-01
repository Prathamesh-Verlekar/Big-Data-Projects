# Importing necessary packages
import os
import re
from datetime import datetime
import boto3
import pandas
from io import StringIO

# Lambda function to create partitioned bucket
def lambda_handler(event, context):
    # Connect to S3
    s3 = boto3.resource('s3')

    # Giving the source directory
    src_directory = 'sadpartitions/'

    # Defining the file prefix
    file_prefix = 'shift_requests'

    # Destination directory
    dst_directory = 'happypartitions/'

    # Source bucket
    bucket = 'intelycare'

    # Destination bucket
    bucket_dest = 'intelycarefinal'

    # Regex for file date
    file_date = r'\d{4}_\d{2}_\d{2}'
    date_format = '%Y_%m_%d'

    # For loop for all the objects in the source directory
    for obj in s3.Bucket(bucket).objects.filter(Prefix=src_directory + file_prefix):
        # Storing the object key
        tmp_file = obj.key
        print(tmp_file)

        # Try block to handle any file which is not in desired format
        try:
            # Finding the date in the filename
            match = re.search(file_date, tmp_file)
            date = datetime.strptime(match.group(), date_format).date()
            copy_source = {
                'Bucket': bucket,
                'Key': tmp_file
            }

            # Reading the object
            body = obj.get()['Body'].read()
            print(body)

            # Creating a dataframe by reading the json file
            df = pandas.read_json(body)

            # Converting the UNIX Timestamp to datetime format
            df['shift_datetime'] = pandas.to_datetime(df['shift_datetime'], unit='ms')
            df['date_created'] = pandas.to_datetime(df['date_created'], unit='ms')

            # Creating a buffer to convert the dataframe into csv
            csv_buffer = StringIO()
            df.to_csv(csv_buffer)

            # Moving the converted csv to destination bucket which is partitioned based on date
            s3.Object(bucket_dest, dst_directory + 'Year=' + str(date.year) + '/' + 'Month=' + str(date.month) + '/' + 'Day=' + str(
                date.day) + '/' + os.path.basename(os.path.splitext(tmp_file)[0]) + '.csv').put(
                Body=csv_buffer.getvalue())

            # Copying the object from source to an archived folder
            s3.meta.client.copy(copy_source, bucket, 'archived' + '/' + os.path.basename(tmp_file))

            # Deleting the object from source directory
            s3.Object(bucket, tmp_file).delete()
            print('Moved')
            return 200

        # Exception block to handle error data objects
        except Exception as err:
            # Copy the error file to error directory
            s3.meta.client.copy(copy_source, bucket, 'error' + '/' + os.path.basename(tmp_file))

            # Deleting the object from source directory
            s3.Object(bucket, tmp_file).delete()
            print("Error -" + str(err))