# EasyGAR

> Request a Google Analytics report. Get a Pandas `DataFrame`.

Do you often use Google Analytics Reporting API in Python? Do you analyze Google Analytics data with Pandas? If yes, then EasyGAR is for you!

EasyGAR takes the pain out of using the Google API Python Client and automatically converts API responses to pandas `DataFrame` objects. It comes with support for several metrics and dimensions (including simple metric arithemtic!), and even handles pagination for you!

> **NOTE:** EasyGAR is still under construction. It doesn't even have an alpha release yet! If you find a bug, please open an issue. If you would like to contribute, please see our [guidelines for contributing](https://github.com/somacdivad/easy-ga-reporting/blob/master/CONTRIBUTING.md).

## Table of Contents

- [Installation](#installation)
- [Basic Usage](#basic-usage)
  - [Getting an API Instance](#getting-an-api-instance)
  - [Creating a Report](#creating-a-report)
  - [Adding Dimensions](#adding-dimensions)
  - [Metric Arithmetic](#metric-arithmetic)
  - [Metric Aliases](#metric-aliases)
  - [Ordering Results](#ordering-results)

## Installation

Currently, the only way to install EasyGAR is with `setup.py`.

```console
python setup.py install
```

> **IMPORTANT:** EasyGAR requires Python 3.6+.

## Basic Usage

EasyGAR works with a `client_secrets.json` file. If you don't have one already, you can get one from the Google APIs [Credentials page](https://console.developers.google.com/apis/credentials). For more information, see the [client secrets guide](https://developers.google.com/api-client-library/python/guide/aaa_client_secrets).

To instantiate the API with your `client_secrets.json` and a Google Analytics View that you have access to:

### Getting an API Instance

```python
from easy_gar import API

ga = API("path/to/client_secrets.json". "<VIEWID>")
```

> **Note:** If you have not authorized your application to access your user daya, your default browser will open to the Google authorization page. This process creates as `Flow` object that is pickled and stored for future access.

### Creating a Report

The basic method of the `API` class is `.get_report()`, which is used to query the Google Analytics Reporting API and store the results in a pandas `DataFrame`. The `.get_report()` method returns a `Report` object with the `DataFrame` accessible via `Report.DataFrame`.

Here's a sample script illustrating basic usage of EasyGAR:

```python
from easy_gar import API, metrics, dimensions

ga = API("client_secrets.json", "<VIEWID>")

rpt = ga.get_report(
    start_date="7daysAgo",
    end_date="today",
    metrics=[metrics.users]
)

print(rpt)
```

Running that will give you output that looks something like this:

```console
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

```console
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

### Adding Dimensions

To add dimensions, just pass a list to the `dimensions` keyword of `.get_report()`:

```python
rpt = ga.get_report(
    start_date="yesterday",
    end_date="today",
    metrics=[metrics.users],
    dimensions=[dimensions.date, dimensions.continent]
)
```

```console
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

```console
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

```console
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

### Ordering Results

You can order your results by passing an `OrderBy` object to the `order_by` keyword argument of `.get_report()`:

```python
rpt = ga.get_report(
    start_date="7daysAgo",
    end_date="today",
    metrics=[metrics.users],
    dimensions=[dimensions.continent]
    order_by=[
        easy_gar.OrderBy(
            field_name=metrics.users,
            sort_order="DESCENDING",
        ),
    ],
)
```

```console
            Users
Continent
Americas   3379.0
Asia         24.0
Europe       11.0
(not set)     3.0
Africa        2.0
```

Valid values for `sort_order` are `ASCENDING` (default) and `DESCENDING`. These values can also be retrieved with `easy_gar.sort_order.ascending` and `easy_gar.sort_order.descending`, if you like.

The `field_name` keyword argument can be any dimension or metric, and you can order by multiple fields:

```python
rpt = ga.get_report(
    start_date="7daysAgo",
    end_date="today",
    metrics=[metrics.users],
    dimensions=[dimensions.continent, dimensions.date],
    order_by=[
        OrderBy(
            field_name=dimensions.continent,
            sort_order="ASCENDING"
        ),
        OrderBy(
            field_name=metrics.users,
            sort_order="DESCENDING",
        ),
    ],
)
```

```console
                    Users
Continent Date
(not set) 20180514    3.0
Africa    20180513    1.0
          20180517    1.0
Americas  20180514  537.0
          20180516  513.0
          20180515  492.0
          20180517  483.0
          20180518  457.0
          20180511  454.0
          20180512  405.0
          20180513  316.0
Asia      20180518    6.0
          20180513    5.0
          20180516    4.0
          20180514    3.0
          20180515    3.0
          20180517    3.0
          20180511    1.0
          20180512    1.0
Europe    20180511    3.0
          20180515    2.0
          20180518    2.0
          20180512    1.0
          20180514    1.0
          20180516    1.0
          20180517    1.0
```