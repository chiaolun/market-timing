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
]:
    pm.execute_notebook(
        'MA200 fast and slow - template.ipynb',
        params['output'], parameters=params['kwargs'],
    )
