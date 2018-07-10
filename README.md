# Bulk_Add_Halo_Users
CloudPassage Halo Bulk User Add

Disclaimer: This script is provided as is. USE AT YOUR OWN RISK.
NOT A SUPPORTED SOLUTION

Disclaimer: This script uses an undocumented endpoint, which is subject to change.
NOT RECOMMENDED FOR PRODUCTION ENVIRONMENTS.

# Configure

To configure script add API Key information to cloudpassage.yml File
>key_id: your_api_key_id
>secret_key: your_api_secret_key


# Requirements

1. This script requires Python 2.7.10 or greater.

2. This script requires the CloudPassage Python SDK
> pip install cloudpassage

3. This script requires the Requests Python module.
> pip install requests

4. This script requires the CSV Python module.
> pip install csv

If you want to make modifications to the SDK you can
install it in editable mode by downloading the source from
the below github repo, navigating to the top directory within
the archive and running "pip install -e ."
(note the . at the end).
Or you can visit https://github.com/cloudpassage/cloudpassage-halo-python-sdk to
clone it directly from our github.


# Running

Run python bulk_useradd.py to create new users from a local .csv file.
File must be in the format of:
username,firstname,lastname,email,sms_phone_number,role,group_id
(See users.csv for an example)

csv.DictReader expects field names in the first line of the file and will skip over any
user data you put in that line.

You will need to set the scope of the user using the group_id field.
To get the group ID, highlight the group name in the left-hand pane in the Environment
screen.  The group ID will be in your URL, e.g.:

https://portal.cloudpassage.com/halo/environment/group/<group_id>/summary

This script has not been tested with multiple roles or with blank phone numbers.



# License

Copyright (c) 2018, CloudPassage, Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of the CloudPassage, Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL CLOUDPASSAGE, INC. BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED ANDON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
