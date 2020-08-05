
import json
import os
import subprocess
import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

cherry_pick_cmd = " && git cherry-pick FETCH_HEAD"
str1 = "git fetch ssh://review-android.quicinc.com:29418/platform/hardware/qcom/camx refs/changes/"

for gerrit in arguments:
	git_query = "ssh -p 29418 review-android.quicinc.com gerrit query --format=JSON branch:kona-release  change:" + gerrit +"  --current-patch-set"
	git_querry_result = subprocess.check_output(git_query,shell = True).split('\n')
	y  = json.loads(git_querry_result[0])
	gerrit_number = int ((y['number']))
	patch_number = (y["currentPatchSet"]["number"])
	last2digits = gerrit_number % 100
	if last2digits<10:
		last2digits = "0" + str(last2digits)
	final_cherrypick_cmd = str1 + str(last2digits) + "/" + (y['number']) + "/" + patch_number + cherry_pick_cmd
	os.system(final_cherrypick_cmd)
	


