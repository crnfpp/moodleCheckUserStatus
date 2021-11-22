import json
import requests

courseIDs = ["__","__","__"] # e.g. courseIDs = ["35","56","5"]
mooToken = "_____" # create a token ___admin/settings.php?section=webservicetokens
mooRoot = "__your_Moodle_root__/webservice/rest/server.php?"

class checkUsersStatus():

    def getCourseCompletionStatus(courseID,userID):
            mooFn ="core_completion_get_course_completion_status"
            url = mooRoot+"wstoken="+mooToken+"&wsfunction="+mooFn+"&courseid="+courseID+"&moodlewsrestformat=json&userid="+userID
            r = requests.get(url).json()
            #print(r)
            if r["completionstatus"]["completed"] == True:
                print(f"The user {userID} completed the course")
                return True
            else:
                print("Course not completed")
                return False

    
    def checkUsersInCourse(courseIDs):
         for courseID in courseIDs:
            mooFn ="core_enrol_get_enrolled_users"
            url = mooRoot+"wstoken="+mooToken+"&wsfunction="+mooFn+"&courseid="+courseID+"&moodlewsrestformat=json"
            # Only look for email and id of the user
            f = {"options[0][name]":"userfields","options[0][value]":"email,id"}
            r = requests.get(url,params=f).json()
            # r is the list of users enrolled in a specific course
            for singleUser in r:        
                if checkUsersStatus.getCourseCompletionStatus(courseID,str(singleUser["id"])) == True: 
                    m = {"course":courseID,"id":singleUser["id"],"email":singleUser["email"]}
                    print("User datas: ",m)
                    
checkUsersStatus.checkUsersInCourse(courseIDs)
