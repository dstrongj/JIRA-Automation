from jira import JIRA
from jira.resources import Sprint
import time
from datetime import datetime, timedelta



analytics_jira = JIRA(server="SERVER URL",\
    basic_auth=("USERNAME", "PASSWORD"))

teams = {"DS Sprint":3,
             "DAO Sprint":8
            } 


start_date = (time.strftime("%m/%d"))
date = datetime.strptime(start_date, "%m/%d")
modified_startdate = date + timedelta(days=46)
new_start = datetime.strftime(modified_startdate, "%m/%d")
modified_enddate = modified_startdate + timedelta(days=13)
end_date = datetime.strftime(modified_enddate, "%m/%d")




for the_key, the_value in teams.iteritems():
    a = the_key
    b = the_value
    c = 42
    d = '('+str(new_start)+'-'+str(end_date)+')'
    
    analytics_jira.create_sprint(name = '{0} {1} {2}'.format(a,c,d), board_id = '{0}'.format(b))



print("Success")
