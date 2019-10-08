import logging
import boto3
from botocore.exceptions import ClientError


def send_sqs_message(sqs_queue_url, msg_body):

    # Send the SQS message
    sqs_client = boto3.client('sqs', region_name='us-east-1')
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=msg_body)
    except ClientError as e:
        logging.error(e)
        return None
    return msg


def send(m, url):
    """Exercise send_sqs_message()"""

    # Assign this value before running the program
    #sqs_queue_url = 'https://sqs.us-east-1.amazonaws.com/432566563479/kiss'
    sqs_queue_url = url
    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')


    # Send some SQS messages
    msg_body = m
    msg = send_sqs_message(sqs_queue_url, msg_body)
    if msg is not None:
        logging.info(f'Sent SQS message ID: {msg["MessageId"]}')
