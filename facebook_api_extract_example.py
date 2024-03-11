from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adreportrun import AdReportRun
import time

# You get this when you create a new app on developers.facebook.com
access_token = 'insert_access_token_here'

# IMPORTANT: Your ad account id appears in the url when you sign into your ad account
# It will be after the act= in the url
# When you type it into the code, it should look like this: 'act_[insert_ad_account_id_here]'
# Example: https://adsmanager.facebook.com/adsmanager/reporting/view?act=[ad_account_id]&business_id=[business_id]
ad_account_id = 'act_[insert_ad_account_id_here]'

# For app secret and app_id, you can rely on FB to provide you with the correct ones
app_secret = 'app_secret'
app_id = 'app_id'
FacebookAdsApi.init(access_token=access_token)

# You can add all kinds of fields here. The ones I have are just examples.
fields = [
    'purchase_roas',
     'spend',
    'clicks',
    'unique_clicks',
    'ctr',
    'unique_ctr',
    'cpc',
     'account_id',
     'account_name',
     'campaign_name',
    'campaign_id',
    'adset_name',
]
params = {
    #'time_range': {'since':'2023-01-01','until':'2023-12-31'}, # This is the same as date_preset: last_year
    'filtering': [],
    'level': 'adset',
    "date_preset": "last_year",
    'breakdowns': [],
    'limit': 1000,
}

# The code below is for pagination. If you have a lot of data, the standard code will not print out all of your data.
# This code will print out all of your data.
job = AdAccount(ad_account_id).get_insights_async(
    fields=fields,
    params=params,
)

TIMEOUT = 60

def wait_for_async_job(job):
    for _ in range(TIMEOUT):
        time.sleep(1)
        job = job.api_get()
        status = job[AdReportRun.Field.async_status]
        if status == "Job Completed":
            return list(job.get_result(params={"limit": 1000}))
        

result_cursor = wait_for_async_job(job)
results = [item for item in result_cursor]
print (results)




