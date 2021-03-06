import pandas as pd
import os
import json
import re

def get_transcripts(path):
    domain = list()
    subject = list()
    topic = list()
    concept = list()
    rough_objectives = list()
    video_link_map = json.loads(open(path + "all_video_links", "r").read())
    article_link_map = json.loads(open(path + "all_article_links", "r").read())
    exercise_link_map = json.loads(open(path + "all_exercise_links", "r").read())
    files = os.listdir(path  + "topics")
    transcripts = list()
    articles = list()
    exercises = list()
    video_transcripts = os.listdir(path + "topic_videos")
    transcript_list = os.listdir(path + "transcripts")
    article_list = os.listdir(path + "articles")
    exercises_list = os.listdir(path + "exercises")
    for file in files:
        split_list = file.split("~")
        # if len(split_list )> 3:
        #     domain.append(split_list[1])
        #     subject.append(split_list[2])
        #     topic.append(split_list[3])
        #     if len(split_list) >4 :
        #         concept.append(split_list[4])
        json_object = json.loads(open(path + "topics/" + file, "r").read())
        rough_objectives.append(json_object['description'])
        transcript = ''
        article= ''
        exercise = ''
            # for youtube_id in video_link_map.keys():
                # if(file.split("~")[2] == 'math'):
                    # print(file.split("~")[2])
                    # if video_link_map[youtube_id]["component_name"] == file.split("~")[-1] and youtube_id in transcript_list:
                    #     transcript = open(path + "transcripts/" + youtube_id, "r").read()
                    #     transcript = re.sub('\d+:\d+\d+', ' ',transcript)
                    #     transcripts.append(transcript)
        for  exercise_id in exercise_link_map.keys():

                if exercise_link_map[exercise_id]["component_name"] == file.split("~")[-1] and exercise_id in exercises_list:
                    if len(split_list )> 3:
                        domain.append(split_list[1])
                        subject.append(split_list[2])
                        topic.append(split_list[3])
                    if len(split_list) >4 :
                        concept.append(split_list[4])
                    exercise = open(path + "exercises/" + exercise_id, "r").read()
                    exercises.append(exercise)
            # exercises.append(exercise)
            # for article_id in article_link_map.keys():
            #     if article_link_map[article_id]["component_name"] == file.split("~")[-1] and article_id in article_list:
            #         article = json.loads(open(path + "articles/" + article_id, "r").read())
            #         if isinstance(json.loads(article["translated_perseus_content"]), list):
            #             article = json.loads(article["translated_perseus_content"])[0]["content"]
            #         else:
            #             article = ""
            # articles.append(article)
    # print(transcripts[0])
    # print(len(transcripts))
    # video_transcripts = ('\n').join(transcripts)

    # with open('exercises', 'w') as output_file:
    #     output_file.write(video_transcripts)
    # data_dict ={'subject':domain, 'chapter': subject, 'topic': topic, "core_objectives": rough_objectives, 'video_transcripts':transcripts, 'articles':articles, 'exercises':exercises}
    # dataframe =  pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in data_dict.items() ]))
    # print(dataframe)
    # dataframe.to_csv('initial_research_data.csv', index=False)

    data_dict ={'subject':domain, 'chapter': subject, 'topic': topic,'exercises':exercises}
    dataframe =  pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in data_dict.items() ]))
    print(dataframe)
    dataframe.to_csv('exercises-complete.csv', index=False)
def main():
    data_path = '/home/venktesh/iiit-journey-books-papers/phd-research/LearningQ/data/khan_crawled_data/'
    get_transcripts(data_path)


if __name__ == "__main__":
    main()