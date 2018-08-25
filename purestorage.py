import purestorage
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()


#   Enter IP of the Pure Storage server
storage_ip = "127.0.0.1"

#   Enter Credentials
username = "pureuser"
password = "passwd"

volname = "volname"

#   Login
array = purestorage.FlashArray(storage_ip,username,password)

#   List of all volumes
all_volumes = array.list_volumes(snap=False)

#   Volume details
vol_details = array.get_volume(volname)

#   Volume Protection Group details
vol_pgroup_details = array.get_volume(volname,protect=True)

#   Create Snapshot
##   Suffix is an optional parameter
snap = array.create_snapshot(volname,suffix="suffix")

#   Delete Snapshot
delete_vol = array.destroy_volume(volname)

#   Recover deleted volume
recover_vol = array.recover_vol(volname)

#   Eradicate Volume
##  Note: Eradicated volumes cannot be recovered
eradicate_vol = array.eradicate_volume(volname)

#   Rename volume
rename_vol = array.rename_vol(volname)

#   Create volume
create_vol = array.create_volume(volume,"1G")

#   Clone a snapshot
clone_snap = array.copy_volume("snapname","new_volname")

#   Clone volume
clone_vol = array.copy_volume("source_volname","dest_volname")

pgroupname = "pgroupname"

#   List protection groups
all_pgroups = array.list_pgroups(pgroupname)

#   Protection group details
pgroup_details = array.get_pgroup(pgroupname)

#   Schedule details of Protection Group
schedule_details = array.get_pgroup(pgroupname,schedule=True)

#   Retention details of Protection Group
retention_details = array.get_pgroup(pgroupname,retention=True)
