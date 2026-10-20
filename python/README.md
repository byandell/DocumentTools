---
title: "Python Language"
parent: "Document Digital Tools"
nav_order: 2
has_children: true
permalink: /python/
---

# Python Language

This is a collection of Python language references that I have found useful.
These were originally in the
[landmapy](https://github.com/byandell-envsys/landmapy)
repository.
See related in
[Environmental Systems](../envsys/).
Please offer suggestions to improve.

- [View Python Slides](https://byandell.github.io/DocumentTools/quarto/python.html)
- [Python Overview](#python-overview)
- [Earth Data Analytics (EDA) Workbook](#earth-data-analytics-eda-workbook)
  - [Coordinate Systems & Projections](#coordinate-systems--projections)
- [Useful Python Libraries](#useful-python-libraries)
  - [Lists of Python Libraries](#lists-of-python-libraries)
- [Plot Libraries and Systems](#plot-libraries-and-systems)
  - [Spatial Libraries](#spatial-libraries)
- [IPython Methods](#ipython-methods)
  - [Data](#data)
    - [Read and Write](#read-and-write)
    - [Store Magic Data](#store-magic-data)
    - [Cached Data via Decorator](#cached-data-via-decorator)
  - [Decorators](#decorators)
  - [Classes](#classes)
- Additional Pages
  - [Python Coding Strategy](./strategy.md)
  - [Interactive and Dynamic Plots](interactive.md)
  - [Python Default Kernel for Quarto](kernel.md)

_[byandell.github.io/DocumentTools](https://byandell.github.io/DocumentTools)_  

## Python Overview

- [Python Tutorial](https://docs.python.org/3/tutorial/)
  - [Modules](https://docs.python.org/3/tutorial/modules.html)
  - [Importing Modules](https://docs.python.org/3/reference/import.html)
  - [Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- [Pandas Library](https://pandas.pydata.org/docs/)
  - [Pandas Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html)
  - [Pandas API Reference](https://pandas.pydata.org/docs/reference/)
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Try and Except code for NetCDF](https://www.earthdatascience.org/courses/use-data-open-source-python/hierarchical-data-formats-hdf/get-maca-2-climate-data-netcdf-python/);
- [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/)
  - [Hitchhikers Guide to Documentation](https://docs.python-guide.org/writing/documentation/)
    - [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/#introduction)
    - [PEP 257: Docstring Conventions](https://peps.python.org/pep-0257/)
  - [Documentation in Python: Methods and Best Practices](https://swimm.io/learn/code-documentation/documentation-in-python-methods-and-best-practices)
- [Python Developer’s Guide](https://devguide.python.org/)
- [Integrating Python Code With R](https://www.geeksforgeeks.org/integrating-python-code-with-r/)

## Earth Data Analytics (EDA) Workbook

- [EDA Scientific Data Structures in Python](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/)
- [Subtract One Raster from Another and Export a New GeoTIFF in Open Source Python](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/raster-data-processing/subtract-rasters-in-python/)
- [Earth Analytics Python Env](https://github.com/earthlab/earth-analytics-python-env)
  - [EDA 4. Set Up Your Conda Earth Analytics Python Environment Setup earth analytics environment](https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-python-conda-earth-analytics-environment/)
    - [Python venv: How To Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv)
  - [EDA 6.15. Intro to Pandas Dataframes](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/)

### Coordinate Systems & Projections

- [Introduction to Python for Geographic Data Analysis (Python GIS)](https://pythongis.org)
  - [Working with map projections (Python GIS)](https://pythongis.org/part2/chapter-06/nb/03-coordinate-reference-system.html)
  - [Coordinate Reference Systems (Python GIS)](https://www.python-gis.org/fundamentals-of-python-gis/coordinate-reference-systems/)
    - [Building Custom Map Projections in Python (Python GIS)](https://www.python-gis.org/fundamentals-of-python-gis/coordinate-reference-systems/building-custom-map-projections-in-python/)
- [GeoPandas: Working with Geospatial Data in Python (realpython)](https://realpython.com/geopandas/)
- [Spatial data in Python – CRS and projections (University of Tartu)](https://kodu.ut.ee/~kmoch/geopython2025/Py_02/crs-projections.html)
- [Reprojecting and transforming data — Geocomputation with Python](https://py.geocompx.org/06-reproj)
- [Python Projection Transforms (Medium)](https://medium.com/@stacyfuende/python-projection-transforms-c047fecf2081)

Some common coordinate systems:

- [EPSG:4326](https://epsg.io/4326): WGS84 = World Geodetic System 1984
- [EPSG:32618](https://epsg.io/32618): WGS84 for UTM zone 18N (North America)
- [EPSG:32730](https://epsg.io/32720): WGS84 for UTM zone 20S (South America)
  
## Useful Python Libraries

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [math](https://docs.python.org/3/library/math.html)
- [time](https://docs.python.org/3/library/time.html)
- [glob](https://docs.python.org/3/library/glob.html)
- [os](https://docs.python.org/3/library/os.html)
- [re](https://docs.python.org/3/library/re.html)
- [csv](https://docs.python.org/3/library/csv.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [zipfile](https://docs.python.org/3/library/zipfile.html)
- [warnings](https://docs.python.org/3/library/warnings.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [scipy](https://www.scipy.org/)
- [scikit-fuzzy](https://pythonhosted.org/scikit-fuzzy/)
- [sklearn](https://scikit-learn.org/) (scikit-learn)
  - [sklearn.model_selection](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection)
  - [sklearn.metrics](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics)
  - [sklearn.cluster](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.cluster)
  - [sklearn.tree](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.tree)
- [seaborn](https://seaborn.pydata.org/)
- [statsmodels](https://www.statsmodels.org/)
- [pystac_client](https://pystac-client.readthedocs.io/en/latest/)
- [pystac](https://pystac.readthedocs.io/en/latest/)

### Lists of Python Libraries

- [The Python Standard Library](https://docs.python.org/3/library/)
- [Python Libraries](https://www.python.org/about/apps/)
- [Awesome Python](https://awesome-python.com/)
- Fan Lists
  - [Geeks4Geeks](https://www.geeksforgeeks.org/python-libraries-to-know/)
  - [dev.to/taipy](https://dev.to/taipy/top-42-python-libraries-you-need-to-know-1omo)
  - [hackr.io](https://hackr.io/blog/best-python-libraries)
  - [Great Learning](https://www.mygreatlearning.com/blog/open-source-python-libraries/)

## Plot Libraries and Systems

See `landmapy` [Plot Functions](plots.md).

- [matplotlib](https://matplotlib.org/)
  - [matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_api.html) ⚠️
  - [matplotlib.colors](https://matplotlib.org/stable/api/colors_api.html)
- [shapely](https://shapely.readthedocs.io/en/stable/)
  - [shapely.geometry](https://shapely.readthedocs.io/en/stable/manual.html#geometric-objects)
- [HoloViews](https://holoviews.org/)
- [GeoViews](https://geoviews.org/)
- [contextily](https://contextily.readthedocs.io/en/latest/)
- [panel](https://panel.holoviz.org/)
- [hvplot](https://hvplot.holoviz.org/)
  - [hvplot.pandas](https://hvplot.holoviz.org/user_guide/Plotting_with_Pandas.html) ⚠️
  - [hvplot.xarray](https://hvplot.holoviz.org/user_guide/Plotting_with_XArray.html) ⚠️
- [plotnine](https://plotnine.readthedocs.io/en/stable/)

### Spatial Libraries

- [geopandas](https://geopandas.org/)
- [rasterio](https://rasterio.readthedocs.io/)
  - [rasterstats](https://pythonhosted.org/rasterstats/)
- [xarray](http://xarray.pydata.org/en/)
  - [rioxarray](https://corteva.github.io/rioxarray/stable/)
- [xrspatial](https://xarray-spatial.readthedocs.io/en/stable/)
- [earthaccess](https://earthaccess.readthedocs.io/en/latest/)
- [getpass](https://docs.python.org/3/library/getpass.html)
- [earthpy](https://earthpy.readthedocs.io/en/latest/)
- [tqdm](https://tqdm.github.io/)
  - [tqdm.notebook](https://tqdm.github.io/docs/notebook/)
- [regionmask](https://regionmask.readthedocs.io/en/stable/)
- [cartopy](https://scitools.org.uk/cartopy/docs/latest/)
  - [cartopy.crs](https://scitools.org.uk/cartopy/docs/latest/crs/index.html) ⚠️
  - [geoplot](https://residentmario.github.io/geoplot/index.html)
- [folium](https://python-visualization.github.io/folium/)
- [geopy](https://geopy.readthedocs.io/en/stable/)
- [pyproj](https://pyproj4.github.io/pyproj/stable/)

## IPython Methods

**AI overview:**
IPython methods enhance interactive computing in Python, offering features beyond the standard interpreter. Some key methods include:

- Tab Completion:
Simplifies code writing by suggesting attributes and methods of objects or modules as you type.
- Introspection:
Provides detailed information about objects, functions, or modules using `?` or `??`.
- Magic Commands:
Special commands prefixed with `%` for tasks like timing code execution (`%timeit`), running external scripts (`%run`), or accessing shell commands (`!`).
- Input Caching:
Stores previous commands and outputs, accessible via `_`, `__`, `___` for outputs and `_i`, `_ii`, `_iii` or `In[n]` for inputs.
- Rich Display:
Enables richer object representations using `_ipython_display_()` or `_repr_*_()` methods for custom display formats like HTML or images.
- History:
Allows browsing and reusing previous commands across sessions.
These methods streamline development, debugging, and exploration in interactive Python environments.

References:

- [IPython Reference](https://ipython.org/ipython-doc/3/interactive/reference.html)
  - [Built-in magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)
  - [Interactive Computing](https://ipython.org/ipython-doc/3/interactive/tutorial.html)
- [Store Magic](https://ipython.readthedocs.io/en/stable/config/extensions/storemagic.html)

### Data

Data can be explicitly stored in a file using `read` and `write` methods,
or implicitly using the `pickle` module.
Store Magic and caching are two ways to store data using
[pickle](https://docs.python.org/3/library/pickle.html).

#### Read and Write

Many projects read and write to files.
Following course guidelines, we use the `data_dir` variable to store data in a consistent location,
which for EDA is `~/earth-analytics/data`.
The
[landmapy/initial.py](https://github.com/byandell-envsys/landmapy/blob/main/landmapy/initial.py) ⚠️
has function `create_data_dir()` to create a directory if it does not exist.

```python
def create_data_dir(new_dir):
    import os
    import pathlib

    data_dir = os.path.join(
        pathlib.Path.home(),
        'earth-analytics',
        'data',
        new_dir
    )
    os.makedirs(data_dir, exist_ok=True)

    return data_dir
```

#### Store Magic Data

[Store Magic](https://ipython.readthedocs.io/en/stable/config/extensions/storemagic.html)
stores user data on demand via the magic command `%store blah` in a named file
in `~/.ipython/profile_default/db/autorestore/`,
and retrieve it with `%store -r blah`.
This is useful for storing data between sessions or projects.

The following code will try to retrieve the object `buffalo_gdf` if it was previously stored.
The `try` statement checks if `buffalo_gdf` exists, creating a `NameError` exception if not,
which leads to code to create and `%store` it.

```python
%store -r buffalo_gdf
try:
    buffalo_gdf
except NameError:
    import geopandas as gpd
    # Assume `data_dir` is defined and `geojson` file is saved there.
    # Read all grasslands GeoJSON into `grassland_gdf`.
    grassland_url = f"{data_dir}/National_Grassland_Units_(Feature_Layer).geojson"
    grassland_gdf = gpd.read_file(grassland_url)
    # Subset to desired locations.
    buffalo_gdf = grassland_gdf.loc[grassland_gdf['GRASSLANDNAME'].isin(
        ["Buffalo Gap National Grassland", "Oglala National Grassland"])]
    %store buffalo_gdf
    print("buffalo_gdf created and stored")
else:
    print("buffalo_gdf retrieved from StoreMagic")
```

#### Cached Data via Decorator

The
[landmapy/cached.py](https://github.com/byandell-envsys/landmapy/blob/main/landmapy/cached.py) ⚠️
decorator caches data in the `jars` directory `~/earth-analytics/data/jars/`.
The decorator `@cached` is used to cache the results of a function.
See examples in
[clustering.qmd](https://github.com/earthlab-education/clustering-byandell/blob/main/clustering.qmd)
using functions in the
[landmapy/reflect.py](https://github.com/byandell-envsys/landmapy/blob/main/landmapy/reflect.py) ⚠️
module.
Some explanation of decorators is in the next section.
There is no need to use Store Magic with this decorator,
as it already caches the data in the `jars` directory.

### Decorators

Code for a caching **decorator** is in
[landmapy/cached.py](https://github.com/byandell-envsys/landmapy/blob/main/landmapy/cached.py) ⚠️,
which you can use in your code.
This decorator will **pickle** the results of running a `do_something()` function,
and only run the code if the results do not already exist.
To override the caching, for example temporarily after
making changes to your code, set `override=True`.
Note that to use the caching decorator, you must write your own function to perform each task.
See examples in
[landmapy/delta.py](https://github.com/byandell-envsys/landmapy/blob/main/landmapy/delta.py) ⚠️
and
[landmapy/reflectance.py](https://github.com/byandell-envsys/landmapy/blob/main/landmapy/reflectance.py) ⚠️.

- [Clustering Project](https://github.com/earthlab-education/clustering-byandell/blob/main/clustering.qmd)
- [Decorators in Python (Geeks4Geeks)](https://www.geeksforgeeks.org/decorators-in-python/)
- [Primer on Python Decorators (RealPython)](https://realpython.com/primer-on-python-decorators/)
- [PEP 318 – Decorators for Functions and Methods](https://peps.python.org/pep-0318/)
- [Python Decorators with Examples (Programiz)](https://www.programiz.com/python-programming/decorator)
- [Practical Decorators by Reuven M Lerner](https://www.youtube.com/watch?v=MjHpMCIvwsY)
- [Python Workout by Reuven M Lerner](https://www.manning.com/books/python-workout)
- [Decorators with Parameters (StackOverflow)](https://stackoverflow.com/questions/5929107/decorators-with-parameters)

One way of thinking about decorators with arguments is

```python
@decorator
def foo(*args, **kwargs):
    pass
```

translates to

```python
foo = decorator(foo)
```

So if the decorator had arguments,

```python
@decorator_with_args(arg)
def foo(*args, **kwargs):
    pass
```

translates to

```python
foo = decorator_with_args(arg)(foo)
```

That is, `decorator_with_args()` is a function which accepts a custom argument
and which returns the actual decorator (that will be applied to the decorated function).

A decorator with arguments can be used in a notebook or document.
However, in order to embed the arguments within a module takes a bit more care.
For instance,
[landmapy/reflect.py](https://github.com/byandell-envsys/landmapy/blob/main/landmapy/reflect.py) ⚠️
uses the `@cached` decorator
from
[landmapy/cached.py](https://github.com/byandell-envsys/landmapy/blob/main/landmapy/cached.py) ⚠️
to cache the results of the function.
The original static use of the decorator was

```python
from landmapy.cached import cached

@cached('wbd_08')
def read_wbd_file(wbd_filename, huc_level, cache_key):
    ...
def read_delta_gdf(huc_level=12, huc_region='08', watershed='080902030506'):
    wbd_gdf = read_wbd_file(
        f"WBD_{huc_region}_HU2_Shape", huc_level, cache_key=f'hu{huc_level}')
    ...
```

Note the keyword argument `cache_key` is used in the function `read_delta_gdf()` when
calling the decorated function `read_wbd_file()`,
with data cached in the `jars` directory as `f'wbd_08_hu{huc_level}.pickle'`,
with the HUC level 12 changeable, but not the HUC region.
To make this more flexible, the code was changed as follows:

```python
from landmapy.cached import cached

def read_wbd_file(wbd_filename, huc_level, cache_key,
                  func_key='wbd_08', override=False):
    @cached(func_key, override)
    def read_wbd_cached(wbd_filename, huc_level, cache_key):
    ...
    wbd_gdf = read_wbd_cached(wbd_filename, huc_level, cache_key=cache_key)
    return wbd_gdf
def read_delta_gdf(huc_level=12, huc_region='08', watershed='080902030506',
                   func_key='wbd_08', override=False):
    wbd_gdf = read_wbd_file(
        f"WBD_{huc_region}_HU2_Shape", huc_level,
        cache_key=f'hu{huc_level}',
        func_key=func_key, override=override)
    ...
```

The revised function `read_delta_gdf()` has added arguments
for the @cached decorator `func_key` and `override`.
In addition, `read_wbd_file()` is now an undecorated function that calls
the internal decorated function `read_wbd_cached()`.
The decorator `@cached` is now inside the function `read_wbd_file()`,
called with arguments `func_key` and `override`.
The keyword argument `cache_key` is still used in the function `read_delta_gdf()`
and importantly in the call to the decorated function `read_wbd_cached()`
from within `read_wbd_file()`.
Data are now cached in the `jars` directory as `'f{func_key}_hu{huc_level}.pickle'`,
which changes with the HUC level 12 and HUC region.

### Classes

A
[class](https://docs.python.org/3/tutorial/classes.html)
is a function with output of an object that has new methods, which are in turn functions
defined in the class.
In addition, the `@property` decorator defines attributes for an object.
The main uses of classes are to:

- add functionality to an existing class
- streamline different functions with the same parameters to keep track of metadata

**AI overview:**
In Python, a class serves as a blueprint for creating objects,
which are instances that encapsulate data (attributes) and behavior (methods).
Classes facilitate object-oriented programming (OOP) principles,
enabling code reusability, modularity, and organization.
A class is defined using the class keyword, followed by the class name and a colon.
Inside the class block, attributes and methods are defined.
The **init** method is a special method, known as the constructor,
which is automatically called when an object of the class is created
to initialize the object's attributes.

- [Habitat Suitability Notes](https://github.com/earthlab-education/habitat-suitability-byandell/blob/main/notes.qmd) ⚠️
- [Python 3 Documentation](https://docs.python.org/3/)
  - [3. Data model](https://docs.python.org/3/reference/datamodel.html)
  - [9. Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Classes and Objects (Geeks4Geeks)](https://www.geeksforgeeks.org/python-classes-and-objects/)
- [Python Classes: The Power of Object-Oriented Programming (RealPython)](https://realpython.com/python-classes/)
- [Google's Python Class](https://developers.google.com/edu/python)
- [earthpy](https://earthpy.readthedocs.io/en/latest/)
  - [apppeears.py](https://github.com/earthlab/earthpy/blob/apppeears/earthpy/appeears.py) ⚠️ (class Elsa created in `earthpy` package)
