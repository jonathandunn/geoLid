# geoLid
Geographically-informed language identification

This Python package carries out language identification with geographic priors to increase performance for low-resource and under-represented languages.

A description and evaluation of this approach can be found here: https://jdunn.name/2024/03/13/geographically-informed-language-identification/

A complete list of language codes and names per regional model can be found in the *language_names* directory.

**Installation**

This package can be installed through pip:

    pip install geoLid

**Downloading models**

geoLid contains a baseline non-geographic model as well as models for 16 specific regions, as shown below:

    baseline (916 languages)
    africa_north (44 languages)
    africa_southern (58 languages)
    africa_sub (166 languages)
    america_brazil (88 languages)
    america_central (188 languages)
    america_north (68 languages)
    america_south (129 languages)
    asia_central (54 languages)
    asia_east (46 languages)
    asia_south (60 languages)
    asia_southeast (325 languages)
    europe_east (65 languages)
    europe_russia (65 languages)
    europe_west (108 languages)
    middle_east (53 languages)
    oceania (49 languages)

To download models, use this command:

    from geoLid import download_model
    download_model("baseline")

The model name "all" will download all region-specific models.

**Usage**

Language identification can be used as shown below:

    from geoLid import geoLid
    lid = geoLid(model_location = "models")
    labels = lid.predict(data = data, region = "baseline")

The *model_location* during initialization points to the directory containing the LID models.

The input variable *data* is a list containing at least one string that represents a text to make predictions about.

The *region* variable indicates which region-specific model should be used. The default is to use the non-geographic baseline model.
