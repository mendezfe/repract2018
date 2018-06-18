import pandas as pd, os
import seaborn as sns, matplotlib.pyplot as plt, numpy as np
sns.set_style('darkgrid')

base = '../../data/codedtruth'
dfdict = {x[:-4]:pd.read_csv(f'{base}/{x}') for x in os.listdir(base) 
          if x.endswith('.csv') and 'coded' not in x}

# this might be of use elsewhere, too
scale = ['Essential', 'Worthwhile', 'Unimportant', 'Unwise']
dfdict['truth_ratings']['rating'] = pd.Categorical(dfdict['truth_ratings']['rating'], scale, ordered=True)

def count_sample(df, var):
    return df[['lfdn', var]].groupby(var).count()

def plot_sample(df, var, varname):
    count_sample(df, var).sort_index(ascending=False).plot.barh(color='k', alpha=0.7, figsize=(10,6), legend=[])
    plt.xlabel('Number of Respondents')
    plt.ylabel(varname)
    plt.tight_layout()

sizes = ['Small (1-4)', 'Medium (5-10)', 'Larger (10-49)', 'Very large (50+)']

ratings_with_respondent_meta = dfdict['truth_ratings'].merge(dfdict['truth_metadata'], how='inner')
ratings_with_respondent_meta['v_14'] = pd.Categorical(ratings_with_respondent_meta['v_14'], sizes, ordered=True)

def plot_df(df, var, varname, absolute=True):
    if type(var) == str:
        data = df[['lfdn', var, 'rating']
                                ].groupby([var, 'rating']).count(
        ).fillna(0).astype(int).unstack().sort_index(ascending=False)
    else:
        data = df[['lfdn'] + var + ['rating']
                                ].groupby(var + ['rating']).count(
        ).fillna(0).astype(int).unstack().sort_index(ascending=False)
    if absolute:
        data.plot.barh(stacked=True, cmap='bwr', alpha=0.5, figsize=(10,6)) 
    else:
        data.div(data.sum(axis=1).values, axis=0).plot.barh(stacked=True, cmap='bwr', alpha=0.5, figsize=(10,6))
        plt.xlim((0,1))
        plt.xticks(np.arange(0,1.01,0.1))
    plt.xlabel('Number of Ratings' if absolute else 'Percentage of Ratings')
    plt.ylabel(varname)
    plt.legend([])
    plt.tight_layout()
    
def split_tags(old_df, level_4=False):
    df = pd.DataFrame(old_df, copy=True)
    levels = [x.split(':') for x in df.Tag]
    df['level_1'] = [x[0] for x in levels]
    df['level_2'] = [x[1] for x in levels]
    df['level_3'] = [x[2].split('_')[0] for x in levels]
    if level_4:
        df['level_4'] = [x[2].split('_')[1] if '_' in x[2] else '' for x in levels]
    return df
    
all_levels = [f'level_{x}' for x in range(1,5)]
all_ratings = ['Essential', 'Worthwhile', 'Unimportant', 'Unwise']

papertags_method = split_tags(dfdict['papertags_how_withwhom_final'], level_4=False)
papertags_content = split_tags(dfdict['papertags_what_final'], level_4=True)

def tag_stats(tagdf, all_levels, totals=True, rel=False):
    df = tagdf.groupby(all_levels + ['rating']).count()[['Tag']
                                                       ].dropna().unstack().fillna(0).rename(columns=str).astype(int)
    if rel:
        rowsums = df.sum(axis=1)
        for col in df.columns.values:
            df[col] = df[col] / rowsums
    if totals:        
        df['Positive'] = df[('Tag','Essential')] + df[('Tag','Worthwhile')]
        df['Negative'] = df[('Tag','Unimportant')] + df[('Tag','Unwise')]
        df['Total'] = df['Positive'] + df['Negative']
    else:
        df['Total'] = df.sum(axis=1)
    return df
    
def plot_tag_ratings(df, sort_values=True, rel=False, step=25):
    if sort_values:
        df.sort_values(['Positive', ('Tag', 'Essential')])[df.columns.values[:4]
            ].plot.barh(stacked=True, cmap='bwr', figsize=(9,6), alpha=0.5)
    else:
        df[df.columns.values[:4]].plot.barh(stacked=True, cmap='bwr', figsize=(9,6), alpha=0.5)
    plt.legend([])
    plt.ylabel('')
    if not rel:
        maxval = df['Total'].max()
        upperbound = (divmod(maxval,100)[0]+1)*100
        plt.xlim((0,upperbound))
        plt.xticks(np.arange(0,upperbound+1,step))
    else:
        plt.xlim((0,1))
        plt.xticks(np.arange(0,1.01,0.1))
    plt.tight_layout()
