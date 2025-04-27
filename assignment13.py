import logging

# Configure logging

#logging.basicConfig(
#    filename='app.log',  # Log output will go to app.log
#    level=logging.DEBUG,  # Set initial log level
#    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
#)


logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,  # Only ERROR and above will be logged
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# Write different types of log messages
logging.debug('This is a DEBUG message.')
logging.info('This is an INFO message.')
logging.warning('This is a WARNING message.')
logging.error('This is an ERROR message.')
