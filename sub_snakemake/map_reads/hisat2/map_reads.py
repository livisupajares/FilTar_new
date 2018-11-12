import sys
import os

print(snakemake.params[0])
print(snakemake.input[0])

if len(snakemake.input) == 2:
	print('single_end')
	os.system('hisat2 -x {} -U {} -S {} {}'.format(snakemake.input['index'],snakemake.input['reads'],snakemake.output,snakemake.params[0]))
else:
	print('paired_end')
	os.system('hisat2 -x {} -1 {} -2 {} -S {} {}'.format(snakemake.input['index'],snakemake.input['reads'][0], snakemake.input['reads'][1], snakemake.output, snakemake.params[0]))
