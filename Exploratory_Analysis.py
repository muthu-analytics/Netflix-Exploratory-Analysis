from collections import Counter

import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot
from plotly.offline import plot
import pandas as pd
df = pd.read_csv(r"C:\Users\Muthuvalli\Desktop\Muthuvalli Practise\datasets\netflix_titles_nov_2019.csv")
print(df)

col = "type"
grouped = df[col].value_counts().reset_index()
print(grouped)
#plot
trace = go.Pie(
    labels = grouped[col],
    values = grouped['count'],
    pull= [0.05,0],
    marker = dict(colors =["#6ad49b", "#a678de"])
)
#layout
layout =go.Layout(title="content Type Distribution",height = 400,legend =dict(x=0.1,y=1.1))
#combine & display
fig = go.Figure(data=[trace],layout= layout)
print(plot(fig))
df.columns.str.strip()
print(df.columns)
df['date_added'] = pd.to_datetime(df['date_added'],errors='coerce')
#extrac year and month
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
d1 = df[df["type"] == 'TV Show']
d2 = df[df["type"] == 'Movie']
print(d1,d2)
col1 = "year_added"
vc1 = d1[col1].value_counts().reset_index()
vc1 = vc1.rename(columns = {col:"count","index":col})
vc1['percentage'] = vc1['count'].apply(lambda x:100*x/sum(vc1['count']))
#percent = 100 * count of the year/total count of the year
vc1 = vc1.sort_values(col1)
print(vc1)
vc2 = d2[col1].value_counts().reset_index()
vc2 = vc2.rename(columns = {col:"count","index":col})
vc2['percentage'] = vc2['count'].apply(lambda x:100 * x/sum(vc2['count']))
vc2 = vc2.sort_values(col1)
print(vc2)
#create trace for line plot
trace1 = go.Scatter(x=vc1[col1],y=vc1['count'],name="TV Show",marker=dict(color="#a678de"))
trace2 = go.Scatter(x=vc2[col1],y=vc2['count'],name="Movie",marker=dict(color="#6ad49b"))
data =[trace1,trace2]
#layout
layout = go.Layout(title = "content added over the year",legend = dict(x=0.1,y=1.1, orientation="h"))
#create and show the figure
fig = go.Figure(data,layout=layout)
fig.show()

#3.Release year of the movies and tv shows
d1 = df[df["type"] == 'TV Show']
d2 = df[df["type"] == 'Movie']
col = 'release_year'
vc3 = d1[col].value_counts().reset_index()
vc3['percentage'] = vc3['count'].apply(lambda x: 100*x/sum(vc3['count']))
vc3 = vc3.sort_values(col)
print(vc3)

vc4 = d2[col].value_counts().reset_index()
vc4['percentage'] = vc4['count'].apply(lambda x:100*x/sum(vc3['count']))
vc4 = vc4.sort_values(col)
print(vc4)

trace11 = go.Bar(x=vc3[col],y=vc3['count'],name ="Tv shows", marker=dict(color ="#a678de"))
trace22 = go.Bar(x=vc4[col],y=vc3['count'],name="Movies",marker = dict(color="#6ad49b"))
data = [trace11,trace22]
layout = go.Layout(title = "content added over the release_year",legend = dict(x=0.1,y=1.1,orientation = "h"))
fig = go.Figure(data,layout=layout)
fig.show()

#In which month , the content is added the most?
print(df.columns)
col = 'month_added'
vc5 = d1[col].value_counts().reset_index()
vc5['percentage'] = vc5['count'].apply(lambda x: 100 * x/sum(vc5['count']))
print(vc5)

trace = go.Bar(x=vc5[col],y=vc5['count'],name="Tv Shows",marker = dict(color = "#a678de"))
data = trace
layout = go.Layout(title= "In which month, the content is added the most ?",legend = dict(x=0.1, y=1.1, orientation="h"))
fig = go.Figure(data,layout=layout)
fig.show()

#some of the oldest movies on netflix
small = df.sort_values('release_year',ascending = True)
print(small)
small = small[small['duration'] != ""]

print(small[['title','release_year']][:15])

#Some of the oldest TV Shows on Netflix

df['season_count'] = 1
small1 = df.sort_values('release_year',ascending=True)
small1 = small1[small1['season_count'] != ""]
print(small1[['title','release_year']][:15])

#content from different countries
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot
from plotly.offline import plot
import pandas as pd
from scipy.fftpack import tilbert

