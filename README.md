# GET-COUNTRY-CODES

Write a function that will return a string of country codes from an argument that is a string of prices (containing dollar amounts following the country codes).

Your function will take as an argument a string of prices like the following: `"US\$40, AU\$89, JP$200"`.

In this example, the function would return the string "US, AU, JP".

Hint: You may want to break the original string into a list, manipulate the individual elements, then make it into a string again.

---

**It may be helpful to look into splitting strings by a `delimiter`.**
There's a good chance most of us have come across a `.csv` file, or maybe even an `excel` file.

A `CSV` or `Comma Separated Value` file has a `,` as a `delimiter` as follows:

```bash
119736,FL,CLAY COUNTY,498960,498960,498960,498960,498960,792148.9,0,9979.2,0,0,30.102261,-81.711777,Residential,Masonry,1
```

The information above represents what you could think of as a single row in an excel file. Each value is it it's own "column" separated by comma. This is a common way `tabular` data is stored into text files which are then shared.

When someone wants to read the data into a program variable list, or some other program, they need to know what `delimits` the values, in the case of a `csv`, a comma (generally). So when someone reads a line in  a csv, they know each value is separated by a comma!