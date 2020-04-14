'''
Created on Dec 1, 2017
@author: Guanliang Chen
'''

import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")


from functions import save_file, gather_topic_hierarchy
import urllib, json, os, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def download_exercise_from_khan(path):
    exercise_link_map = json.loads(open(path + "all_exercise_links", "r").read())
    print("There is a total of %d exercise links." % len(exercise_link_map))
    
    # Collected exercises
    collected_exercises= set()
    if not os.path.isdir(path + "exercises/"):
        os.mkdir(path + "exercises/")         
    collected_files = os.listdir(path + "exercises/")
    for collected_file in collected_files:
        if collected_file not in [".DS_Store"]:
            collected_exercises.add(collected_file)
    print("There are %d  exercises have been collected." % len(collected_exercises))
    
    # Collect exercise exercises
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    
    for exercise_id in exercise_link_map.keys(): 
        if exercise_id not in collected_exercises:
            driver.get(exercise_link_map[exercise_id]["ka_url"])
            time.sleep(2)          
            try:                
                exercise = driver.find_element_by_xpath("//div[@class='perseus-renderer perseus-renderer-responsive']").text        
                if exercise != "":
                    outFile = open(path + "exercises/" + exercise_id, "w")
                    outFile.write(exercise)
                    outFile.close()                
                    collected_exercises.add(exercise_id)                    
            except:
                continue
                print('e',e)
            time.sleep(1)
                

def gather_exercise_ids(path):
    topic_hierarchy = gather_topic_hierarchy(path)
    component_topic_relation = {}
    for topic in topic_hierarchy.keys():
        for component in topic_hierarchy[topic]:
            component_topic_relation[component] = topic
    # print("component_topic_relationcomponent_topic_relation", component_topic_relation)
    exercise_map = {}
    topic_files = os.listdir(path + "topics/")
    for topic_file in topic_files:
         
        if topic_file != ".DS_Store":
            jsonObject = json.loads(open(path + "topics/" + topic_file, "r").read())
            for tuple in jsonObject["children"]:
                if tuple["kind"] == "Exercise":
                    exercise_map[tuple["internal_id"]] = {"ka_url":tuple["url"],"component_name":topic_file.split("~")[-1], "topic_category":component_topic_relation[topic_file.split("~")[-1]]}
                    
    print("There is a total of %d exercises." % len(exercise_map))
    save_file(exercise_map, path + "all_exercise_links")



######################################################################    
def main():
    data_path = '/home/venktesh/iiit-journey-books-papers/phd-research/LearningQ/data/khan_crawled_data/'
    
    # Step 1: gather exercise list
    gather_exercise_ids(data_path)
    
    # Step 2: download exercises
    download_exercise_from_khan(data_path)
    


            
if __name__ == "__main__":
    main()
    print("Done.")