df = pd.read_csv(r"C:\Users\Muthuvalli\Desktop\Muthuvalli Practise\datasets\netflix_titles_nov_2019.csv")
print(df)



country_codes = {'afghanistan': 'AFG',
 'albania': 'ALB',
 'algeria': 'DZA',
 'american samoa': 'ASM',
 'andorra': 'AND',
 'angola': 'AGO',
 'anguilla': 'AIA',
 'antigua and barbuda': 'ATG',
 'argentina': 'ARG',
 'armenia': 'ARM',
 'aruba': 'ABW',
 'australia': 'AUS',
 'austria': 'AUT',
 'azerbaijan': 'AZE',
 'bahamas': 'BHM',
 'bahrain': 'BHR',
 'bangladesh': 'BGD',
 'barbados': 'BRB',
 'belarus': 'BLR',
 'belgium': 'BEL',
 'belize': 'BLZ',
 'benin': 'BEN',
 'bermuda': 'BMU',
 'bhutan': 'BTN',
 'bolivia': 'BOL',
 'bosnia and herzegovina': 'BIH',
 'botswana': 'BWA',
 'brazil': 'BRA',
 'british virgin islands': 'VGB',
 'brunei': 'BRN',
 'bulgaria': 'BGR',
 'burkina faso': 'BFA',
 'burma': 'MMR',
 'burundi': 'BDI',
 'cabo verde': 'CPV',
 'cambodia': 'KHM',
 'cameroon': 'CMR',
 'canada': 'CAN',
 'cayman islands': 'CYM',
 'central african republic': 'CAF',
 'chad': 'TCD',
 'chile': 'CHL',
 'china': 'CHN',
 'colombia': 'COL',
 'comoros': 'COM',
 'congo democratic': 'COD',
 'Congo republic': 'COG',
 'cook islands': 'COK',
 'costa rica': 'CRI',
 "cote d'ivoire": 'CIV',
 'croatia': 'HRV',
 'cuba': 'CUB',
 'curacao': 'CUW',
 'cyprus': 'CYP',
 'czech republic': 'CZE',
 'denmark': 'DNK',
 'djibouti': 'DJI',
 'dominica': 'DMA',
 'dominican republic': 'DOM',
 'ecuador': 'ECU',
 'egypt': 'EGY',
 'el salvador': 'SLV',
 'equatorial guinea': 'GNQ',
 'eritrea': 'ERI',
 'estonia': 'EST',
 'ethiopia': 'ETH',
 'falkland islands': 'FLK',
 'faroe islands': 'FRO',
 'fiji': 'FJI',
 'finland': 'FIN',
 'france': 'FRA',
 'french polynesia': 'PYF',
 'gabon': 'GAB',
 'gambia, the': 'GMB',
 'georgia': 'GEO',
 'germany': 'DEU',
 'ghana': 'GHA',
 'gibraltar': 'GIB',
 'greece': 'GRC',
 'greenland': 'GRL',
 'grenada': 'GRD',
 'guam': 'GUM',
 'guatemala': 'GTM',
 'guernsey': 'GGY',
 'guinea-bissau': 'GNB',
 'guinea': 'GIN',
 'guyana': 'GUY',
 'haiti': 'HTI',
 'honduras': 'HND',
 'hong kong': 'HKG',
 'hungary': 'HUN',
 'iceland': 'ISL',
 'india': 'IND',
 'indonesia': 'IDN',
 'iran': 'IRN',
 'iraq': 'IRQ',
 'ireland': 'IRL',
 'isle of man': 'IMN',
 'israel': 'ISR',
 'italy': 'ITA',
 'jamaica': 'JAM',
 'japan': 'JPN',
 'jersey': 'JEY',
 'jordan': 'JOR',
 'kazakhstan': 'KAZ',
 'kenya': 'KEN',
 'kiribati': 'KIR',
 'north korea': 'PRK',
 'south korea': 'KOR',
 'kosovo': 'KSV',
 'kuwait': 'KWT',
 'kyrgyzstan': 'KGZ',
 'laos': 'LAO',
 'latvia': 'LVA',
 'lebanon': 'LBN',
 'lesotho': 'LSO',
 'liberia': 'LBR',
 'libya': 'LBY',
 'liechtenstein': 'LIE',
 'lithuania': 'LTU',
 'luxembourg': 'LUX',
 'macau': 'MAC',
 'macedonia': 'MKD',
 'madagascar': 'MDG',
 'malawi': 'MWI',
 'malaysia': 'MYS',
 'maldives': 'MDV',
 'mali': 'MLI',
 'malta': 'MLT',
 'marshall islands': 'MHL',
 'mauritania': 'MRT',
 'mauritius': 'MUS',
 'mexico': 'MEX',
 'micronesia': 'FSM',
 'moldova': 'MDA',
 'monaco': 'MCO',
 'mongolia': 'MNG',
 'montenegro': 'MNE',
 'morocco': 'MAR',
 'mozambique': 'MOZ',
 'namibia': 'NAM',
 'nepal': 'NPL',
 'netherlands': 'NLD',
 'new caledonia': 'NCL',
 'new zealand': 'NZL',
 'nicaragua': 'NIC',
 'nigeria': 'NGA',
 'niger': 'NER',
 'niue': 'NIU',
 'northern mariana islands': 'MNP',
 'norway': 'NOR',
 'oman': 'OMN',
 'pakistan': 'PAK',
 'palau': 'PLW',
 'panama': 'PAN',
 'papua new guinea': 'PNG',
 'paraguay': 'PRY',
 'peru': 'PER',
 'philippines': 'PHL',
 'poland': 'POL',
 'portugal': 'PRT',
 'puerto rico': 'PRI',
 'qatar': 'QAT',
 'romania': 'ROU',
 'russia': 'RUS',
 'rwanda': 'RWA',
 'saint kitts and nevis': 'KNA',
 'saint lucia': 'LCA',
 'saint martin': 'MAF',
 'saint pierre and miquelon': 'SPM',
 'saint vincent and the grenadines': 'VCT',
 'samoa': 'WSM',
 'san marino': 'SMR',
 'sao tome and principe': 'STP',
 'saudi arabia': 'SAU',
 'senegal': 'SEN',
 'serbia': 'SRB',
 'seychelles': 'SYC',
 'sierra leone': 'SLE',
 'singapore': 'SGP',
 'sint maarten': 'SXM',
 'slovakia': 'SVK',
 'slovenia': 'SVN',
 'solomon islands': 'SLB',
 'somalia': 'SOM',
 'south africa': 'ZAF',
 'south sudan': 'SSD',
 'spain': 'ESP',
 'sri lanka': 'LKA',
 'sudan': 'SDN',
 'suriname': 'SUR',
 'swaziland': 'SWZ',
 'sweden': 'SWE',
 'switzerland': 'CHE',
 'syria': 'SYR',
 'taiwan': 'TWN',
 'tajikistan': 'TJK',
 'tanzania': 'TZA',
 'thailand': 'THA',
 'timor-leste': 'TLS',
 'togo': 'TGO',
 'tonga': 'TON',
 'trinidad and tobago': 'TTO',
 'tunisia': 'TUN',
 'turkey': 'TUR',
 'turkmenistan': 'TKM',
 'tuvalu': 'TUV',
 'uganda': 'UGA',
 'ukraine': 'UKR',
 'united arab emirates': 'ARE',
 'united kingdom': 'GBR',
 'united states': 'USA',
 'uruguay': 'URY',
 'uzbekistan': 'UZB',
 'vanuatu': 'VUT',
 'venezuela': 'VEN',
 'vietnam': 'VNM',
 'virgin islands': 'VGB',
 'west bank': 'WBG',
 'yemen': 'YEM',
 'zambia': 'ZMB',
 'zimbabwe': 'ZWE'}
