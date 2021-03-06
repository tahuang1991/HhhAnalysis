#!/usr/bin/python
import os
import sys


#benchmarks =  ["ttV","Wjet","sT","VV","DY","TT","Data"]
#benchmarks = ["ttV","Wjet","sT","VV","DY","TT","Data","radion","graviton"]
benchmarks = []
for mass in [260, 270, 300, 350, 400, 450, 500, 550, 600, 650, 700, 800, 900, 1000]:
    benchmarks.append("graviton_M%d"%mass)
    benchmarks.append("radion_M%d"%mass)
jobdir = "REFPDFJobs"
totaljobs = 1
os.system("mkdir -p %s" % jobdir)
submitscript = open("submitallREFPDF.sh","w")
submitscript.write("""#!/bin/bash
cd $CMSSW_BASE/src/HhhAnalysis/PlottingTools/
rm -rf HADD/*txt	
	""")


for job in benchmarks:
    for ijob in range(0, totaljobs):
	jobscript = open("{0}/Send_PlotterProducer_{1}_{2}.slrm".format(jobdir, job, ijob), "w")
	jobscript.write("""#!/bin/bash
#SBATCH -J run{jobtype}
#SBATCH -p stakeholder-4g
#SBATCH -n1
#SBATCH --mem-per-cpu=4000
#SBATCH -o batchjobs_{jobtype}-%A-%a.out
#SBATCH -e batchjobs_{jobtype}-%A-%a.err
#SBATCH --ntasks-per-core=1

echo "starting at `date` on `hostname`"
echo "SLURM_JOBID=$SLURM_JOBID"
jobid=$SLURM_JOBID
source ~/.bashrc
. /etc/profile.d/modules.sh
cd $CMSSW_BASE/src/HhhAnalysis/PlottingTools/
python runRefPDF.py -n {njobs} -i {ijob} -jt {jobtype}
echo "job$jobid starts, `date`"
echo "job$jobid is done, `date`"
exit 0""".format(jobtype=job, njobs=totaljobs, ijob=ijob))
	jobscript.close()

	submitscript.write("""
sbatch {0}/Send_PlotterProducer_{1}_{2}.slrm""".format(jobdir, job, ijob))
submitscript.close()
os.system("chmod +x submitallREFPDF.sh")

#python PlotterProducer.py -b HaddNo {jobtype}
os.system("./submitallREFPDF.sh")

