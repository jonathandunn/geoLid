import os
import fasttext
import urllib.request
from cleantext import clean

#---------------------
def download_model(model = "all", data_dir = None):

    #First set the data directories
    #If no directories set, use default
    if data_dir == None:
        data_dir = "models"

    #Make dir if necessary
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
        
    print("Saving models to " + data_dir)
    
    #Second, define the list of possible models
    model_list = {
        "baseline":"https://uofi.box.com/shared/static/q9329djbi7k9ss9aam9d690v24ceq9cy.bin",
        "africa_north":"https://uofi.box.com/shared/static/h1aip1g1k66598ght79pq5y8xbz79xpg.bin",
        "africa_southern":"https://uofi.box.com/shared/static/zwfmxb2r7nsl3b0dnw35amiirkwk454w.bin",
        "africa_sub":"https://uofi.box.com/shared/static/66ukzhe7rjr036t5aimnnv5libf9qhsm.bin",
        "america_brazil":"https://uofi.box.com/shared/static/38m3i7qwbygasni5ih2b1lw1m1iwo5oj.bin",
        "america_central":"https://uofi.box.com/shared/static/eytjcqgnkye3bsh1k3c2skp8ds4elncj.bin",
        "america_north":"https://uofi.box.com/shared/static/vqssq1rl0qs71qsj5lnze7k5vfv4cddu.bin",
        "america_south":"https://uofi.box.com/shared/static/bg1vbpfixsk0lo16epxdfg9y8j63feh5.bin",
        "asia_central":"https://uofi.box.com/shared/static/tmzbhihm08euxeyzdohg4o3lq6f8yqbi.bin",
        "asia_east":"https://uofi.box.com/shared/static/h67chtegv28dohnbyk7rxuqe7ppee6dy.bin",
        "asia_south":"https://uofi.box.com/shared/static/36hymeckcdbkv7m11akkgldu8wnv9vp2.bin",
        "asia_southeast":"https://uofi.box.com/shared/static/0a08li6wnkwouwgyhq5ve3f26m6mlp7y.bin",
        "europe_east":"https://uofi.box.com/shared/static/aasygzv6hnvtss6lzwnvdbf38w9hg1ze.bin",
        "europe_russia":"https://uofi.box.com/shared/static/jml2a1huyl8mz2abgw4sz2jgnzn3wrtc.bin",
        "europe_west":"https://uofi.box.com/shared/static/o947o1gz87m1ghrhjh7kdltctva8ggr7.bin",
        "middle_east":"https://uofi.box.com/shared/static/ef1z5j4rx797vz8qngq88b551b0dsyoc.bin",
        "oceania":"https://uofi.box.com/shared/static/pl5di6c94fdygr5coh2ek6nrc5si45c5.bin",
        }
    
    #Third, download single model
    if model != "all":
        try:
            url = model_list[model]
        except:
            print("Valid download files: \n")
            print(model_list)
            sys.kill()
        
        #Download to the data directory
        urllib.request.urlretrieve(url, os.path.join(data_dir, "geolid."+model+".bin"))

    #Fourth download all models
    elif model == "all":
        for name in model_list:
            url = model_list[name]
            
            #Download to the data directory
            urllib.request.urlretrieve(url, os.path.join(data_dir, model))
    
    print("Finished downloading to ", os.path.join(data_dir))
#-----------------------------------------------------------------------------------------------

class geoLid(object):

    def __init__(self, model_location = None):

        #Default model location
        if model_location == None:
            self.model_location = os.path.join(".", "models")
        else:
            self.model_location = model_location

    #-----------------------------------------------------------------
    
    def clean_it(self, line):

        #Remove non-linguistic characters
        line = clean(line,
                        fix_unicode = True,
                        to_ascii = False,
                        lower = True,
                        no_line_breaks = True,
                        no_urls = True,
                        no_emails = True,
                        no_phone_numbers = True,
                        no_numbers = True,
                        no_digits = True,
                        no_currency_symbols = True,
                        no_punct = True,
                        replace_with_punct = "",
                        replace_with_url = "",
                        replace_with_email = "",
                        replace_with_phone_number = "",
                        replace_with_number = "",
                        replace_with_digit = "",
                        replace_with_currency_symbol = "",
                        )

        #Make spaceless
        line = "".join(line.split())    #NO SPACES
        line = " ".join(line)           #SPACES FOR EACH

        return line

    #-----------------------------------------------------------------

    def predict(self, data, region = "baseline"):

        #First load the required model
        model = fasttext.load_model(os.path.join(self.model_location, "geolid."+region+".bin"))

        #Second clean data
        data = [self.clean_it(line) for line in data]

        #Third get predictions
        predictions = model.predict(data)[0]
        predictions = [x[0].replace("__label__","") for x in predictions]

        return predictions

    #-----------------------------------------------------------------