from collections import Counter
colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
    "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
    "#08519c", "#0b4083", "#08306b"
]
def geoplot(df):
    country_with_code,country = {},{}
    show_countries = ",".join(df['country'].dropna()).split(',')
    for c,v in  dict(Counter(show_countries)).items():
        code =""
        if c.lower() in country_codes:
            code = country_codes[c.lower()]
        country_with_code[code] = v #USed for world map
        country[c] = v #Used for Bar chart

    data =[ dict(
        type = 'choropleth',
        locations = list(country_with_code.keys()),
        z = list(country_with_code.values()),
        colorscale = [[0, "rgb(5, 10, 172)"], [0.65, "rgb(40, 60, 190)"], [0.75, "rgb(70, 100, 245)"], \
                      [0.80, "rgb(90, 120, 245)"], [0.9, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict(
                color = 'gray',
                width = 0.5

            )
        ),
        colorbar = dict(
         autotick = False,
         title = ''

        ),
    )
    ]
    layout = dict(
     title='',
     geo=dict(
      showframe=False,
      showcoastlines=False,
      projection=dict(
       type='Mercator'
      )
     )
    )
    fig = dict(data = data,layout = layout)
    #plot(fig,validate=False,filename='d3-world-map')
    return country
country_vals = geoplot(df)
tabs = Counter(country_vals).most_common(25)

label = [_[0] for _ in tabs][::-1]
values = [_ [1] for _ in tabs[::-1]]
trace1 = go.Bar(y=label,x=values,orientation = 'h',name = "",marker = dict(color="#a678de"))

data = [trace1]
layout = go.Layout(title = "Countries with most content",height = 700,legend = dict(x=0.1,y=1.1,orientation = "h"))
fig = go.Figure(data, layout=layout)
#fig.show()

#Distribution of movie duration
import plotly.figure_factory as ff
movies_df = df[df['type'] == 'Movie'].copy()

# Remove 'min' text and convert to float
movies_df['duration'] = movies_df['duration'].str.replace(' min', '', regex=False)

# Convert to float safely
x1 = movies_df['duration'].astype(float)
fig = ff.create_distplot([x1], ['Movie Duration'], bin_size=5, curve_type='normal', colors=["#6ad49b"])
fig.update_layout(title_text='Distribution of Movie Durations')
#fig.show()
'''
x1 = df['duration'].fillna(0.0).astype(float)
fig = ff.create_distplot([x1],['a'],bin_size=0.7,curve_type = 'normal',colors =["#6ad49b"])
fig.update_layout(tite_text='Distplot with normal distribution')
fig.show()
'''
#TV shows with many seasons
import plotly.graph_objects as go
df = pd.read_csv(r"C:\Users\Muthuvalli\Desktop\Muthuvalli Practise\datasets\netflix_titles_nov_2019.csv")
df['season_count'] = df['duration'].str.extract(r'(\d+)').astype(float)
print(df['season_count'])

# Drop missing values (Movies don't have seasons)
d1 = df.dropna(subset=['season_count'])

col = 'season_count'
vc1 = df[col].value_counts().reset_index()
vc1.columns = [col, "count"]
#vc1 = pd.DataFrame(vc1)
#vc1 = vc1.rename(columns = {col : "count","index":col})
print(vc1.dtypes)
print(vc1.columns)
print(vc1.head())

#vc1['count'] = vc1['count'].astype(float)
vc1['percentage'] = (vc1['count']/vc1['count'].sum()) * 100
vc1 = vc1.sort_values(col)
#create a bar chart
trace1 = go.Bar(x = vc1[col],y= vc1['count'],name = "TV shows",marker=dict(color ="#a678de"))
data=[trace1]
layout = go.Layout(title = "number of seasons in Tv shows",legend = dict(x=0.1, y=1.1,orientation='h'))
fig = go.Figure(data,layout=layout)
#fig.show()

#The rating of the content
d1 = df[df["type"] == 'TV Show']
d2 = df[df["type"] == 'Movie']
col = 'rating'
vc1 = d1['rating'].value_counts().reset_index()
print(vc1['count'])
print(vc1.dtypes)
vc1.columns = [col, 'count']
print(vc1)
vc1['count'] = pd.to_numeric(vc1['count'], errors='coerce')
vc1['percent'] = 100 * vc1['count'] / vc1['count'].sum()
vc1 = vc1.sort_values(col)

vc2 = d2['rating'].value_counts().reset_index()
print(vc2['count'])
print(vc2.dtypes)
vc2.columns = [col, 'count']
print(vc2)
vc2['count'] = pd.to_numeric(vc2['count'], errors='coerce')
vc2['percent'] = 100 * vc2['count'] / vc2['count'].sum()
vc2 = vc2.sort_values(col)
trace1 = go.Bar(x=vc1[col],y=vc1['count'],name = "Tv Shows",marker = dict(color="#a678de"))
trace2 = go.Bar(x=vc2[col],y=vc2['count'],name = "Movies",marker = dict(color="#6ad49b"))
data =[trace1,trace2]
layout = go.Layout(title = "Content added in the over years",legend = dict(x=0.1, y=1.1, orientation="h"))
fig = go.Figure(data,layout=layout)
#fig.show()

#What are the top categories
from collections import Counter
col='listed_in'
#join single sentence and then split each word
categories = ",".join(d2[col]).split(',')
counter_list = Counter(categories).most_common(50)
label = [_[0] for _ in counter_list] [::-1]
value = [_[1] for _ in counter_list][::-1]
trace1 = go.Bar(x=value,y=label,orientation ='h',name = "Tv shows",marker = dict(color="#a678de"))
data=trace1
layout = go.Layout(title="Content added over the years", legend=dict(x=0.1, y=1.1, orientation="h"))
fig = go.Figure(data, layout=layout)
fig.show()

#Top Actors on Netflix with most movies
def country_trace(country,flag = 'Movie'):
 df['country'] = df['country'].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
 df['from_us'] = df['country'].fillna("").apply(lambda x: 1 if country.lower() in x.lower() else 0)
 small = df[df['from_us'] == 1]
 if flag == 'Movie':
  small = small[small['duration'] != ""]
 else:
  small = small[small['season_count'] != ""]
 cast = ', '.join(small['cast'].fillna("")).split(', ')
 tags = Counter(cast).most_common(25)
 print(tags)
 tags = [_ for _ in tags if "" != _[0]]
 labels = [_[0]+" " for _ in tags][::-1]
 values = [_[1] for _ in tags][::-1]
 trace = go.Bar(y=label,x = values,orientation ='h',name='',marker = dict(color="#a678de"))
 return trace

from plotly.subplots import make_subplots
traces =[]
titles = ["United States", "","India","", "United Kingdom", "Canada","", "Spain","", "Japan"]
for title in titles:
 if title != "":
  traces.append(country_trace(title))
fig = make_subplots(rows=2, cols=5, subplot_titles=titles)
fig.add_trace(traces[0], 1, 1)
fig.add_trace(traces[1], 1, 3)
fig.add_trace(traces[2], 1, 5)
fig.add_trace(traces[3], 2, 1)
fig.add_trace(traces[4], 2, 3)
fig.add_trace(traces[5], 2, 5)
fig.update_layout(height=1200, showlegend=False)
fig.show()

#Top Actors on netflex with most Tv shows
traces=[]
titles = ["United States","", "United Kingdom"]
for tilte in titles:
 if tilte != "":
  traces.append(country_trace(title,flag='Tv Show'))
fig = make_subplots(rows=1, cols=3, subplot_titles=titles)
fig.add_trace(traces[0], 1,1)
fig.add_trace(traces[1], 1,3)
fig.update_layout(height=600, showlegend=False)
fig.show()

#Movie director from india with content
small = df[df['type'] == 'Movie']
small = small[small['country'] == 'India']
col ='director'
categories = ', '.join(small[col].fillna("")).split(', ')
counter_list = Counter(categories).most_common(12)
counter_list = [_ for _ in counter_list if _[0] != ""]
labels = [_[0] for _ in counter_list][::-1]
value = [_[1]for _ in counter_list][::-1]
trace2 = go.Bar(y=labels, x= value,orientation = 'h',name='Tv Shows',marker =dict(color="orange"))
data = [trace2]
layout = go.Layout(title ="Movie Director from india with content",legend = dict(x=0.1, y=1.1, orientation="h"))
fig = go.Figure(data,layout = layout)
fig.show()

#Most director from US with most content
small = df[df['type']=='Movie']
small = small[small['country'] == 'United States']
col = 'director'
categories = ', '.join(small[col].fillna("")).split(', ')
counter_list = Counter(categories).most_common(12)
counter_list = [_ for _ in counter_list if _[0] != ""]
labels = [_[0] for _ in counter_list][::-1]
value = [_[1]for _ in counter_list][::-1]
trace1 = go.Bar(y=labels, x=value, orientation="h", name="TV Shows", marker=dict(color="orange"))

data = [trace1]
layout = go.Layout(title="Movie Directors from US with most content", legend=dict(x=0.1, y=1.1, orientation="h"))
fig = go.Figure(data, layout=layout)
fig.show()

#Standup Comedies by Jay Karas
tag = "jay karas"
df["relevant"] = df['director'].fillna("").apply(lambda x: 1 if tag in x.lower() else 0)
small = df[df['relevant']==1]
print(small[['title','release_year','listed_in']])

#StandUp Comedies on Netflix united stated
tag = "Stand-Up Comedy"
df["relevant"] = df['listed_in'].fillna("").apply(lambda x: 1 if tag in x.lower() else 0)
small = df[df['relevant'] == 1]
print(small[small['country'] == "United Stated"][["title","country","release_year"]].head(8))

##StandUp Comedies on Netflix india
tag = "stand-up comedy"
df['relevant'] = df['listed_in'].fillna("").apply(lambda x: 1 if tag in x.lower() else 0)
small = df[df['relevant'] == 1]
print(small[small["country"].str.contains("India", case=False, na=False)]
      [['title','country','release_year']].head(10))


