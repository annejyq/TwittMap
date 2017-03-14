## TwittMap
1. Assignment 1 COMS E6998 Cloud Computing & Big Data
2. Yunqing Jiang  UNI:yj2407
3. Keyi Yang      UNI:ky2343
4. http://twittermap.nfvaftgznc.us-west-2.elasticbeanstalk.com/

## Step 1: Create ElasticSearch Domain
1. Run the following command:
```
aws es create-elasticsearch-domain --domain-name twittmap --elasticsearch-cluster-config InstanceType=t2.micro.elastic
search,InstanceCount=1 --ebs-options EBSEnabled=true,VolumeType=gp2,VolumeSize=10
```
2. Configure the access policy to allow open access to the domain

## Step 2: Create Index and Type in ElasticSearch
1. Run the following command to create an index (database) called twittmap and a type (table) called tweets. 'Geo' is configured as gwo_point variable for geospatial searching.
```
curl -XPUT search-twittmap-z7jgounce6usksgcxt4kbsruvi.us-east-1.es.amazonaws.com/twittmap -d '
{
    "mappings": {
        "tweets": {
            "properties": {
                "user": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "time": {
                    "type": "date"
                },
                "text": {
                    "type": "string"
                },
                "geo": {
                    "type": "geo_point"
                }
            }
        }
    }
}'
```

## Step 3: Fetch tweets from the twitter in real-time
1. Create an ubuntu (14.0 or 16.0) EC2 instance
2. Pull the repo from Github, `cd` into `streaming`, and run `pip install -r requirements.txt`.
3. Run `python streaming.py & python tokens.py`

## Step 4: Create a Web Application
1. Create a Web App using Django to let users choose keyword via a drop-down box
2. Send keyword by POST Request from web page to to back-end web app.
3. Initialize Google Map using Google Maps API.

## Step 5: Query Tweets
1. Using Django as back-end server to query ElasticSearch according to keyword selected by users.
2. Once ES responds to the server, the server then sends the response as JSON payload to the front-end.

## Step 6: Visualization
1. Locate tweets and place a marker with regard to geometry information.
2. Add a listener Event for each marker. Whenver the user clicks the marker, an infowindow is created and popped out.

## Step 7: Search Tweets by Geolocation
1. Set a toggle button to enable Geolocation search mode.
2. Set a map listener for click event, use acquired geolocation information to query ES database.

## Step 8: Deploying to Amazon Elastic Beanstalk
1. Deploy the Web App and Streaming.py onto ELB according to `ELB_build_up.txt`
