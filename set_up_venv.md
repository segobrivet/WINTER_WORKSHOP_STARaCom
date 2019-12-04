# Commands to set up a virtual environnement

```
python -m pip install -U pip
pip install virtualenv
```

In the desired folder:
```
virtualenv venv
```

- For Linux users:  ```source venv/bin/activate```  
- For windows users:  ```venv\Scripts\activate.bat```

Now `venv` is activated. Make it visible to Jupyter:
```
pip install ipykernel
python -m ipykernel install --user --name=venv
```
Then on Jupyter notebook, you can select Kernel > Change kernel > venv
        
To install more libraries in the activated venv:
```
pip install --upgrade tensorflow
pip install scikit-image 
.....
```
