# import logging

# # directory is passed without lagging '/'
# # example directory = '/data/{system}/'
# # returns tuple: filename, Logger object
# def create_log(datadir, code):
# 	os.system("mkdir -p '{0}/logs'".format(datadir))
# 	now = datetime.utcnow()
# 	log_filename = "{0}/logs/{1}_{2}.log".format(datadir,code,now.strftime("%Y%m%d-%H%M%S"))
# 	logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(message)s')
# 	log = logging.getLogger("ex")
# 	log_string = """
# 	-----
# 	start time: {now} UTC
# 	code: {code}
# 	filename: {log_filename}
# 	-----
# 	""".format(**locals())
# 	logging.info(log_string)
# 	return log_filename, log

# # To log general print statement for information 
# def log_print(log, message):
# 	log.info('\n' + str(message) + '\n')

# # This will print the entire error trace
# # Use it in a try/except clause
# # Example of use:
# # ...
# # except Exception as e:
# 	# log_error(log, "Custom Error Message...")
# 	# raise
# def log_error(log, message):
# 	log.exception('\n' + message + '\n')

# def s3cp(local_file,bucket,remote_file):
# 	client = boto3.client('s3',
# 	    aws_access_key_id = AWS_ACCESS_KEY_ID,
# 	    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
# 	)
# 	client.upload_file(local_file,bucket,remote_file)

# # Prints timestamp and sends log to s3://quandl-lake
# # log_filename 
# def close_log(log,bucket,system,log_filename):
# 	now = datetime.utcnow()
# 	log_print(log, "Close log at {0}".format(now))
# 	run_date = datetime.utcnow().strftime("%Y%m%d")
# 	filename = log_filename.split('/')[-1]
# 	s3cp(log_filename,bucket,'{0}/logs/{1}/{2}'.format(system, run_date, filename))
	
	
def say_hello():
	raise Exception("hello!")

