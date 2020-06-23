import numpy as np
from sklego.pandas_utils import log_step

@log_step
def start_pipeline(dataf):
    return dataf.copy()

@log_step
def set_types_names(dataf):
    dataf.columns = [c.lower() for c in dataf.columns]
    return dataf[['workweekhrs', 'convertedcomp', 'country', 'devtype',
                  'languageworkedwith', 'yearscode', 
                  'age', 'gender', 'ethnicity']]

@log_step
def filter_outliers(dataf, max_week_hrs=60, max_salary=300000):
    return (dataf
            .loc[lambda d: d['workweekhrs'] <= max_week_hrs]
            .loc[lambda d: d['convertedcomp'] <= max_salary])

@log_step
def split_column(dataf, datacol, split=';', prefix='lang'):
    clean_col = dataf[datacol].str.lower().str.replace('+', 'plus')
    split_col = clean_col.apply(lambda d: str(d).split(";"))
    groups = set(split_col.explode())
    for g in groups:
        dataf[f"{prefix}_{g.replace(' ', '_')}"] = clean_col.str.contains(g)
    return dataf

@log_step
def add_categorical_features(dataf):
    return (dataf
            .pipe(split_column, datacol='languageworkedwith')
            .pipe(split_column, datacol='devtype', prefix='devtype')
            .pipe(split_column, datacol='ethnicity', prefix='ethnicity')
            .drop(columns=['languageworkedwith', 'devtype', 'ethnicity']))

@log_step
def normalise_features(dataf):
    return (dataf
            .assign(gender=lambda d: np.where(d['gender'].str.contains('binary'), 'Non-Binary', d['gender']))
            .assign(gender=lambda d: np.where(d['gender'].str.contains('Woman;Man'), 'Non-Binary', d['gender'])))
