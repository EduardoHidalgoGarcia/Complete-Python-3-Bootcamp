#usefull functions in python


#r str for pandas dataframe
def rstr(df): return df.shape, df.apply(lambda x: [x.unique()])

#use:
#print(rstr(iris))


def embed_map(m, file_name):
    from IPython.display import IFrame
    m.save(file_name)
    return IFrame(file_name, width='100%', height='500px')





def my_geocoder(row):
    try:
        point = geocode(row, provider='nominatim').geometry.iloc[0]
        return pd.Series({'Latitude': point.y, 'Longitude': point.x, 'geometry': point})
    except:
        return None

