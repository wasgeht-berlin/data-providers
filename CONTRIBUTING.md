# CONTRIBUTING

Currently, there are two ways to contribute event data to wasgeht. For
services providing an iCal-Subscription of their events, that can easily be
added with some meta information in a YAML-file. More help on that can be
found in the section on iCal-Subscriptions below. Usually though, it will
unfortunately be necessary to scrape data from a website. Adding a scraper is
described in more detail in the scrapers chapter.

## Scrapers

Scrapers are (usually) short scripts which extract information from a website.
This project allows for data input from scrapers by defining an output format
and a configuration file on how to run the script.

All files related to a scraper reside in an appropriately named directory
under `/scrapers/`. You need to at least provide a `scraper.yml` and an
executable script file. Currently, scrapers are expected to be runnable with
Python 3, using the standard libraries and Beautiful Soup 4.

### Configuration

```yaml
name: My Scraper # Human readable name, e.g. the website's name
main: script.py # Path to script, relative from scraper root directory
interpreter: python3 
output: json|yaml # (optional)
```

### Scraper Output

The system expects scrapers to output a list of events in JSON or YAML format. These events must contain at least the following properties:

- `title`
- `description`
- `url`
- `starting_time`
- `hash`

and a `location` object containing at least a `human_name` property.

Additionally, events may include:

- `ending_time`
- `tags`
- `notes`

The `location` object may be amended with:

- `human_street_address`
- `lat`
- `lon`
- `url`
- `osm_feature_id`
