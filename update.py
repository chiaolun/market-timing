import papermill as pm

for params in [
        dict(
            output='MA200 fast and slow - tradeable version.ipynb',
            kwargs=dict(symbol='SPY'),
        ),
        dict(
            output='MA200 fast and slow - untradeable version.ipynb',
            kwargs=dict(symbol='^GSPC'),
        ),
        dict(
            output='MA200 fast and slow - untradeable version - all_history.ipynb',
            kwargs=dict(symbol='^GSPC', start_date=None),
        ),
]:
    pm.execute_notebook(
        'MA200 fast and slow - template.ipynb',
        params['output'], parameters=params['kwargs'],
    )
