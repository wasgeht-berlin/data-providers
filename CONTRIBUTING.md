# CONTRIBUTING

Currently, there are two ways to contribute event data to wasgeht. For services providing an iCal-Subscription of their events, that can easily be added with some meta information in a YAML-file. More help on that can be found in the section on iCal-Subscriptions below. Usually though, it will unfortunately be necessary to scrape data from a website. Adding a scraper is described in more detail in the scrapers chapter.

## Scrapers

## iCal-Subscriptions

### Schema
```yaml

- subscription name:
    - url: "ical://subscription.url"
    - updateFrequency: "daily|weekly|monthly"
    - category: "a schema.org sub-event type, e.g. LiteraryEvent, EducationEvent, etc."
```

- `updateFrequency` can be left off, defaults to `monthly`
- http://schema.org/Event
