import pandas as pd

dbmf_nav = (
    pd.read_excel("DBMF-Table.xlsx")
    .rename(columns=lambda xs: xs.lower())
)

print(dbmf_nav[dbmf_nav.date.diff().div(pd.Timedelta(days=1)) > 10])

dbmf_nav.loc[756, "date"] = dbmf_nav.loc[756, "date"].replace(year=dbmf_nav.loc[755, "date"].year)
dbmf_nav.loc[890, "date"] = dbmf_nav.loc[890, "date"].replace(month=11)
dbmf_nav.loc[1115, "date"] = dbmf_nav.loc[1115, "date"].replace(year=dbmf_nav.loc[1114, "date"].year)
dbmf_nav.loc[1119, "date"] = dbmf_nav.loc[1119, "date"].replace(year=dbmf_nav.loc[1118, "date"].year)

dbmf_nav = dbmf_nav.set_index("date").nav
dbmf_nav_ret = dbmf_nav.transform(lambda xs: xs / xs.shift() - 1)
