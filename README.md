# Batch Youtube Tag Scraper

## About the Project

This Python script is designed to streamline the process of extracting and analyzing tags from YouTube videos. By providing a list of YouTube URLs as input, the script fetches the tags associated with each video and compiles them into a CSV (Comma Separated Values) file. This simplifies the task of organizing and analyzing video metadata for various purposes such as content categorization, SEO optimization, or research analysis. You have the option to create a simplified CSV file suitable for direct analysis with tools like pandas, or alternatively, you can choose to include an extra column that tallies the frequency of each tag occurrence. This enhancement facilitates quicker data visualization without the need for external processing tools, but makes it not very suitable for these more refined analyses.

## Getting Started

### Prerequisites

Use the following command in your terminal in the project's path:

```pip install -r requirements.txt```

 This will install all the packages and libraries necessary for this script.

## Usage

Executing the script, you will be prompted to answer whether you want the additional column containing the frequency of each term. This is recommended only if you are interested in directly visualizing the data yourself, rather than utilizing as another tool's input.

The output CSV file will be created in the project's path with the name of "Final_output.csv".