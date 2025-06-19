# Authentication with HyP3

Users must authenticate with 
[Earthdata Login](https://urs.earthdata.nasa.gov/ "https://urs.earthdata.nasa.gov/" ){target=_blank} 
credentials before they can submit jobs to HyP3 for processing or access information about the resulting 
On Demand products.

The options available for authentication depend on the interface you are using to interact with HyP3 functionality. 

- The [Vertex](https://search.asf.alaska.edu/ "search.asf.alaska.edu" ){target=_blank} search and discovery 
  interface is a map-based web application that allows users to search for Sentinel-1 acquisitions, submit them for 
  processing by HyP3, and access the resulting On Demand products.
- Programmatic access is available through the  
  [HyP3 API](../using/api.md "hyp3-docs.asf.alaska.edu/using/api") or 
  [HyP3 Python SDK](../using/sdk.md "hyp3-docs.asf.alaska.edu/using/sdk").

## Authentication in Vertex

Users need to sign in with 
[Earthdata Login credentials](https://urs.earthdata.nasa.gov/ "urs.earthdata.nasa.gov" ){target=_blank} 



## Authentication with HyP3 API

There are a couple of authentication methods available when using the 
[HyP3 API](../using/api.md "hyp3-docs.asf.alaska.edu/using/api"). 
The most common is using an 
[Earthdata Login session cookie](#earthdata-login-session-cookie "Jump to the Earthdata Login Session Cookie section of this document"), 
but you can also use an 
[Earthdata Login token](#earthdata-login-token "Jump to the Earthdata Login Token section of this document").

### Earthdata Login Session Cookie

You can authorize the HyP3 API by having a valid Earthdata Login (asf-urs) session cookie in your web environment. 
This cookie is generated when you enter your Earthdata Login credentials in a browser, either by clicking the 
**Sign In** icon in 
[Vertex](https://search.asf.alaska.edu/ "search.asf.alaska.edu" ){target=_blank}, 
or by using the 
[Earthdata Login](https://urs.earthdata.nasa.gov/ "urs.earthdata.nasa.gov" ){target=_blank} 
web interface.

### Earthdata Login Token

Earthdata Login (EDL) supports the generation of tokens that are valid for 60 days. These user/bearer tokens can be 
used for EDL authentication instead of entering a username and password. The 
[User Token Management](https://urs.earthdata.nasa.gov/documentation/for_users/user_token "urs.earthdata.nasa.gov/documentation/for_users/user_token" ){target=_blank} 
document provides step-by-step guidance for generating an EDL token, which you can do either in the 
[Earthdata Login web interface](https://urs.earthdata.nasa.gov/ "https://urs.earthdata.nasa.gov/" ){target=_blank} 
or by using the User Tokens API. 

Once you have a valid EDL token, open the Swagger UI interface for the HyP3 API. Click the **Authorize** button, 
and enter or paste your EDL token in the **Value** field in the BearerAuth section. 

![Authorize EDL Token in API](../images/api-authorize.png "Authorize an EDL Token in the HyP3 API")


## Authentication with HyP3 Python SDK







Authentication is not required for using download links once you have them, but you must authenticate 
in order to look up the download URLs for On Demand products.