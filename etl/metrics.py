def compute_productivity_score(browser_df, app_df):
    work_time = browser_df[browser_df['category'] == 'Work']['time_spent'].sum()
    entertainment_time = browser_df[browser_df['category'] == 'Entertainment']['time_spent'].sum()
    app_work = app_df[app_df['app_name'].isin(['VS Code', 'Chrome'])]['minutes'].sum()

    score = (work_time + app_work) / (entertainment_time + 1)
    return round(min(score * 10, 100), 2)
    
    
def compute_sleep_adequacy(sleep_df):
    avg_sleep = sleep_df['sleep_hours'].mean()
    return round((avg_sleep / 8) * 100, 2)


def entertainment_work_ratio(app_df):
    entertainment_apps = ['Instagram', 'YouTube', 'Netflix', 'Spotify']
    ent = app_df[app_df['app_name'].isin(entertainment_apps)]['minutes'].sum()
    work = app_df[~app_df['app_name'].isin(entertainment_apps)]['minutes'].sum()
    return round(ent / (work + 1), 2)
