# EasyGAR

> Request a Google Analytics report. Get a Pandas `DataFrame`.

Do you often use Google Analytics Reporting API in Python? Do you analyze Google Analytics data with Pandas? If yes, then EasyGAR is for you!

EasyGAR takes the pain out of using the Google API Python Client and automatically converts API responses to pandas `DataFrame` objects. It comes with support for several metrics and dimensions (including simple metric arithemtic!), and even handles pagination for you!

> **NOTE:** EasyGAR is still under construction. It doesn't even have an alpha release yet! If you find a bug, please open an issue. If you would like to contribute, please see our [guidelines for contributing](https://github.com/somacdivad/easy-ga-reporting/blob/master/CONTRIBUTING.md).

## Installation

Currently, the only way to install EasyGAR is with `setup.py`. Clone this repository and then run the following in the directory you cloned into:

```console
$ python setup.py install
```

> **IMPORTANT:** EasyGAR requires Python 3.6+.

## Basic Usage

Here's a sample script illustrating basic usage fo EasyGAR:

```python
from easy_gar import API, metrics, dimensions

ga = API("client_secrets.json", "XXXXXXXXX")

rpt = ga.get_report(
    start_date="7daysAgo",
    end_date="today",
    metrics=[metrics.users]
)

print(rpt)
```

Running that will give you output that looks something like this:

```
          Users
Date
20180511  458.0
20180512  407.0
20180513  322.0
20180514  544.0
20180515  497.0
20180516  518.0
20180517  488.0
20180518  235.0
```

Note that if no dimension is specified, the Date dimension is used. You can specify up to 10 metrics (API limitation):

```python
rpt = ga.get_report(
    start_date="7daysAgo",
    end_date="today",
    metrics=[metrics.users, metrics.sessions, metrics.pageviews, metrics.unique_pageviews]
)
```

That ouputs:

```
          Users  Sessions  Pageviews  Unique Page Views
Date                                                   
20180511  458.0     503.0      969.0              762.0
20180512  407.0     437.0      787.0              631.0
20180513  322.0     352.0      586.0              489.0
20180514  544.0     598.0     1304.0              960.0
20180515  497.0     541.0     1128.0              856.0
20180516  518.0     571.0     1148.0              909.0
20180517  488.0     543.0     1101.0              849.0
20180518  236.0     253.0      455.0              373.0
```

To add dimensions, just pass a list to the `dimensions` keyword of `.get_report()`:

```python
rpt = ga.get_report(
    start_date="yesterday",
    end_date="today",
    metrics=[metrics.users],
    dimensions=[dimensions.date, dimensions.continent]
)
```

```
                    Users
Date     Continent       
20180517 Africa       1.0
         Americas   483.0
         Asia         3.0
         Europe       1.0
20180518 Americas   231.0
         Asia         5.0
         Europe       2.0
```

### Metric Arithmetic

Metrics support basic arithmetic. For example, the following returns a metric calculating sessions per user:

```python
sessions_per_user = metrics.sessions / metrics.user
```

Of course, you could just use the built in `metric.sessions_per_user` metric. But arithemtic allows for calculating metrics that aren't available in Google Analytics:

```python
unique_pageviews_per_user = metrics.unique_pageviews / metrics.users

combined_value = metrics.goal01_value + metrics.goal02_value
```

Here's what that looks like:

```python
rpt = ga.get_report(
    start_date="7daysAgo",
    end_date="today",
    metrics=[metrics.unique_pageviews / metrics.users],
)
```

```
          Unique Page Views / Users
Date                               
20180511                   1.663755
20180512                   1.550369
20180513                   1.518634
20180514                   1.764706
20180515                   1.722334
20180516                   1.754826
20180517                   1.739754
20180518                   1.585774
```

### Metric Aliases

You can provide an alias to metrics to customize the fieldname in the `DataFrame` if needed:

```python
unique_pageviews_per_user = metrics.unique_pageviews / metrics.users
unique_pageviews_per_user.alias = "Unique Pageviews per User"

rpt = ga.get_report(
    start_date="7daysAgo",
    end_date="today",
    metrics=[unique_pageviews_per_user],
)
```

```
          Unique Pageviews per User
Date                               
20180511                   1.663755
20180512                   1.550369
20180513                   1.518634
20180514                   1.764706
20180515                   1.722334
20180516                   1.754826
20180517                   1.739754
20180518                   1.593361
```

