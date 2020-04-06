import pandas as pd
import os
import json

def get_topics_and_sub_topics(path):
    domain = list()
    subject = list()
    topic = list()
    concept = list()
    rough_objectives = list()
    video_link_map = json.loads(open(path + "all_video_links", "r").read())

    files = os.listdir(path  + "topics")
    transcripts = list()
    video_transcripts = os.listdir(path + "topic_videos")
    transcript_list = os.listdir(path + "transcripts")
    for file in files:
        split_list = file.split("~")
        if len(split_list )> 3:
            domain.append(split_list[1])
            subject.append(split_list[2])
            topic.append(split_list[3])
            if len(split_list) >4 :
                concept.append(split_list[4])
            json_object = json.loads(open(path + "topics/" + file, "r").read())
            rough_objectives.append(json_object['description'])
            transcript = ''
            for youtube_id in video_link_map.keys():
                if video_link_map[youtube_id]["component_name"] == file.split("~")[-1] and youtube_id in transcript_list:
                     transcript = open(path + "transcripts/" + youtube_id, "r").read()
            transcripts.append(transcript)
    data_dict ={'domain':domain, 'subject': subject, 'topic': topic, "core_objectives": rough_objectives, 'video_transcripts':transcripts}
    dataframe =  pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in data_dict.items() ]))
    print(dataframe.head(100))
    dataframe.to_csv('initial_research_data.csv', index=False)
def main():
    data_path = '/home/venktesh/iiit-journey-books-papers/phd-research/LearningQ/data/khan_crawled_data/'
    get_topics_and_sub_topics(data_path)


if __name__ == "__main__":
    main()