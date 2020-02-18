#Function 1
import pandas as pd
import numpy as np

ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.head()

twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

#Function 2
### START FUNCTION
def dictionary_of_metrics(items):
    # your code here
    """ The function calculates the mean, median, variance, 
    standad deviation, maximum and minimum list of items. 
    All values are returned in a dictionary """ 
    
    #Calculating the required metrics.
    mean = np.mean(items) 
    variance = sum([(xi - mean)**2 for xi in items]) / (len(items) -1) 
    std = sum([(i - mean)**2 for i in items]) / (len(items) -1)  
    minimum = min(items)
    maximum = max(items) 
    median = np.median(items)  
   
    return{'mean': round(mean,2),
           'median':median,
           'var':round(variance,2),
           'std':round((std) ** (1/2),2),
           'min': minimum,
           'max':maximum}   #returning calculated metrics in a dictionary.
### END FUNCTION

#Function 3
### START FUNCTION
def five_num_summary(items):
    # your code here
    """ The funcion takes in a list of intergers and returns
    a dictionary of the five number summary. 
    All numerical values are rounded to two decimal places."""
    
    #Calclating the five number summary. 
    minimum = min(items)
    maximum = max(items)
    median = np.median(items)
    q1 = np.percentile(items,25)
    q3 = np.percentile(items,75)   
    
    return {'max':maximum,
           'median':median,
           'min': minimum,
           'q1': q1,
           'q3': q3,} #returning the calculated five number summary in a dictionary.
### END FUNCTION

#Function 3
### START FUNCTION
def date_parser(dates):
    # your code here
    """ The function takes a list of datetime strings and 
    returns only the date in the format 'yyyy-mm-dd' """
    
    x = [i.split(" ") for i in dates] # seperate the date and timpestamp with a whitespace.
    return [y[0] for y in x] # return only the first element (date) in the list.
### END FUNCTION

#Function 4
### START FUNCTION
def extract_municipality_hashtags(df):
    # your code here
    """ The function takes in a pandas dataframe as input and returns a 
    new dataframe that includes two new columns that have information 
    about the municipality and hashtag of the tweet """
    
    muni = list(mun_dict.keys()) #construct a list from the municipality twitter handles.
    df1 = df.copy() 
    cities = []
    hashtags = [] 
    
    Tweets = list(df1['Tweets']) #construct a list of tweets from the 'Tweets' column
    Tweets_Split = [] 
    for Tweet in Tweets: 
        Tweets_Split.append(Tweet.lower().split()) # add a new tweet iteratively at the end of the list
    
    #extracting a list of hashtags from a tweet into a new column named 'hashtags'
    for tweet in Tweets_Split: 
        city1 = '' 
        hashs = [] 
        for words in tweet: 
            if words in muni:  
                city1 = str(mun_dict[words]) 
            if '#' in words: 
                words = words.lower() 
                hashs.append(words) 
        cities.append(city1) 
        hashtags.append(hashs) 
    
    cities = [np.nan if x == '' else x for x in cities] 
    df1['municipality'] = cities 
    df1['hashtags'] = hashtags 
    df1['hashtags'] = df1['hashtags'].apply(lambda y: np.nan if len(y)==0 else y) 
    
    
    return df1
### END FUNCTION

#Function 5
### START FUNCTION
def number_of_tweets_per_day(df):
    # your code here
    """ The function calculates the number of tweets that were posted 
    on each date in the dataframe. It returns a new dataframe, grouped 
    by day with the number of tweets for that day. """
    
    df1=df.copy()
    dates=list(df1['Date'])#construct list from date column
    dates_only=[]
    #add dates iteratively in list
    for date in dates :
        temp=date[0:10]
        dates_only.append(temp)
    #return a new dataframe, grouped by day    
    data=pd.DataFrame()
    data['Date']=dates_only
    data['Tweets']=1
    data=data.groupby(['Date']).sum() #sum all tweets in the dataframe for that date entry
    return data

### END FUNCTION

#Function 6
### START FUNCTION
def word_splitter(df):
    # your code here
    """ The function takes ina pandas dataframe as input and it splits the sentences in 
    the dataframe's column into a list of seperate words. The created list is then placed
    in a column named 'Split Tweets' """
    
    df["Split_Tweets"] = df.apply(lambda column: column.Tweets.lower().split(), axis=1) #split the sentences into separate words
    return df #return column named 'Split Tweets'
### END FUNCTION

#Function 7
### START FUNCTION
def stop_words_remover(df):
    # your code here
    """ The function takes ina pandas dataframe as input and removes english stop words from a tweet."""
    
    twitter_df= {
        'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}
    Tweets_new = []  
    Tweets = list(df['Tweets'])
    Tweets_Split = [] 
    #remove stop words
    for Tweet in Tweets: 
        Tweets_Split.append(Tweet.lower().split()) 
        for Tweets in Tweets_Split: 
            x = Tweets
            for item in x: 
                if item in stop_words_dict['stopwords']: 
                    x.remove(item) 
        Tweets_new.append(x)      
    df['Without Stop Words'] = Tweets_new 
    return df
### END FUNCTION
