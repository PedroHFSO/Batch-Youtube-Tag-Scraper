import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def get_youtube_keywords(video_url):
    try:
        response = requests.get(video_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        keywords_tag = soup.find('meta', {'name': 'keywords'})
        if keywords_tag:
            keywords = keywords_tag['content'].split(',')        
            keywords = [keyword.strip() for keyword in keywords]
            video_title = soup.title.text.replace('- YouTube', '')
            title = (soup.find(id = 'watch7-content')
                     .find('span', {'itemprop': 'author'})
                     .find('link', {'itemprop': 'name'})['content']
            ) + ' - ' + video_title
            return title, keywords
        else:
            print("There are no tags in this URL")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error visiting URL: {e}")
        return None


if __name__ == '__main__':
    output_style = input('Do you want to add the count column to the output? (Y/N)')
    while output_style.lower() != 'y' and output_style.lower() != 'yes' and output_style.lower() != 'n' and output_style.lower() != 'no':
        output_style = input('Do you want to add the count column to the output? (Y/N)')
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    f = open(file_path)
    df_list = []
    for yt_url in f:
        title, keywords = get_youtube_keywords(yt_url)
        df = pd.DataFrame({title: keywords})
        df_list.append(df)
    df = pd.concat(df_list, axis = 1)
    if output_style == 'y' or output_style == 'yes':
        total_df_list = list(map(lambda x: x.rename(columns={x.columns[0]: "Everything"}),  df_list))
        total_df = pd.concat(total_df_list)
        total_df['Count'] = total_df['Everything'].map(total_df['Everything'].value_counts())
        df_final = pd.concat([df, total_df.reset_index(drop = True)], axis = 1)
    else:
        df_final = df
    print('Gathering the tags. Please wait...')
    df_final.to_csv("Final_output.csv", index = False)
    