import pandas as pd
import os
import uuid

if __name__ == '__main__':
    khan_acad_data = pd.read_csv('initial_research_data.csv')
    khan_acad_data = khan_acad_data[khan_acad_data[['video_transcripts']].notnull().all(axis=1)]
    khan_acad_data = khan_acad_data.loc[khan_acad_data['subject']=='science']
    khan_acad_trasncripts = khan_acad_data['video_transcripts']
    khan_acad_transcript_values  = (khan_acad_trasncripts.values)
    if not os.path.isdir("docsutf8/"):
        os.mkdir("docsutf8/")
    for transcript in khan_acad_transcript_values:
        outFile = open("docsutf8/" + "science"+ str(uuid.uuid4())+".txt", "w")
        outFile.write(transcript)
        outFile.close() 