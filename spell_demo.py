#!/usr/bin/env python
import sys
sys.path.append('../')
import Spell

input_dir  = ''  # The input directory of log file
output_dir = 'Spell_result/'  # The output directory of parsing results
log_file   = 'test_log.csv'  # The input log file name
log_format = '<Date> <Time> <sudo>: <User> : <TTY> ; <PWD> ; <User_type> ; <Command>'  # HDFS log format
tau        = 0.8  # Message type threshold (default: 0.5)
regex      = []  # Regular expression list for optional preprocessing (default: [])

parser = Spell.LogParser(indir=input_dir, outdir=output_dir, log_format=log_format, tau=tau, rex=regex)
parser.parse(log_file)