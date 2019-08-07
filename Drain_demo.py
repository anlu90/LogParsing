#!/usr/bin/env python
import sys
sys.path.append('../')
import Drain

input_dir  = ''  # The input directory of log file
output_dir = 'Drain_result/'  # The output directory of parsing results
log_file   = 'test_log.csv'  # The input log file name
log_format = '<Month> <Date> <Time> <sudo>: <User> : <TTY> ; <PWD> ; <User_type> ; <Command>'  # HDFS log format
# Regular expression list for optional preprocessing (default: [])
regex      = [
    r'blk_(|-)[0-9]+' , # block id
    r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', # IP
    r'(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$', # Numbers
]
st         = 0.8  # Similarity threshold
depth      = 5  # Depth of all leaf nodes

parser = Drain.LogParser(log_format, indir=input_dir, outdir=output_dir,  depth=depth, st=st, rex=regex)
parser.parse(log_file)

